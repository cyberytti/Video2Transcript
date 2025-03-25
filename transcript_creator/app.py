# app.py
from flask import Flask, render_template, request, jsonify, send_from_directory
import subprocess
import os
import json
from main import process_video_to_transcript  # Import the main processing function
from typing import List, Dict
from pathlib import Path

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
ALLOWED_EXTENSIONS = {'mp4'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_directories():
    """Create necessary directories if they don't exist."""
    for folder in [UPLOAD_FOLDER, OUTPUT_FOLDER]:
        if not os.path.exists(folder):
            os.makedirs(folder)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    create_directories()  # Ensure directories exist

    if 'video' not in request.files:
        return jsonify({'error': 'No video file part'}), 400
    file = request.files['video']
    target_language = request.form.get('language', 'bengali')  # Default to Bengali

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(video_path)

        try:
            # Call the processing function from main.py
            transcript_data: List[Dict] = process_video_to_transcript(video_path, target_language)

            if not transcript_data:
                return jsonify({'error': 'Processing failed or returned empty result'}), 500

            # Create a unique output filename
            output_filename = os.path.splitext(file.filename)[0] + '_transcript.json'
            output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)

            # Save the transcript data to a JSON file
            with open(output_path, 'w', encoding='utf-8') as outfile:
                json.dump(transcript_data, outfile, ensure_ascii=False, indent=4)

            # Return the path to the output file for download
            return jsonify({'success': True, 'download_url': f'/download/{output_filename}'})

        except Exception as e:
            return jsonify({'error': str(e)}), 500
        finally:
            # Clean up the uploaded video file
            if Path(video_path).is_file():
                os.remove(video_path)
                print(f"Deleted uploaded video: {video_path}")

    else:
        return jsonify({'error': 'Invalid file type'}), 400

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    create_directories()
    app.run(debug=True)