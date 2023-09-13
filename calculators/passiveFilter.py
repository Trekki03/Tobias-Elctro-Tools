from PySide6.QtWidgets import QWidget

class PassiveHighPassFilterWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Passive High-Pass Filter")

class PassiveLowPassFilterWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Passive Low-Pass Filter")