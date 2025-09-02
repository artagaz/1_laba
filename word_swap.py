import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout


class word_swap(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 900, 200)
        self.setWindowTitle('word_swap')

        # layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # button
        self.btn = QPushButton('->', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 100)

        self.btn.clicked.connect(self.swap)

        # label
        self.left_input = QLineEdit('input_1', self)
        self.right_input = QLineEdit('input_2', self)

        # add widgets
        main_layout.addWidget(self.left_input)
        main_layout.addWidget(self.btn)
        main_layout.addWidget(self.right_input)

        self.transfer_direction = True

    # two-way
    # def swap(self):
    #     cache = self.left_input.text()
    #     self.left_input.setText(self.right_input.text())
    #     self.right_input.setText(cache)
    #     self.btn.setText('<-') if self.btn.text() == '->' else self.btn.setText('->')

    # one-way
    def swap(self):
        if self.transfer_direction:
            # Перенос из левого поля в правое
            self.right_input.setText(self.left_input.text())
            self.left_input.clear()
            self.btn.setText('<-')
        else:
            # Перенос из правого поля в левое
            self.left_input.setText(self.right_input.text())
            self.right_input.clear()
            self.btn.setText('->')

        # Меняем направление
        self.transfer_direction = not self.transfer_direction


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = word_swap()
    ex.show()
    sys.exit(app.exec())