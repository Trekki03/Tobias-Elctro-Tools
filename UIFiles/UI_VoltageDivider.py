# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VoltageDivider.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import Resources_rc

class Ui_VoltageDivider(object):
    def setupUi(self, VoltageDivider):
        if not VoltageDivider.objectName():
            VoltageDivider.setObjectName(u"VoltageDivider")
        VoltageDivider.resize(750, 551)
        self.layoutWidget = QWidget(VoltageDivider)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 731, 531))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbSchemacticImage = QLabel(self.layoutWidget)
        self.lbSchemacticImage.setObjectName(u"lbSchemacticImage")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbSchemacticImage.sizePolicy().hasHeightForWidth())
        self.lbSchemacticImage.setSizePolicy(sizePolicy)
        self.lbSchemacticImage.setMinimumSize(QSize(500, 0))
        self.lbSchemacticImage.setMaximumSize(QSize(500, 300))
        self.lbSchemacticImage.setFrameShape(QFrame.Box)
        self.lbSchemacticImage.setLineWidth(2)
        self.lbSchemacticImage.setPixmap(QPixmap(u":/images/resources/images/VoltageDivider.png"))
        self.lbSchemacticImage.setScaledContents(True)

        self.verticalLayout.addWidget(self.lbSchemacticImage, 0, Qt.AlignHCenter)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(30, 0))
        self.label_3.setMaximumSize(QSize(150, 50))
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(30, 0))
        self.label_6.setMaximumSize(QSize(150, 50))
        self.label_6.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.lbUdUd = QLabel(self.layoutWidget)
        self.lbUdUd.setObjectName(u"lbUdUd")
        self.lbUdUd.setMinimumSize(QSize(100, 0))
        self.lbUdUd.setMaximumSize(QSize(150, 50))
        self.lbUdUd.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.lbUdUd, 1, 3, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(30, 0))
        self.label_7.setMaximumSize(QSize(150, 50))
        self.label_7.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_7, 2, 3, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(30, 0))
        self.label_4.setMaximumSize(QSize(150, 50))
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(30, 0))
        self.label.setMaximumSize(QSize(150, 50))
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(30, 0))
        self.label_2.setMaximumSize(QSize(150, 50))
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(30, 0))
        self.label_8.setMaximumSize(QSize(150, 50))
        self.label_8.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.lbR2R2 = QLabel(self.layoutWidget)
        self.lbR2R2.setObjectName(u"lbR2R2")
        self.lbR2R2.setMinimumSize(QSize(100, 0))
        self.lbR2R2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.lbR2R2, 3, 3, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(30, 0))
        self.label_10.setMaximumSize(QSize(150, 50))
        self.label_10.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.btCalculateUd = QPushButton(self.layoutWidget)
        self.btCalculateUd.setObjectName(u"btCalculateUd")

        self.gridLayout.addWidget(self.btCalculateUd, 1, 4, 1, 1)

        self.btCalculateR2 = QPushButton(self.layoutWidget)
        self.btCalculateR2.setObjectName(u"btCalculateR2")

        self.gridLayout.addWidget(self.btCalculateR2, 3, 4, 1, 1)

        self.leUdU = QLineEdit(self.layoutWidget)
        self.leUdU.setObjectName(u"leUdU")
        sizePolicy.setHeightForWidth(self.leUdU.sizePolicy().hasHeightForWidth())
        self.leUdU.setSizePolicy(sizePolicy)
        self.leUdU.setMinimumSize(QSize(20, 10))
        self.leUdU.setMaximumSize(QSize(150, 50))

        self.gridLayout.addWidget(self.leUdU, 1, 0, 1, 1)

        self.leUdR1 = QLineEdit(self.layoutWidget)
        self.leUdR1.setObjectName(u"leUdR1")
        sizePolicy.setHeightForWidth(self.leUdR1.sizePolicy().hasHeightForWidth())
        self.leUdR1.setSizePolicy(sizePolicy)
        self.leUdR1.setMinimumSize(QSize(20, 10))
        self.leUdR1.setMaximumSize(QSize(150, 50))

        self.gridLayout.addWidget(self.leUdR1, 1, 1, 1, 1)

        self.leUdR2 = QLineEdit(self.layoutWidget)
        self.leUdR2.setObjectName(u"leUdR2")
        sizePolicy.setHeightForWidth(self.leUdR2.sizePolicy().hasHeightForWidth())
        self.leUdR2.setSizePolicy(sizePolicy)
        self.leUdR2.setMinimumSize(QSize(20, 10))
        self.leUdR2.setMaximumSize(QSize(150, 50))

        self.gridLayout.addWidget(self.leUdR2, 1, 2, 1, 1)

        self.leR2U = QLineEdit(self.layoutWidget)
        self.leR2U.setObjectName(u"leR2U")
        sizePolicy.setHeightForWidth(self.leR2U.sizePolicy().hasHeightForWidth())
        self.leR2U.setSizePolicy(sizePolicy)
        self.leR2U.setMinimumSize(QSize(20, 10))
        self.leR2U.setMaximumSize(QSize(150, 50))

        self.gridLayout.addWidget(self.leR2U, 3, 0, 1, 1)

        self.leR2R1 = QLineEdit(self.layoutWidget)
        self.leR2R1.setObjectName(u"leR2R1")
        sizePolicy.setHeightForWidth(self.leR2R1.sizePolicy().hasHeightForWidth())
        self.leR2R1.setSizePolicy(sizePolicy)
        self.leR2R1.setMinimumSize(QSize(20, 10))
        self.leR2R1.setMaximumSize(QSize(150, 50))

        self.gridLayout.addWidget(self.leR2R1, 3, 1, 1, 1)

        self.leR2Ud = QLineEdit(self.layoutWidget)
        self.leR2Ud.setObjectName(u"leR2Ud")
        sizePolicy.setHeightForWidth(self.leR2Ud.sizePolicy().hasHeightForWidth())
        self.leR2Ud.setSizePolicy(sizePolicy)
        self.leR2Ud.setMinimumSize(QSize(20, 10))
        self.leR2Ud.setMaximumSize(QSize(150, 50))

        self.gridLayout.addWidget(self.leR2Ud, 3, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(VoltageDivider)

        QMetaObject.connectSlotsByName(VoltageDivider)
    # setupUi

    def retranslateUi(self, VoltageDivider):
        VoltageDivider.setWindowTitle(QCoreApplication.translate("VoltageDivider", u"Form", None))
        self.lbSchemacticImage.setText("")
        self.label_3.setText(QCoreApplication.translate("VoltageDivider", u"<html><head/><body><p><span style=\" font-weight:600;\">R2 [Ohm]</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("VoltageDivider", u"<html><head/><body><p><span style=\" font-weight:600;\">U_D [V]</span></p></body></html>", None))
        self.lbUdUd.setText("")
        self.label_7.setText(QCoreApplication.translate("VoltageDivider", u"<html><head/><body><p><span style=\" font-weight:600;\">R2 [Ohm]</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("VoltageDivider", u"<html><head/><body><p><span style=\" font-weight:600;\">U_D [V]</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("VoltageDivider", u"<html><head/><body><p><span style=\" font-weight:600;\">U [V]</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("VoltageDivider", u"<html><head/><body><p><span style=\" font-weight:600;\">R1 [Ohm]</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("VoltageDivider", u"<html><head/><body><p><span style=\" font-weight:600;\">R1 [Ohm]</span></p></body></html>", None))
        self.lbR2R2.setText("")
        self.label_10.setText(QCoreApplication.translate("VoltageDivider", u"<html><head/><body><p><span style=\" font-weight:600;\">U [V]</span></p></body></html>", None))
        self.btCalculateUd.setText(QCoreApplication.translate("VoltageDivider", u"Calculate U_D", None))
        self.btCalculateR2.setText(QCoreApplication.translate("VoltageDivider", u"Calculate R2", None))
        self.leUdU.setInputMask("")
        self.leUdU.setText("")
        self.leUdR1.setInputMask("")
        self.leUdR1.setText("")
        self.leUdR2.setInputMask("")
        self.leR2U.setInputMask("")
        self.leR2R1.setInputMask("")
        self.leR2Ud.setInputMask("")
    # retranslateUi

