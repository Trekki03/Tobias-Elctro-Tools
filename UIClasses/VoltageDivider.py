import UIFiles.UI_VoltageDivider
from PySide6.QtWidgets import QWidget, QLineEdit
from PySide6.QtCore import Qt, QEvent

class VoltageDivider(QWidget):
    def __init__(self):
        super().__init__()
        self.uiVoltageDivider = UIFiles.UI_VoltageDivider.Ui_VoltageDivider()
        self.uiVoltageDivider.setupUi(self)
        self.uiVoltageDivider.btCalculateUd.clicked.connect(self.actionCalculateUd)
        self.uiVoltageDivider.btCalculateR2.clicked.connect(self.actionCalculateR2)
        self.uiVoltageDivider.leUdU.installEventFilter(self)
        self.uiVoltageDivider.leUdR1.installEventFilter(self)
        self.uiVoltageDivider.leUdR2.installEventFilter(self)
        self.uiVoltageDivider.leR2U.installEventFilter(self)
        self.uiVoltageDivider.leR2R1.installEventFilter(self)
        self.uiVoltageDivider.leR2Ud.installEventFilter(self)
        self.show()

    def actionCalculateUd(self):
        u = int(self.uiVoltageDivider.leUdU.text())
        r1 = int(self.uiVoltageDivider.leUdR1.text())
        r2 = int(self.uiVoltageDivider.leUdR2.text())
        ud = u/(r1+r2)*r2
        self.uiVoltageDivider.lbUdUd.setText(str(ud))

    def actionCalculateR2(self):
        u = int(self.uiVoltageDivider.leR2U.text())
        r1 = int(self.uiVoltageDivider.leR2R1.text())
        ud = int(self.uiVoltageDivider.leR2Ud.text())
        r2 = (ud*r1)/(u-ud)
        self.uiVoltageDivider.lbR2R2.setText(str(r2))

    def eventFilter(self, source, event):
            if isinstance(source, QLineEdit) and event.type() == QEvent.MouseButtonPress:
                source.setFocus(Qt.MouseFocusReason)
                source.setCursorPosition(0)
                return True
            return super().eventFilter(source, event)