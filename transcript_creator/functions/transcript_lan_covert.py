from openai import OpenAI

# Initialize client once as a constant
CLIENT = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama',  # required, but unused
)

def extract_translation(text):
    """Extract text between <translation> tags."""
    try:
        start = text.index('<translation>') + 13  # 13 is len('<translation>')
        end = text.index('</translation>')
        return text[start:end] if start < end else ""
    except ValueError:
        return ""

def translate(text_to_translate, target_language):
    """Translate text to target language using the API."""
    try:
        response = CLIENT.chat.completions.create(
            model="gemma3:12b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a translator. Your task is to assist users with translations. "
                        "When a user provides text and specifies a target language, translate "
                        "that text accurately into the requested language and enclose the "
                        "translation within <translation> tags. Ensure the translation is "
                        "natural, contextually appropriate, and faithful to the original meaning."
                    )
                },
                {
                    "role": "user",
                    "content": f"Text: {text_to_translate}.\n\nTranslate it into {target_language}"
                }
            ]
        )
        return extract_translation(response.choices[0].message.content)
    except Exception as e:
        print(f"Translation error: {e}")
        return ""

def translate_list(texts, target_language):
    """Translate a list of texts to target language."""
    return [translate(text, target_language) for text in texts]

