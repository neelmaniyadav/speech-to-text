import speech_recognition as sr
AUDIO_FILE=('maniraj2.Wav')

r=sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)

try:
    print("audio file contains "+ r.recognize_google(audio))
except sr.UnknownValueError :
    print("Google Speech Recognition could not understand audio")
except sr.RequestError :
    print("couldn't get the results from Google Speech Recognition")
