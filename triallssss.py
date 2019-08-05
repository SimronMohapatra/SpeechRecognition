import pyaudio
pa = pyaudio.PyAudio()
i = pa.open(rate=44100, format=pyaudio.paFloat32, channels=2, input=True)
d = i.read(41000 * 10)
o = pa.open(rate=44100, format=pyaudio.paFloat32, channels=2, output=True)
o.write(d)