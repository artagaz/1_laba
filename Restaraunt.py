import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QCheckBox, QSpinBox, QPlainTextEdit, QLabel


class RestaurantOrderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Restaurant')

        # layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Menu
        self.menu = [
            ("Burger", 500),
            ("Pasta", 600),
            ("Juice", 150),
            ("coffe", 321),
            ("candy", 59)
        ]

        # checkboxes + spinboxes
        self.dish_widgets = []
        for name, price in self.menu:
            dish_layout = QVBoxLayout()

            # name + price
            checkbox = QCheckBox(f"{name} - {price} руб.")
            checkbox.stateChanged.connect(self.update_order)

            # spinboxes
            spinbox = QSpinBox()
            spinbox.setRange(0, 50)
            spinbox.setValue(0)
            spinbox.valueChanged.connect(self.update_order)

            checkbox.spinbox = spinbox
            spinbox.checkbox = checkbox

            dish_layout.addWidget(checkbox)
            dish_layout.addWidget(spinbox)
            layout.addLayout(dish_layout)

            self.dish_widgets.append((checkbox, spinbox, price))

        self.bill = QPlainTextEdit()
        self.bill.setReadOnly(True)
        layout.addWidget(QLabel("Bill:"))
        layout.addWidget(self.bill)

    def update_order(self):
        bill_text = "You ordered:\n\n"
        total = 0

        for checkbox, spinbox, price in self.dish_widgets:
            if checkbox.isChecked():
                quantity = spinbox.value()
                if quantity == 0:
                    spinbox.setValue(1)
                    quantity = 1
                dish_total = price * quantity
                bill_text += f"{checkbox.text().split(" - ")[0]} x {quantity}: {dish_total} rub.\n"
                total += dish_total

        bill_text += f"\nTotal: {total} rub."
        self.bill.setPlainText(bill_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RestaurantOrderApp()
    ex.show()
    sys.exit(app.exec())
