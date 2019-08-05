import pyttsx3
print("start")
engine = pyttsx3.init()
engine.say('Hi Corefactors')
print("done")
engine.say('You guys are wonderful')
engine.runAndWait()
print("end")