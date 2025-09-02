import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout


class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.reset_calculator()

    def initUI(self):
        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle('Calculator')

        # layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # display
        self.display = QLineEdit()
        self.display.setReadOnly(False)  # Разрешаем редактирование
        main_layout.addWidget(self.display)

        # buttons
        grid_layout = QGridLayout()
        main_layout.addLayout(grid_layout)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '±'
        ]

        positions = [(i, j) for i in range(5) for j in range(4)]
        for position, button_text in zip(positions, buttons):
            button = QPushButton(button_text)
            button.clicked.connect(lambda checked, text=button_text: self.on_button_click(text))
            grid_layout.addWidget(button, *position)

    def reset_calculator(self):
        self.current_input = ""
        self.waiting_for_operand = True
        self.display.setText("0")

    def on_button_click(self, text):
        if text in '0123456789':
            if self.waiting_for_operand:
                self.display.clear()
                self.waiting_for_operand = False
            self.display.setText(self.display.text() + text)

        elif text == '.':
            if self.waiting_for_operand:
                self.display.setText('0')
                self.waiting_for_operand = False
            if '.' not in self.display.text():
                self.display.setText(self.display.text() + '.')

        elif text == '±':
            current_text = self.display.text()
            if current_text.startswith('-'):
                self.display.setText(current_text[1:])
            else:
                self.display.setText('-' + current_text)

        elif text in '+-*/':
            if not self.waiting_for_operand:
                try:
                    result = str(eval(self.display.text()))
                    self.display.setText(result)
                except ZeroDivisionError:
                    self.display.setText("Ошибка: деление на ноль")
                    self.waiting_for_operand = True
                except:
                    self.display.setText("Ошибка")
                    return

            self.display.setText(self.display.text() + text)
            self.waiting_for_operand = False

        elif text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
                self.waiting_for_operand = True
            except ZeroDivisionError:
                self.display.setText("Ошибка: деление на ноль")
                self.waiting_for_operand = True
            except:
                self.display.setText("Ошибка")
                self.waiting_for_operand = True

        elif text == 'C':
            self.reset_calculator()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalculatorApp()
    ex.show()
    sys.exit(app.exec())
