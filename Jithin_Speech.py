#!/usr/bin/python

import speech_recognition as sr
import os
import pyaudio
pa = pyaudio.PyAudio()
i = pa.open(rate=44100, format=pyaudio.paFloat32, channels=2, input=True)
d = i.read(41000 * 10)
o = pa.open(rate=44100, format=pyaudio.paFloat32, channels=2, output=True)
o.write(d)

def try_devices(index) :
    try:
        r = sr.Recognizer()
        m= sr.Microphone(device_index = index, sample_rate = 44100, chunk_size = 512)
        with m as source:
            r.adjust_for_ambient_noise(source)
            print("Set minimum energy threshold to {}".format(r.energy_threshold))
            while True:
                print("Say something!")
                audio = r.listen(source)
                print("Got it! Now to recognize it...")
                try:
                    value = r.recognize_sphinx(audio)
                    if str is bytes: # this version of Python uses bytes for string (Python 2)
                        print("You said {}".format(value).encode("utf-8"))
                    else: # this version of Python uses unicode for strings (Python 3+)
                        print("You said {}".format(value))
                except sr.UnknownValueError:
                    print("Oops! Didn't catch that")
                except LookupError:
                    print("Oops! Didn't catch that")
                except IOError:
                    print("Oops! Didn't catch that")
    except Exception as e:
        print("Error in device"+str(e))


mic_list = sr.Microphone.list_microphone_names()
for i, microphone_name in enumerate(mic_list):
    print (str(i) + ": " +microphone_name)
    try_devices(i)
