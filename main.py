import sys

from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication, QLabel, QGridLayout, \
    QWidget, QPushButton
from PyQt6.QtGui import QAction

from aboutdialog import AboutDialog
from calculate import Calculate


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
        about_menu_action.triggered.connect(self.about)
        help_menu_item.addAction(about_menu_action)

        # Num Display
        self.number_display = QLabel(str(self.result))

        # Number Buttons
        num_0_button = QPushButton("0", widget)
        num_1_button = QPushButton("1", widget)
        num_2_button = QPushButton("2", widget)
        num_3_button = QPushButton("3", widget)
        num_4_button = QPushButton("4", widget)
        num_5_button = QPushButton("5", widget)
        num_6_button = QPushButton("6", widget)
        num_7_button = QPushButton("7", widget)
        num_8_button = QPushButton("8", widget)
        num_9_button = QPushButton("9", widget)
        # Operator Buttons
        add_button = QPushButton("+", widget)
        subtract_button = QPushButton("-", widget)
        multiply_button = QPushButton("*", widget)
        divide_button = QPushButton("/", widget)
        equal_button = QPushButton("=", widget)
        period_button = QPushButton(".", widget)
        clear_button = QPushButton("Clear", widget)

        # Connect Buttons
        num_0_button.clicked.connect(lambda: self.button_num_clicked(0))
        num_1_button.clicked.connect(lambda: self.button_num_clicked(1))
        num_2_button.clicked.connect(lambda: self.button_num_clicked(2))
        num_3_button.clicked.connect(lambda: self.button_num_clicked(3))
        num_4_button.clicked.connect(lambda: self.button_num_clicked(4))
        num_5_button.clicked.connect(lambda: self.button_num_clicked(5))
        num_6_button.clicked.connect(lambda: self.button_num_clicked(6))
        num_7_button.clicked.connect(lambda: self.button_num_clicked(7))
        num_8_button.clicked.connect(lambda: self.button_num_clicked(8))
        num_9_button.clicked.connect(lambda: self.button_num_clicked(9))
        period_button.clicked.connect(self.button_period)
        add_button.clicked.connect(lambda: self.operator_clicked("+"))
        subtract_button.clicked.connect(lambda: self.operator_clicked("-"))
        multiply_button.clicked.connect(lambda: self.operator_clicked("*"))
        divide_button.clicked.connect(lambda: self.operator_clicked("/"))
        equal_button.clicked.connect(self.equal_clicked)
        clear_button.clicked.connect(self.clear_clicked)

        # Set Layout (find a way to tidy this up at some point jesus)
        layout = QGridLayout()

        layout.addWidget(self.number_display, 0, 0)
        layout.addWidget(num_1_button, 1, 0)
        layout.addWidget(num_2_button, 1, 1)
        layout.addWidget(num_3_button, 1, 2)
        layout.addWidget(num_4_button, 2, 0)
        layout.addWidget(num_5_button, 2, 1)
        layout.addWidget(num_6_button, 2, 2)
        layout.addWidget(num_7_button, 3, 0)
        layout.addWidget(num_8_button, 3, 1)
        layout.addWidget(num_9_button, 3, 2)
        layout.addWidget(num_0_button, 4, 0)
        layout.addWidget(add_button, 1, 3)
        layout.addWidget(subtract_button, 2, 3)
        layout.addWidget(multiply_button, 3, 3)
        layout.addWidget(divide_button, 4, 3)
        layout.addWidget(period_button, 4, 1)
        layout.addWidget(equal_button, 4, 2)
        layout.addWidget(clear_button, 5, 0)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def about(self):
        dialog = AboutDialog()
        dialog.exec()

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
