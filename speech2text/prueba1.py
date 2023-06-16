import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

with sr.Microphone() as source:
    # read the audio data from the default microphone
    print("Grabando...")
    # reduce ambient noise
    r.adjust_for_ambient_noise(source)
    audio_data = r.listen(source)
    # convert speech to text

    text = r.recognize_google(audio_data, language="es-MX")
    print(text)

