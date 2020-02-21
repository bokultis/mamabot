# from gtts import gTTS
from playsound import playsound

import speech_recognition as sr
# import wave
# import pyaudio

# myText = "Boris presvuci beba"

# output = gTTS(text=myText, lang="sk")

# output.save("output.wav")

# playsound("output.wav")
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Recording...")
#     # read the audio data from the default microphone
#     audio_data = r.record(source, duration=5)
#     print("Recognizing...")

# playsound(audio_data)

#     # # convert speech to text
#     # text = r.recognize_google(audio_data)
#     # print(text)
# audio = pyaudio.PyAudio()
# print("----------------------record device list---------------------")
# info = audio.get_host_api_info_by_index(0)
# numdevices = info.get('deviceCount')
# for i in range(0, numdevices):
#     if (audio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
#         print ("Input Device id ", i, " - ", audio.get_device_info_by_host_api_device_index(0, i).get('name'))

# print("-------------------------------------------------------------")



# ding_wav = wave.open("file_example_WAV_1MG.wav", 'rb')
# ding_data = ding_wav.readframes(ding_wav.getnframes())
# audio = pyaudio.PyAudio()
# stream_out = audio.open(
#     format=audio.get_format_from_width(ding_wav.getsampwidth()),
#     channels=ding_wav.getnchannels(),
#     rate=ding_wav.getframerate(), input=False, output=True)
# stream_out.start_stream()
# stream_out.write(ding_data)
# time.sleep(0.2)
# stream_out.stop_stream()
# stream_out.close()
# audio.terminate() 
import pyaudio
import wave
 
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 2
WAVE_OUTPUT_FILENAME = "file.wav"
 
audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print ("recording...")
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print ("finished recording")
 
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

playsound("file.wav")

r = sr.Recognizer()
with sr.AudioFile("file.wav") as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)