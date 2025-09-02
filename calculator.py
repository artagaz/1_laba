import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QHBoxLayout


class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 900, 100)
        self.setWindowTitle('Calculator')

        # layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # input fields
        self.expression_input = QLineEdit('0', self)
        self.result_output = QLineEdit('0', self)
        self.result_output.setReadOnly(True)

        # button
        self.calc_btn = QPushButton('=', self)
        self.calc_btn.clicked.connect(self.calculate)

        # add widgets
        main_layout.addWidget(self.expression_input)
        main_layout.addWidget(self.calc_btn)
        main_layout.addWidget(self.result_output)

    def calculate(self):
        try:
            expression = self.expression_input.text()
            result = eval(expression)
            self.result_output.setText(str(result))
        except Exception as e:
            self.result_output.setText(f"Ошибка: {str(e)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalculatorWindow()
    ex.show()
    sys.exit(app.exec())