from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox
from PySide6.QtCore import Qt
from consts import VERSION
from calculators.voltageDivider import VoltageDividerWidget, LoadedVoltageDividerWidget
from calculators.passiveFilter import PassiveHighPassFilterWidget, PassiveLowPassFilterWidget
from calculators.ne555 import OffDelay555Widget, OnDelay555Widget
from calculators.opamp import AmplifierWidget, InvertedAmplifierWidget
from calculators.transitor import DiffernzialAmplifierWidget

class MainWindow(QMainWindow):
    
    def __init__(self, app):

        super().__init__()
        self.app = app
        self.setWindowTitle("ElectroTools")

        # Menu Bar
        menuBar = self.menuBar()

        # Menus
        fileMenu = menuBar.addMenu("File")
        helpMenu = menuBar.addMenu("Help")

        # File Menu Actions
        quit_action = fileMenu.addAction("Quit")
        quit_action.triggered.connect(self.ma_quit_app)

        # Help Menu Actions
        version_action = helpMenu.addAction("Version")
        version_action.triggered.connect(self.ma_show_version)

        # Labels
        lb_resistors = QLabel("<b>Voltage Dividers and Filters<b>")
        lb_ics = QLabel("<b>ICs<B>")
        lb_opamps = QLabel("<b>OpAmps<b>")
        lb_transistors = QLabel("<b>Transitors<b>")

        # Buttons
        bt_voltageDivider = QPushButton("Voltage Divider")
        bt_voltageDivider.clicked.connect(self.ba_voltageDivider)
        bt_loadedVoltageDivider = QPushButton("Loaded Voltage Divider")
        bt_loadedVoltageDivider.clicked.connect(self.ba_loadedVoltageDivider)
        bt_passivLowPassFilter = QPushButton("Passive Low Pass Filter")
        bt_passivLowPassFilter.clicked.connect(self.ba_passivLowPassFilter)
        bt_passivHighPassFilter = QPushButton("Passive High Pass Filter")
        bt_passivHighPassFilter.clicked.connect(self.ba_passivLowPassFilter)

        bt_555offDelay = QPushButton("Switch-Off Delay (NE555 Timer)")
        bt_555offDelay.clicked.connect(self.ba_555offDelay)
        bt_555onDelay = QPushButton("Switch-On Delay (NE555 Timer)")
        bt_555onDelay.clicked.connect(self.ba_555onDelay)

        bt_amplifier = QPushButton("Amplifier")
        bt_amplifier.clicked.connect(self.ba_amplifier)
        bt_invertAmplifier = QPushButton("Inverted Amplifier")
        bt_invertAmplifier.clicked.connect(self.ba_invertAmplifier)

        bt_differenzialAmplifier = QPushButton("Differnzial Amplifier")
        bt_differenzialAmplifier.clicked.connect(self.ba_differenzialAmplifier)



        #Content
        mainWidget = QWidget()

        #Layout
        layout_main = QHBoxLayout()
        layout_resitor = QVBoxLayout()
        layout_resitor.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout_ic = QVBoxLayout()
        layout_ic.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout_opAmp = QVBoxLayout()
        layout_opAmp.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout_transitor = QVBoxLayout()
        layout_transitor.setAlignment(Qt.AlignmentFlag.AlignTop)

        layout_main.insertLayout(0, layout_resitor)
        layout_main.insertLayout(1, layout_ic)
        layout_main.insertLayout(2, layout_opAmp)
        layout_main.insertLayout(3, layout_transitor)

        # resitorLayout
        layout_resitor.addWidget(lb_resistors)
        layout_resitor.addWidget(bt_voltageDivider)
        layout_resitor.addWidget(bt_loadedVoltageDivider)
        layout_resitor.addWidget(bt_passivLowPassFilter)
        layout_resitor.addWidget(bt_passivHighPassFilter)

        #ic layout
        layout_ic.addWidget(lb_ics)
        layout_ic.addWidget(bt_555offDelay)
        layout_ic.addWidget(bt_555onDelay)

        #opamp layout
        layout_opAmp.addWidget(lb_opamps)
        layout_opAmp.addWidget(bt_amplifier)
        layout_opAmp.addWidget(bt_invertAmplifier)

        #transitor layout
        layout_transitor.addWidget(lb_transistors)
        layout_transitor.addWidget(bt_differenzialAmplifier)

        # Add Content
        mainWidget.setLayout(layout_main)
        self.setCentralWidget(mainWidget)


    # Menu Actions
    def ma_quit_app(self):
        self.app.quit()

    def ma_show_version(self):
        mb_version = QMessageBox()
        mb_version.setWindowTitle("Version")
        mb_version.setText("Tobias' Electro Tools - Version: " + VERSION)
        mb_version.setIcon(QMessageBox.Information)
        mb_version.setStandardButtons(QMessageBox.Ok)
        mb_version.exec()

    # Button Actions
    def ba_voltageDivider(self):
        self.widget = VoltageDividerWidget()
        self.widget.show()

    def ba_loadedVoltageDivider(self):
        self.widget = LoadedVoltageDividerWidget()
        self.widget.show()

    def ba_passivLowPassFilter(self):
        self.widget = PassiveLowPassFilterWidget()
        self.widget.show()

    def ba_passivHighPassFilter(self):
        self.widget = PassiveHighPassFilterWidget()
        self.widget.show()

    def ba_555offDelay(self):
        self.widget = OffDelay555Widget()
        self.widget.show()

    def ba_555onDelay(self):
        self.widget = OnDelay555Widget()
        self.widget.show()

    def ba_amplifier(self):
        self.widget = AmplifierWidget()
        self.widget.show()

    def ba_invertAmplifier(self):
        self.widget = InvertedAmplifierWidget()
        self.widget.show()

    def ba_differenzialAmplifier(self):
        self.widget = DiffernzialAmplifierWidget()
        self.widget.show()