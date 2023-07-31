import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QGridLayout, \
    QWidget, QPushButton
from PyQt6.QtGui import QAction

from aboutdialog import AboutDialog
from calculate import Calculate


def about():
    dialog = AboutDialog()
    dialog.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.result = 0.0
        self.operator_pressed = False
        self.num_1 = ""
        self.num_2 = ""
        self.operator = ""
        print(type(self.result))

        self.setWindowTitle("Calculator")
        self.setMinimumSize(400, 400)
        widget = QWidget()

        # Menu Bar
        help_menu_item = self.menuBar().addMenu("&Help")

        # Menu Bar Items
        about_menu_action = QAction("About", self)
        about_menu_action.triggered.connect(about)
        help_menu_item.addAction(about_menu_action)

        # Num Display
        self.number_display = QLabel(str(self.result))

        self.number_buttons = [self.create_number_button(str(i)) for i in range(10)]

        # Operator Buttons
        self.add_button = QPushButton("+", widget)
        self.subtract_button = QPushButton("-", widget)
        self.multiply_button = QPushButton("*", widget)
        self.divide_button = QPushButton("/", widget)
        self.equal_button = QPushButton("=", widget)
        self.period_button = QPushButton(".", widget)
        self.clear_button = QPushButton("Clear", widget)

        # Connect Buttons
        self.period_button.clicked.connect(self.button_period)
        self.add_button.clicked.connect(lambda: self.operator_clicked("+"))
        self.subtract_button.clicked.connect(lambda: self.operator_clicked("-"))
        self.multiply_button.clicked.connect(lambda: self.operator_clicked("*"))
        self.divide_button.clicked.connect(lambda: self.operator_clicked("/"))
        self.equal_button.clicked.connect(self.equal_clicked)
        self.clear_button.clicked.connect(self.clear_clicked)

        self.create_layout()

    def create_layout(self):
        layout = QGridLayout()

        layout.addWidget(self.number_display, 0, 0, 1, 4)  # Span the display label across 4 columns

        # Add number buttons
        row, col = 1, 0
        for button in self.number_buttons:
            layout.addWidget(button, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1

        # Add operator buttons
        layout.addWidget(self.add_button, 1, 3)
        layout.addWidget(self.subtract_button, 2, 3)
        layout.addWidget(self.multiply_button, 3, 3)
        layout.addWidget(self.divide_button, 4, 3)
        layout.addWidget(self.period_button, 4, 1)
        layout.addWidget(self.equal_button, 4, 2)
        layout.addWidget(self.clear_button, 5, 0, 1, 4)  # Span the "Clear" button across 4 columns

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def create_number_button(self, num):
        button = QPushButton(str(num), self)
        button.clicked.connect(lambda: self.button_num_clicked(num))
        return button

    def button_num_clicked(self, number):
        if not self.operator_pressed:
            self.num_1 = self.num_1 + str(number)
            self.number_display.setText(self.num_1)
        else:
            self.num_2 = self.num_2 + str(number)
            self.number_display.setText(self.num_2)
        self.number_display.update()

    def button_period(self):
        if not self.operator_pressed:
            self.num_1 = self.num_1 + "."
            self.number_display.setText(self.num_1)
            self.number_display.update()
        elif self.operator_pressed:
            self.num_2 = self.num_2 + "."
            self.number_display.setText(self.num_2)
            self.number_display.update()

    def operator_clicked(self, op):
        self.operator = op
        self.operator_pressed = True

    def equal_clicked(self):
        calc = Calculate(self.num_1, self.num_2, self.operator)
        result = calc.equals()
        self.number_display.setText(result)
        self.operator_pressed = False

    def clear_clicked(self):
        self.num_1 = ""
        self.num_2 = ""
        self.operator = ""
        self.operator_pressed = False
        self.result = 0.0
        self.number_display.setText(str(self.result))


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())
