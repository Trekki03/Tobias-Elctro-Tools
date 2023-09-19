import UIFiles.UI_VoltageDivider
from PySide6.QtWidgets import QWidget, QLineEdit
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QDoubleValidator

class VoltageDivider(QWidget):
    def __init__(self):
        super().__init__()
        self.uiVoltageDivider = UIFiles.UI_VoltageDivider.Ui_VoltageDivider()
        self.uiVoltageDivider.setupUi(self)
        self.uiVoltageDivider.btCalculateUd.clicked.connect(self.actionCalculateUd)
        self.uiVoltageDivider.btCalculateR2.clicked.connect(self.actionCalculateR2)

        self.uiVoltageDivider.leUdU.installEventFilter(self)
        self.uiVoltageDivider.leUdU.setValidator(QDoubleValidator().setNotation(QDoubleValidator.StandardNotation))
        self.uiVoltageDivider.leUdR1.installEventFilter(self)
        self.uiVoltageDivider.leUdR1.setValidator(QDoubleValidator().setNotation(QDoubleValidator.StandardNotation))
        self.uiVoltageDivider.leUdR2.installEventFilter(self)
        self.uiVoltageDivider.leUdR2.setValidator(QDoubleValidator().setNotation(QDoubleValidator.StandardNotation))
        self.uiVoltageDivider.leR2U.installEventFilter(self)
        self.uiVoltageDivider.leR2U.setValidator(QDoubleValidator().setNotation(QDoubleValidator.StandardNotation))
        self.uiVoltageDivider.leR2R1.installEventFilter(self)
        self.uiVoltageDivider.leR2R1.setValidator(QDoubleValidator().setNotation(QDoubleValidator.StandardNotation))
        self.uiVoltageDivider.leR2Ud.installEventFilter(self)
        self.uiVoltageDivider.leR2Ud.setValidator(QDoubleValidator().setNotation(QDoubleValidator.StandardNotation))
        self.show()

    def actionCalculateUd(self):
        u = float(self.uiVoltageDivider.leUdU.text())
        r1 = float(self.uiVoltageDivider.leUdR1.text())
        r2 = float(self.uiVoltageDivider.leUdR2.text())
        ud = round(u/(r1+r2)*r2, 3)
        self.uiVoltageDivider.lbUdUd.setText(str(ud))

    def actionCalculateR2(self):
        u = float(self.uiVoltageDivider.leR2U.text())
        r1 = float(self.uiVoltageDivider.leR2R1.text())
        ud = float(self.uiVoltageDivider.leR2Ud.text())
        r2 = round((ud*r1)/(u-ud), 3)
        self.uiVoltageDivider.lbR2R2.setText(str(r2))

    def eventFilter(self, source, event):
            if isinstance(source, QLineEdit) and event.type() == QEvent.MouseButtonPress:
                source.setFocus(Qt.MouseFocusReason)
                source.setCursorPosition(0)
                return True
            return super().eventFilter(source, event)