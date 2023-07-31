from PyQt6.QtWidgets import QMessageBox


class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        content = """
        This app was created using python and PyQt6 as a portfolio project. Feel free
        to use this code or app in your own project.
        """
        self.setText(content)
