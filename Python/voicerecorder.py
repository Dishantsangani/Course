import sounddevice
from scipy.io.wavfile import write
fs=44100
second=int(input("enter the time duration in second:"))
print("Recording..\n")
record_voice=sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
sounddevice.wait()
write("out.mp3",fs,record_voice)
print("finished..\nplease check it..")