import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QLineEdit, QCheckBox, QGridLayout, QLabel)


class VisibilityControlWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 200)
        self.setWindowTitle('Widgets')

        # layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        grid = QGridLayout(central_widget)

        # widgets
        self.widgets = [
            QLabel("QLabel"),
            QLineEdit("QLineEdit"),
            QPushButton("QPushButton")
        ]

        # checkboxes
        for i, widget in enumerate(self.widgets):
            checkbox = QCheckBox(f"widget {i + 1} visible")
            checkbox.setChecked(True)
            checkbox.stateChanged.connect(self.toggle_visibility)

            # Сохраняем ссылку на виджет в свойстве чекбокса
            checkbox.setProperty("linked_widget", widget)

            # Добавляем в сетку: чекбокс в первый столбец, виджет во второй
            grid.addWidget(checkbox, i, 0)
            grid.addWidget(widget, i, 1)

    def toggle_visibility(self, state):
        checkbox = self.sender()
        widget = checkbox.property("linked_widget")

        if widget:
            widget.setVisible(checkbox.isChecked())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VisibilityControlWindow()
    ex.show()
    sys.exit(app.exec())