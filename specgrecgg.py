import speech_recognition as sr

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    r.energy_threshold = 4000
    # obtain audio from the microphone

    with sr.Microphone(3) as source:
        # r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)

        # Speech recognition using Google Speech Recognition
        data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_sphinx(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        speak("Sorry sir, but, I could not understand what you said!")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


