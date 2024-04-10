import os
import config
import stt
import tts
from fuzzywuzzy import fuzz
import datetime
from num2words import num2words
import webbrowser
import random
import keyboard
import winsound
import subprocess
import psutil
import mouse



winsound.PlaySound('d11.mp3', winsound.SND_FILENAME)
def va_respond(voice: str):
    print(voice)
    if voice.startswith(config.VA_ALIAS):
        # обращаются к ассистенту
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.VA_CMD_LIST.keys():
#            winsound.PlaySound('d1.mp3', winsound.SND_FILENAME)
            winsound.PlaySound('d2.mp3', winsound.SND_FILENAME)
        else:
            execute_cmd(cmd['cmd'])




def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    for x in config.VA_TBR:
        cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.VA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc


def execute_cmd(cmd: str):

    if cmd == 'myname':
        winsound.PlaySound('d13.mp3', winsound.SND_FILENAME)


    elif cmd == 'ctime':
        # current time
        now = datetime.datetime.now()
        text = "Қазір сагат " + num2words(now.hour, lang='kz') + " ден  " + num2words(now.minute, lang='kz') + "кетті"
        tts.va_speak(text)

    elif cmd == 'joke':
        jokes = [#winsound.PlaySound('d7.mp3', winsound.SND_FILENAME),
                 #winsound.PlaySound('d9.mp3', winsound.SND_FILENAME),
                 #winsound.PlaySound('d10.mp3', winsound.SND_FILENAME),
                 winsound.PlaySound('d8.mp3', winsound.SND_FILENAME)]
        random.choice(jokes)

    elif cmd == 'open_browser':
        winsound.PlaySound('d6.mp3', winsound.SND_FILENAME)
        subprocess.call("C:/Program Files/Google/Chrome/Application/chrome.exe")

    elif cmd == 'open_youtube':
        winsound.PlaySound('ok1.wav', winsound.SND_FILENAME)
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open('https://www.youtube.com/')

    elif cmd == 'muz':
        winsound.PlaySound('ok1.wav', winsound.SND_FILENAME)
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open('https://www.youtube.com/')

    elif cmd == 'open_prez':
        winsound.PlaySound('d6.mp3', winsound.SND_FILENAME)
        os.startfile("C:\\Users\\Nur\\dam\\Jarvis 2.0\\1.pptx")

    elif cmd == 'f5':
        winsound.PlaySound('ok1.wav', winsound.SND_FILENAME)
        keyboard.send("F5")

    elif cmd == 'klav':
        winsound.PlaySound('ok1.wav', winsound.SND_FILENAME)
        keyboard.send("Page Down")

    elif cmd == 'off':
        winsound.PlaySound('d4.mp3', winsound.SND_FILENAME)
        pid = psutil.Process().pid
        process = psutil.Process(pid)
        process.terminate()

    elif cmd == 'game':
        winsound.PlaySound('game.wav', winsound.SND_FILENAME)
        subprocess.call("C:\Program Files (x86)\Left 4 Dead 2\left4dead2.exe")


    elif cmd == 'klav2':
        winsound.PlaySound('ok1.wav', winsound.SND_FILENAME)
        keyboard.send("Page UP")

    elif cmd == 'nice':
        winsound.PlaySound('d3.mp3', winsound.SND_FILENAME)

    elif cmd == 'enter':
        winsound.PlaySound('ok1.wav', winsound.SND_FILENAME)
        keyboard.send("Enter")

    elif cmd == 'stop':
        winsound.PlaySound('ok1.wav', winsound.SND_FILENAME)
        keyboard.send("K")

    elif cmd == 'L':
        winsound.PlaySound('ok1.wav', winsound.SND_FILENAME)
        keyboard.send("L")

    elif cmd == 'J':
        winsound.PlaySound('ok1.wav', winsound.SND_FILENAME)
        keyboard.send("J")

    elif cmd == 'F':
        winsound.PlaySound('ok1.wav', winsound.SND_FILENAME)
        keyboard.send("F")

    elif cmd == 'M':
        winsound.PlaySound('ok1.wav', winsound.SND_FILENAME)
        keyboard.send("M")

    elif cmd == 'f4':
        winsound.PlaySound('ok1.wav', winsound.SND_FILENAME)
        keyboard.send("Alt+F4")

    elif cmd == 'left':
        winsound.PlaySound('ok1.wav', winsound.SND_FILENAME)
        mouse.click('left')

    elif cmd == 'tanday':
        winsound.PlaySound('ok1.wav', winsound.SND_FILENAME)
        mouse.move(886, 448)

# начать прослушивание команд
stt.va_listen(va_respond)