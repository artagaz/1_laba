import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QGridLayout


class MorseCodeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Morse Code')

        # layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        grid = QGridLayout(central_widget)

        # out
        self.output_field = QLineEdit()
        self.output_field.setReadOnly(True)
        grid.addWidget(self.output_field, 0, 0, 1, 6)

        morse_code = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..'
        }

        # Создаем кнопки с буквами в цикле
        row, col = 1, 0
        for letter, code in morse_code.items():
            button = QPushButton(letter)
            button.clicked.connect(lambda checked, x=code: self.add_morse_code(x))
            button.setFixedSize(40, 30)
            grid.addWidget(button, row, col)

            # next row
            col += 1
            if col > 5:
                col = 0
                row += 1

    def add_morse_code(self, code):
        current_text = self.output_field.text()
        self.output_field.setText(current_text + " " + code if current_text else code)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MorseCodeWindow()
    ex.show()
    sys.exit(app.exec())
