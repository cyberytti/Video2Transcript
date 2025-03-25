from pydub import AudioSegment


def wav_to_16kwav(original_audio_path):
    try:
        # Convert to compatible format: 16kHz WAV, Mono
        audio = AudioSegment.from_file(original_audio_path)
        audio = audio.set_frame_rate(16000).set_channels(1)
        converted_audio_path = "audio_16k.wav"
        audio.export(converted_audio_path, format="wav")
        return converted_audio_path
    except Exception as error:
        print (error)
        exit()

