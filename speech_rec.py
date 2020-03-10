import speech_recognition as sr
import myspsolution as mysp

sr.__version__

script = ["hello there, please introduce yourselves and icebreaker",
          "Welcome to Test Your Bias! A way to facilitate learning about bias, internally and externally",
          "Let's begin. Tell each about a time when you experienced prejudice.",
          "Excellent. Tell me about your most recent aha moment"]
state = 0
r = sr.Recognizer()

mic = sr.Microphone()
transcription = []
c=r"./" # Path to the Audio_File directory (Python 3.7)


LuisAppId = "8468f0ba-5923-4ad3-9285-9c9e57ff921c"
LuisAPIKey = "275c1674cf9e484680a0e7500202abef"
LuisAPIHostName = "eastus.api.cognitive.microsoft.com"
AZURE_SPEECH_KEY = "1ea5ab6891654c78b6d5a40aade2864e"

for state in range(0, 3):
    print(script[state])
    with mic as source:
        fn = "microphone-results{}.wav".format(state)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        with open(fn, "wb") as f: #44100, 2
            f.write(audio.get_wav_data())
        f.close()
        response = {}
        try:
           transcription = r.recognize_google(audio)
           print(transcription)
           #askMode
           #listenMode
           #determineIntent()
           #how fast slow/ loud/soft pauses
           #promptMode -keywords, phrases
           #per personality
           #storyMode
           #fork
           mysp.myspgend(fn, c)
           mysp.mysptotal(fn, c)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"

