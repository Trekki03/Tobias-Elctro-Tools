from PySide6.QtWidgets import QMainWindow
from UIFiles.UI_MainWindow import Ui_MainWindow
import UIClasses.VoltageDivider

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        UIMainWindow = Ui_MainWindow()
        UIMainWindow.setupUi(self)
        UIMainWindow.btVoltageDivider.clicked.connect(self.actionVoltageDivider)
        UIMainWindow.btLoadedVoltageDivider.clicked.connect(self.actionLoadedVoltageDivider)
        UIMainWindow.btPassiveLowPassFilter.clicked.connect(self.actionPassiveLowPassFilter)
        UIMainWindow.btPassiveHighPassFilter.clicked.connect(self.actionPassiveHighPassFilter)
        UIMainWindow.bt555OnDelay.clicked.connect(self.action555OnDelay)
        UIMainWindow.bt555OffDelay.clicked.connect(self.action555OffDelay)
        UIMainWindow.btAmplifier.clicked.connect(self.actionAmplifier)
        UIMainWindow.btInvertedAmplifier.clicked.connect(self.actionInvertedAmplifier)
        UIMainWindow.btDifferenzialAmplifier.clicked.connect(self.actionDifferenzialAmplifier)
        self.setFixedSize(self.size())
        self.show()

    def actionVoltageDivider(self):
        self.window = UIClasses.VoltageDivider.VoltageDivider()

    def actionLoadedVoltageDivider(self):
        print("LoadedVoltage Divider Pressed")

    def actionPassiveLowPassFilter(self):
        print("Passive Low Pass Filter Pressed")

    def actionPassiveHighPassFilter(self):
        print("Passive High Pass Filter Pressed")

    def action555OnDelay(self):
        print("NE555 On Delay Pressed")

    def action555OffDelay(self):
        print("NE555 Off Delay Pressed")

    def actionAmplifier(self):
        print("Amplifier Pressed")

    def actionInvertedAmplifier(self):
        print("Inverted Amplifier Pressed")

    def actionDifferenzialAmplifier(self):
        print("Differnzial Amplifier Pressed")