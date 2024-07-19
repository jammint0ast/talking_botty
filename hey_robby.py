import pvporcupine
from pvrecorder import PvRecorder
from datetime import datetime

import sounddevice


import speech_recognition as sr
r = sr.Recognizer()
mic_devices = sr.Microphone.list_microphone_names()
mic_device = mic_devices.index("default")
mic = sr.Microphone(device_index=mic_device, sample_rate=22050)

with mic as source:
    r.adjust_for_ambient_noise(source)
    #audio = r.listen(source)
        
import pyttsx3
engine = pyttsx3.init()

def get_speech_input(language="english", model="small.en"):
    with mic as source:
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    return r.recognize_whisper(audio, language=language, model=model)

keywords = ["computer"]
keyword_paths = ['picovoice/hey-robby_en_linux_v2_1_0.ppn', 'picovoice/S-O-S-abort_en_linux_v2_1_0.ppn']
for keyword in keywords:
    keyword_paths.append(pvporcupine.KEYWORD_PATHS[keyword])

keywords.insert(0, "S-O-S Abort")
keywords.insert(0, "Hey Robby!")

print(keywords)
print(keyword_paths)

porcupine = pvporcupine.create(
  access_key='MN667eSAK/O+tM+fXUeOaOhI3uap8rOuiTgOwKwm7JUy3eiOZ6lnpg==',
  keyword_paths=keyword_paths
)

recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
recorder.start()

print('Using device: %s', recorder.selected_device)

while True:
  pcm = recorder.read()
  result = porcupine.process(pcm)
  if result >= 0:
    print('[%s] Detected %s' % (str(datetime.now()), keywords[result]))
  if result == 1:
      break
  if result == 0:
      recorder.stop()
      engine.say("Yes Captain?")
      engine.runAndWait()
      input = get_speech_input()
      print(input)
      recorder.start()
        

