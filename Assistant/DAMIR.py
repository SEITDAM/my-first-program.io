import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QLabel,
    QScrollArea
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from openai import OpenAI

class ModernMessengerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setupOpenAI()

    def initUI(self):
        self.setWindowTitle('Көмекші бот')
        self.setGeometry(100, 100, 600, 800)
        self.layout = QVBoxLayout()

        self.message_area = QScrollArea()
        self.message_area.setWidgetResizable(True)
        self.message_widget = QWidget()
        self.message_layout = QVBoxLayout(self.message_widget)
        self.message_area.setWidget(self.message_widget)
        self.layout.addWidget(self.message_area)

        self.input_field = QLineEdit()
        self.input_field.setFont(QFont("Arial", 14))
        self.layout.addWidget(self.input_field)

        self.send_button = QPushButton('Жіберу')
        self.send_button.setFont(QFont("Arial", 16))
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

        self.setLayout(self.layout)

    def setupOpenAI(self):
        self.OPENAI_API_KEY = "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"
        self.client = OpenAI(api_key=self.OPENAI_API_KEY)

    def send_message(self):
        user_input = self.input_field.text()
        self.display_message("Сіз", user_input)
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": user_input}
            ]
        )
        message = completion.choices[0].message.content
        self.display_message("Көмекші", message)
        self.input_field.clear()

    def display_message(self, role, content):
        message_label = QLabel(f"[{role}]: {content}")
        message_label.setFont(QFont("Arial", 14))
        if role == "Сіз":
            message_label.setAlignment(Qt.AlignRight)
        else:
            message_label.setAlignment(Qt.AlignLeft)
        self.message_layout.addWidget(message_label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("QWidget { background-color: #1d2124; color: #4975f5; }")
    window = ModernMessengerApp()
    window.show()
    sys.exit(app.exec_())