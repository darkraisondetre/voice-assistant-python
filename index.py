# Голосовой ассистент КЕША 1.0 BETA
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime

opts = {
    "alias": ('Edit', 'edt', 'hey edit', ''),
    "tbr": ('say','tell','show','how many'),
    "cmds": {
        "ctime": ('current time','time is it', 'time is it now', 'time'),
        "radio": ('play music', 'turn music', 'turn on the music','turn on the radio','turn radio'),
        "joke": ('tell joke','tell the joke')
    }
}

# функции
def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
        print("[log] Recognized: " + voice)
    
        if voice.startswith(opts["alias"]):
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()
            
            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()
            
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("[log] Speech not recognized!")
    except sr.RequestError as e:
        print("[log] Undefined error, check internet connection!")

def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    
    return RC

def execute_cmd(cmd):
    if cmd == 'ctime':
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
    
    elif cmd == 'radio':
        os.system("D:\\led-zeppelin-stairway-to-heaven.mp3")
    
    elif cmd == 'joke':
        speak("It's a simple joke")
    
    else:
        print('Command not recognized, please try again!')

# запуск
r = sr.Recognizer()
# m = sr.Microphone(device_index = 0)

# with m as source:
#     r.adjust_for_ambient_noise(source)

# speak_engine = pyttsx3.init()

# voices = speak_engine.getProperty('voices')
# speak_engine.setProperty('voice', voices[4].id)

# forced cmd test
# speak("Зашли как то в бар латинос, русский и американец")

# os.system("D:\\led-zeppelin-stairway-to-heaven.mp3")
# stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1) # infinity loop