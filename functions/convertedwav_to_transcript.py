from groq import Groq


client = Groq(api_key="<grok-api-key>") 

def transcribe(filename):
    with open(filename, "rb") as file:
        transcription = client.audio.transcriptions.create(
        file=(filename, file.read()),
        model="whisper-large-v3",
        response_format="verbose_json",
        )
        return (transcription.segments)
      

