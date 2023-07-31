import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QGridLayout, \
    QWidget, QPushButton
from PyQt6.QtGui import QAction, QFont, QShortcut

from aboutdialog import AboutDialog
from calculate import Calculate

PLUS_OPERATOR = "+"
MINUS_OPERATOR = "-"
MULTIPLY_OPERATOR = "*"
DIVIDE_OPERATOR = "/"
EQUALS = "="
PERIOD = "."
NUMBER_DISPLAY_FONT = QFont("Times", 25)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.result = 0.0
        self.operator_pressed = False
        self.num_1 = ""
        self.num_2 = ""
        self.operator = ""

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
        self.number_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.number_display.setFont(NUMBER_DISPLAY_FONT)

        self.number_buttons = [self.create_number_button(str(i)) for i in range(10)]

        # Operator Buttons
        self.add_button = QPushButton(PLUS_OPERATOR, widget)
        self.subtract_button = QPushButton(MINUS_OPERATOR, widget)
        self.multiply_button = QPushButton(MULTIPLY_OPERATOR, widget)
        self.divide_button = QPushButton(DIVIDE_OPERATOR, widget)
        self.equal_button = QPushButton(EQUALS, widget)
        self.period_button = QPushButton(PERIOD, widget)
        self.clear_button = QPushButton("Clear", widget)

        # Connect Buttons
        self.period_button.clicked.connect(self.button_period)
        self.add_button.clicked.connect(lambda: self.operator_clicked(PLUS_OPERATOR))
        self.subtract_button.clicked.connect(lambda: self.operator_clicked(MINUS_OPERATOR))
        self.multiply_button.clicked.connect(lambda: self.operator_clicked(MULTIPLY_OPERATOR))
        self.divide_button.clicked.connect(lambda: self.operator_clicked(DIVIDE_OPERATOR))
        self.equal_button.clicked.connect(self.equal_clicked)
        self.clear_button.clicked.connect(self.clear_clicked)

        self.create_layout()

    def create_layout(self):
        layout = QGridLayout()

        layout.addWidget(self.number_display, 0, 0, 1, 4)  # Span the display label across 4 columns

        # Add number buttons
        row, col = 1, 0
        for i, button in enumerate(self.number_buttons):
            layout.addWidget(button, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1

            # Set shortcuts for each number button (main keyboard)
            shortcut = QShortcut(self)
            shortcut.setKey(str(i))
            shortcut.activated.connect(button.click)

            # Set shortcuts for each number button (numpad)
            numpad_shortcut = QShortcut(self)
            numpad_shortcut.setKey(f"NumPad{i}")
            numpad_shortcut.activated.connect(button.click)

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

        # Set shortcuts for operator buttons (numpad)
        numpad_add_shortcut = QShortcut(self)
        numpad_add_shortcut.setKey(Qt.Key.Key_Plus)
        numpad_add_shortcut.activated.connect(self.add_button.click)

        numpad_subtract_shortcut = QShortcut(self)
        numpad_subtract_shortcut.setKey(Qt.Key.Key_Minus)
        numpad_subtract_shortcut.activated.connect(self.subtract_button.click)

        numpad_multiply_shortcut = QShortcut(self)
        numpad_multiply_shortcut.setKey(Qt.Key.Key_Asterisk)
        numpad_multiply_shortcut.activated.connect(self.multiply_button.click)

        numpad_divide_shortcut = QShortcut(self)
        numpad_divide_shortcut.setKey(Qt.Key.Key_Slash)
        numpad_divide_shortcut.activated.connect(self.divide_button.click)

        numpad_equal_shortcut = QShortcut(self)
        numpad_equal_shortcut.setKey(Qt.Key.Key_Enter)
        numpad_equal_shortcut.activated.connect(self.equal_button.click)

        numpad_clear_shortcut = QShortcut(self)
        numpad_clear_shortcut.setKey(Qt.Key.Key_Backspace)
        numpad_clear_shortcut.activated.connect(self.clear_button.click)

        numpad_period_shortcut = QShortcut(self)
        numpad_period_shortcut.setKey(Qt.Key.Key_Period)
        numpad_period_shortcut.activated.connect(self.period_button.click)



    def about(self):
        """Show the About Dialog."""
        dialog = AboutDialog()
        dialog.exec()

    def create_number_button(self, num):
        """Create a number button with the given label."""
        button = QPushButton(str(num), self)
        button.clicked.connect(lambda: self.button_num_clicked(num))
        return button

    def button_num_clicked(self, num):
        """Handle number button clicks."""
        if not self.operator_pressed:
            self.num_1 = self.num_1 + str(num)
            self.number_display.setText(self.num_1)
        else:
            self.num_2 = self.num_2 + str(num)
            self.number_display.setText(self.num_2)
        self.number_display.update()

    def button_period(self):
        """Handle decimal point button click."""
        if not self.operator_pressed:
            self.num_1 = self.num_1 + "."
            self.number_display.setText(self.num_1)
            self.number_display.update()
        elif self.operator_pressed:
            self.num_2 = self.num_2 + "."
            self.number_display.setText(self.num_2)
            self.number_display.update()

    def operator_clicked(self, op):
        """Handle operator button clicks."""
        self.operator = op
        self.operator_pressed = True

    def equal_clicked(self):
        """Handle equal button click."""
        calc = Calculate(self.num_1, self.num_2, self.operator)
        result = calc.equals()
        self.number_display.setText(result)
        self.operator_pressed = False

    def clear_clicked(self):
        """Handle clear button click."""
        self.num_1 = ""
        self.num_2 = ""
        self.operator = ""
        self.operator_pressed = False
        self.result = 0.0
        self.number_display.setText(str(self.result))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
