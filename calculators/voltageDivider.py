from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class VoltageDividerWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voltage Divider")

class LoadedVoltageDividerWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Loaded Voltage Divider")