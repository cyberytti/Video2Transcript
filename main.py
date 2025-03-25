from functions.video_to_wav import video_to_wav
from functions.wav_to_16kwav import wav_to_16kwav
from functions.convertedwav_to_transcript import transcribe
from functions.transcript_lan_covert import translate_list
import os
from typing import List, Dict
from pathlib import Path

def delete_files(file_paths: List[str]) -> bool:
    """Delete multiple files and return True if all deletions succeed."""
    success = True
    for file_path in file_paths:
        try:
            if Path(file_path).is_file():
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            else:
                print(f"Not found: {file_path}")
                success = False
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
            success = False
    return success

def process_video_to_transcript(
    video_path: str, 
    target_language: str = "bengali"
) -> List[Dict]:
    """
    Convert video to translated transcript with cleanup.
    
    Args:
        video_path: Path to input video file
        target_language: Target language for translation
    
    Returns:
        List of dictionaries containing transcript with translations
    """
    # Temporary file names
    TEMP_WAV = "output_audio.wav"
    TEMP_16K_WAV = "audio_16k.wav"

    try:
        # Process video through conversion pipeline
        wav_file = video_to_wav(video_path)
        converted_wav = wav_to_16kwav(wav_file)
        transcript = transcribe(converted_wav)

        if not transcript:
            raise ValueError("Transcription failed or returned empty result")

        # Extract texts and translate
        texts = [entry['text'] for entry in transcript]
        translations = translate_list(texts, target_language)

        # Combine results using list comprehension
        final_output = [
            {
                "id": entry['id'],
                "start": entry['start'],
                "end": entry['end'],
                "text": translations[i]
            }
            for i, entry in enumerate(transcript)
        ]

        return final_output

    except Exception as e:
        print(f"Error processing video: {e}")
        return []

    finally:
        # Cleanup temporary files
        delete_files([TEMP_WAV, TEMP_16K_WAV])

def main():
    video_path = "/home/sagnik/Downloads/test.mp4"
    result = process_video_to_transcript(video_path, "bengali")
    print(result)

if __name__ == "__main__":
    main()