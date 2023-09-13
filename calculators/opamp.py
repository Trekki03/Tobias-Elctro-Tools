from PySide6.QtWidgets import QWidget

class AmplifierWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Amplifier")

class InvertedAmplifierWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inverted Amplifier")