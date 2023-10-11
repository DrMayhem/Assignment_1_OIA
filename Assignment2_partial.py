from playsound import playsound 
import speech_recognition as sr 
from googletrans import Translator 
from gtts import gTTS 
import os 

# A dictionary containing language names and their codes
language_codes = {
    'english': 'en',
    'hindi': 'hi',
    'telugu': 'te',
}

# Function to recognize speech from an audio file
def recognize_audio_file(audio_file):
    r = sr.Recognizer() 
    with sr.AudioFile(audio_file) as source: 
        print("Recognizing...")
        audio = r.record(source) 

    try: 
        query = r.recognize_google(audio, language='en-in') 
        print(f"Text in the audio: {query}\n") 
        return query
    except Exception as e: 
        print("Speech Recognition could not understand the audio")
        return "None"

# Input from user
# Replace the filename with the path to your audio file
audio_file_path = r"C:\Users\Umansh Agarwal\Downloads\Openinapp\output.wav"
query = recognize_audio_file(audio_file_path)
while query == "None": 
    query = recognize_audio_file(audio_file_path)

# Translate to English
to_lang_code = language_codes['english']
translator = Translator()
translated_text_english = translator.translate(query, dest=to_lang_code).text

# Translate to Hindi
to_lang_code = language_codes['hindi']
translated_text_hindi = translator.translate(query, dest=to_lang_code).text

# Translate to Telugu
to_lang_code = language_codes['telugu']
translated_text_telugu = translator.translate(query, dest=to_lang_code).text

# Specify the output directory for saving audio files
output_directory = r"C:\Users\Umansh Agarwal\Downloads\Openinapp"

# Save translations to audio files
for lang, translated_text in zip(['english', 'hindi', 'telugu'], [translated_text_english, translated_text_hindi, translated_text_telugu]):
    # Translating from source to destination using gTTS
    tts = gTTS(text=translated_text, lang=language_codes[lang], slow=False)
    output_file_path = os.path.join(output_directory, f"translated_audio_{lang}.mp3")
    tts.save(output_file_path)

# Provide information about saving the audio files
print(f"Audio files saved in {output_directory}.")
