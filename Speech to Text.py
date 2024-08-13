# Convert audio file Speech to Text.

#pip install SpeechRecognition
#pip install pydub
import speech_recognition as sr  # Importing the SpeechRecognition library.
from pydub import AudioSegment  # Importing the AudioSegment class from the pydub library.

# Initialize the recognizer
recognizer = sr.Recognizer()  # Creating a Recognizer instance for speech recognition.

# Load the MP3 audio file
audio_file_mp3 = "C:\\Users\\DELL\\Desktop\\STUDIES\\NLP\\welcomeNK.mp3"  # Setting the path to the input MP3 audio file.

# Load audio file as AudioSegment
audio = AudioSegment.from_mp3(audio_file_mp3)  # Loading the MP3 audio file as an AudioSegment object.

# Export AudioSegment to WAV format
audio_file_wav = "C:\\Users\\DELL\\Desktop\\STUDIES\\NLP\\welcomeNK.wav"  # Setting the path for the output WAV audio file.
audio.export(audio_file_wav, format="wav")  # Exporting the AudioSegment to WAV format.

# Load WAV audio file as audio data
with sr.AudioFile(audio_file_wav) as source:  # Opening the WAV audio file as an AudioFile object.
    audio_data = recognizer.record(source)  # Recording the audio data from the WAV file.

# Recognize speech using Google Speech Recognition
try:
    text = recognizer.recognize_google(audio_data)
    print("Recognized speech:", text)
except sr.UnknownValueError:
    print("Speech recognition could not understand the audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
