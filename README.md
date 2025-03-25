# 🎥 Video to Transcript Converter 🌐

A Flask web application that converts video files into translated transcripts using AI-powered speech recognition and translation.

![Project Screenshot](https://via.placeholder.com/800x500.png?text=Video+to+Transcript+Converter)

## ✨ Features

- 🎤 Extract audio from MP4 videos
- 🔉 Convert audio to 16kHz WAV format (optimal for speech recognition)
- 🗣️ Transcribe audio using Groq's Whisper model
- 🌍 Translate transcripts to multiple languages using Gemma3 AI
- 💾 Download transcripts as JSON files
- 🎨 Modern, responsive UI with progress tracking

## 📋 Prerequisites

Before you begin, ensure you have:

- Python 3.8+
- [Ollama](https://ollama.ai/) running locally with Gemma3 model
- Groq API key (for Whisper transcription)
- FFmpeg installed (for audio processing)

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/video-to-transcript.git
   cd video-to-transcript
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up grok api key**:
   ```
   set your grok api key in convertedwav_to_transcript.py file 
   ```

5. **Set up environment variables**:
   Create a `.env` file in the root directory with:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## 🚀 Running the Application

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Access the application**:
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## 🖥️ Usage

1. Upload an MP4 video file
2. Select target language for translation
3. Click "Process Video"
4. Wait for processing to complete
5. Download the JSON transcript file

## 📂 Project Structure

```
video-to-transcript/
├── app.py                # Main Flask application
├── main.py               # Core processing logic
├── functions/
│   ├── video_to_wav.py   # Video to WAV conversion
│   ├── wav_to_16kwav.py  # Audio format conversion
│   ├── convertedwav_to_transcript.py  # Speech recognition
│   └── transcript_lan_covert.py       # Translation
├── templates/
│   └── index.html        # Frontend interface
├── static/
│   ├── script.js         # Client-side JavaScript
│   └── style.css         # Styling
├── uploads/              # Temporary video storage
└── outputs/              # Generated transcripts
```

## 🔧 Configuration

You can modify the following in `app.py`:
- `UPLOAD_FOLDER`: Change the upload directory
- `ALLOWED_EXTENSIONS`: Add more video formats if needed

In `main.py`, you can adjust:
- Temporary file names
- Error handling behavior

## 🌐 Supported Languages

The application supports translation to:
- Bengali (default)
- English
- Hindi
- Spanish
- French
- Portuguese
- German
- Russian
- Italian
- Dutch
- Chinese (Simplified)
- Japanese
- Korean
- Arabic

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Troubleshooting

- **Audio processing fails**: Ensure FFmpeg is installed and in your PATH
- **Translation errors**: Verify Ollama is running and Gemma3 model is downloaded
- **API errors**: Check your Groq API key in the `.env` file
- **File permission issues**: Ensure the `uploads` and `outputs` directories are writable

## 📧 Contact

For support or questions, please contact [your-email@example.com](mailto:your-email@example.com)
