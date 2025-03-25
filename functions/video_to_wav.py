from moviepy.editor import VideoFileClip

def video_to_wav(video_path):
    output_audio_path = "output_audio.wav"
    try:
        # Extract audio
        video = VideoFileClip(video_path)
        video.audio.write_audiofile(output_audio_path, codec='pcm_s16le')  # WAV format
        return output_audio_path
    except Exception as error:
        return (error)
        exit()


