from PySide6.QtWidgets import QWidget

class OffDelay555Widget(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("NE555 Switch-Off Delay")

class OnDelay555Widget(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("NE555 Switch-On Delay")