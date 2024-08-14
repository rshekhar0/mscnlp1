'''
pip install SpeechRecognition
pip install pyaudio  # For capturing microphone input


'''


import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the microphone as the source for input.
with sr.Microphone() as source:
    print("Adjusting for ambient noise, please wait...")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Listening...")
    audio_data = recognizer.listen(source)
    print("Processing...")

# Use Google Speech Recognition
try:
    text = recognizer.recognize_google(audio_data)
    print(f"Transcribed Text: {text}")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")


