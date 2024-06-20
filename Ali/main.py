import os
import sys
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt
import config
import stt
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
import sympy as sp
import pyttsx3

# Initialize the TTS engine
tts_engine = pyttsx3.init()

# Define the response function
def va_respond(voice: str):
    print(voice)
    gui.update_output(f"You: {voice}")
    if voice.startswith(config.VA_ALIAS):
        cmd = recognize_cmd(filter_cmd(voice))
        if cmd['cmd'] not in config.VA_CMD_LIST.keys():
            winsound.PlaySound('d2.mp3', winsound.SND_FILENAME)
        else:
            execute_cmd(cmd['cmd'], voice)

# Filter the command from the voice input
def filter_cmd(raw_voice: str):
    cmd = raw_voice
    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()
    for x in config.VA_TBR:
        cmd = cmd.replace(x, "").strip()
    return cmd

# Recognize the command
def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.VA_CMD_LIST.items():
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt
    return rc

# Translate Kazakh words to mathematical symbols
def translate_kazakh_to_math(expression: str):
    translation_dict = {
        'бір': '1',
        'екі': '2',
        'үш': '3',
        'төрт': '4',
        'бес': '5',
        'алты': '6',
        'жеті': '7',
        'сегіз': '8',
        'тоғыз': '9',
        'нөл': '0',
        'қосу': '+',
        'алу': '-',
        'көбейту': '*',
        'бөлу': '/',
        'есепте': '',
        'тең': '='
    }
    for kazakh_word, math_symbol in translation_dict.items():
        expression = expression.replace(kazakh_word, math_symbol)
    return expression

# Execute the recognized command
def execute_cmd(cmd: str, voice: str):
    if cmd == 'myname':
        winsound.PlaySound('d13.mp3', winsound.SND_FILENAME)
    elif cmd == 'joke':
        jokes = ['d7.mp3', 'd9.mp3', 'd10.mp3', 'd8.mp3']
        joke = random.choice(jokes)
        winsound.PlaySound(joke, winsound.SND_FILENAME)
    elif cmd == 'open_browser':
        winsound.PlaySound('d6.mp3', winsound.SND_FILENAME)
        subprocess.call("C:/Program Files/Google/Chrome/Application/chrome.exe")
    elif cmd == 'open_youtube':
        winsound.PlaySound('ok1.wav', winsound.SND_FILENAME)
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open('https://www.youtube.com/')
    elif cmd == 'open_prez':
        winsound.PlaySound('d6.mp3', winsound.SND_FILENAME)
        os.startfile("C:\\Users\\NURS\\dd\\voice_assistant\\5.pptx")
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
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open('https://vseigru.net/igry-sabvej-serf/42068-igra-sabvej-serf-prizrachnyj-kapyushon.html')
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
        mouse.move(886, 458)
    elif cmd == 'move_left':
        keyboard.press_and_release('left')
    elif cmd == 'move_right':
        keyboard.press_and_release('right')
    elif cmd == 'jump':
        keyboard.press_and_release('up')
    elif cmd == 'roll':
        keyboard.press_and_release('down')
    elif cmd == 'muz':
        winsound.PlaySound('ok1.wav', winsound.SND_FILENAME)
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        music_links = [
            'https://www.youtube.com/watch?v=XCBi5kCbeNg',
            'https://www.youtube.com/watch?v=dRzG0Jq88Vc',
            'https://youtube.com/watch?v=jHhG_cli_OI',
            'https://www.youtube.com/watch?v=MafAZeag1_0'
        ]
        music_link = random.choice(music_links)
        webbrowser.get(chrome_path).open(music_link)
    elif cmd == 'math':
        try:
            expression = filter_cmd(voice)
            expression = translate_kazakh_to_math(expression)  # Translate Kazakh to math symbols
            result = sp.sympify(expression)
            gui.update_output(f"Result: {result}")
            winsound.PlaySound('d15.mp3', winsound.SND_FILENAME)
            tts_engine.say(f"{result}")  # Speak out the result
            tts_engine.runAndWait()
        except Exception as e:
            gui.update_output(f"Error: {str(e)}")
            winsound.PlaySound('16.mp3', winsound.SND_FILENAME)


class VoiceAssistantGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.start_listening()  # Automatically start listening when the GUI initializes

    def initUI(self):
        font = QFont('Arial', 12)
        font.setBold(True)
        self.setFont(font)

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.blue)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(palette)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Output label to display heard words
        self.output_label = QLabel('', self)
        self.layout.addWidget(self.output_label)

        # GPT button (as an example, it executes the 'nice' command)
        self.gpt_button = QPushButton('GPT', self)
        self.gpt_button.clicked.connect(lambda: execute_cmd('nice', ''))
        self.layout.addWidget(self.gpt_button)
        winsound.PlaySound('d11.mp3', winsound.SND_FILENAME)
        self.setGeometry(300, 300, 300, 500)
        self.setWindowTitle('Voice Assistant')
        self.show()

    def start_listening(self):
        # Start the STT listening in a new thread
        thread = threading.Thread(target=stt.va_listen, args=(va_respond,))
        thread.daemon = True
        thread.start()

    def update_output(self, text):
        self.output_label.setText(text)

# Initialize and run the application
def main():
    app = QApplication(sys.argv)
    global gui
    gui = VoiceAssistantGUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
