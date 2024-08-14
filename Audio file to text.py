import speech_recognition as sr

def transcribe_audio(a):
    # Create a Recognizer instance
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile("C:\\Users\\schau\\Downloads\\NLP-Codes\\temp.wav") as source:
        audio_data = recognizer.record(source)  # Read the entire audio file

    # Recognize (convert from speech to text)
    try:
        text = recognizer.recognize_google(audio_data)
        print(f"Transcribed Text: {text}")
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from the service; {e}")

# Example usage
transcribe_audio("temp.wav")
