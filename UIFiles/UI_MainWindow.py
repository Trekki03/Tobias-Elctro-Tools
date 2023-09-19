# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(580, 224)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionVersion = QAction(MainWindow)
        self.actionVersion.setObjectName(u"actionVersion")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbTitleResistor = QLabel(self.centralwidget)
        self.lbTitleResistor.setObjectName(u"lbTitleResistor")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbTitleResistor.sizePolicy().hasHeightForWidth())
        self.lbTitleResistor.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.lbTitleResistor)

        self.btVoltageDivider = QPushButton(self.centralwidget)
        self.btVoltageDivider.setObjectName(u"btVoltageDivider")
        sizePolicy1.setHeightForWidth(self.btVoltageDivider.sizePolicy().hasHeightForWidth())
        self.btVoltageDivider.setSizePolicy(sizePolicy1)
        self.btVoltageDivider.setMinimumSize(QSize(88, 34))

        self.verticalLayout.addWidget(self.btVoltageDivider)

        self.btLoadedVoltageDivider = QPushButton(self.centralwidget)
        self.btLoadedVoltageDivider.setObjectName(u"btLoadedVoltageDivider")
        sizePolicy1.setHeightForWidth(self.btLoadedVoltageDivider.sizePolicy().hasHeightForWidth())
        self.btLoadedVoltageDivider.setSizePolicy(sizePolicy1)
        self.btLoadedVoltageDivider.setMinimumSize(QSize(88, 34))

        self.verticalLayout.addWidget(self.btLoadedVoltageDivider)

        self.btPassiveLowPassFilter = QPushButton(self.centralwidget)
        self.btPassiveLowPassFilter.setObjectName(u"btPassiveLowPassFilter")
        sizePolicy1.setHeightForWidth(self.btPassiveLowPassFilter.sizePolicy().hasHeightForWidth())
        self.btPassiveLowPassFilter.setSizePolicy(sizePolicy1)
        self.btPassiveLowPassFilter.setMinimumSize(QSize(88, 34))

        self.verticalLayout.addWidget(self.btPassiveLowPassFilter)

        self.btPassiveHighPassFilter = QPushButton(self.centralwidget)
        self.btPassiveHighPassFilter.setObjectName(u"btPassiveHighPassFilter")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(100)
        sizePolicy2.setHeightForWidth(self.btPassiveHighPassFilter.sizePolicy().hasHeightForWidth())
        self.btPassiveHighPassFilter.setSizePolicy(sizePolicy2)
        self.btPassiveHighPassFilter.setMinimumSize(QSize(88, 34))

        self.verticalLayout.addWidget(self.btPassiveHighPassFilter, 0, Qt.AlignTop)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.lbTitleIc = QLabel(self.centralwidget)
        self.lbTitleIc.setObjectName(u"lbTitleIc")
        sizePolicy1.setHeightForWidth(self.lbTitleIc.sizePolicy().hasHeightForWidth())
        self.lbTitleIc.setSizePolicy(sizePolicy1)
        self.lbTitleIc.setMinimumSize(QSize(88, 18))
        self.lbTitleIc.setTextFormat(Qt.AutoText)
        self.lbTitleIc.setScaledContents(False)
        self.lbTitleIc.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.lbTitleIc, 0, Qt.AlignTop)

        self.bt555OnDelay = QPushButton(self.centralwidget)
        self.bt555OnDelay.setObjectName(u"bt555OnDelay")
        sizePolicy1.setHeightForWidth(self.bt555OnDelay.sizePolicy().hasHeightForWidth())
        self.bt555OnDelay.setSizePolicy(sizePolicy1)
        self.bt555OnDelay.setMinimumSize(QSize(88, 34))
        self.bt555OnDelay.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.bt555OnDelay, 0, Qt.AlignTop)

        self.bt555OffDelay = QPushButton(self.centralwidget)
        self.bt555OffDelay.setObjectName(u"bt555OffDelay")
        sizePolicy2.setHeightForWidth(self.bt555OffDelay.sizePolicy().hasHeightForWidth())
        self.bt555OffDelay.setSizePolicy(sizePolicy2)
        self.bt555OffDelay.setMinimumSize(QSize(88, 34))
        self.bt555OffDelay.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.bt555OffDelay, 0, Qt.AlignTop)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.lbTitleOpamp = QLabel(self.centralwidget)
        self.lbTitleOpamp.setObjectName(u"lbTitleOpamp")
        sizePolicy1.setHeightForWidth(self.lbTitleOpamp.sizePolicy().hasHeightForWidth())
        self.lbTitleOpamp.setSizePolicy(sizePolicy1)
        self.lbTitleOpamp.setMinimumSize(QSize(88, 18))

        self.verticalLayout_3.addWidget(self.lbTitleOpamp, 0, Qt.AlignTop)

        self.btAmplifier = QPushButton(self.centralwidget)
        self.btAmplifier.setObjectName(u"btAmplifier")
        sizePolicy1.setHeightForWidth(self.btAmplifier.sizePolicy().hasHeightForWidth())
        self.btAmplifier.setSizePolicy(sizePolicy1)
        self.btAmplifier.setMinimumSize(QSize(88, 34))

        self.verticalLayout_3.addWidget(self.btAmplifier, 0, Qt.AlignTop)

        self.btInvertedAmplifier = QPushButton(self.centralwidget)
        self.btInvertedAmplifier.setObjectName(u"btInvertedAmplifier")
        sizePolicy2.setHeightForWidth(self.btInvertedAmplifier.sizePolicy().hasHeightForWidth())
        self.btInvertedAmplifier.setSizePolicy(sizePolicy2)
        self.btInvertedAmplifier.setMinimumSize(QSize(88, 34))

        self.verticalLayout_3.addWidget(self.btInvertedAmplifier, 0, Qt.AlignTop)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.lbTitleTransitor = QLabel(self.centralwidget)
        self.lbTitleTransitor.setObjectName(u"lbTitleTransitor")
        sizePolicy1.setHeightForWidth(self.lbTitleTransitor.sizePolicy().hasHeightForWidth())
        self.lbTitleTransitor.setSizePolicy(sizePolicy1)
        self.lbTitleTransitor.setMinimumSize(QSize(88, 18))

        self.verticalLayout_4.addWidget(self.lbTitleTransitor)

        self.btDifferenzialAmplifier = QPushButton(self.centralwidget)
        self.btDifferenzialAmplifier.setObjectName(u"btDifferenzialAmplifier")
        sizePolicy2.setHeightForWidth(self.btDifferenzialAmplifier.sizePolicy().hasHeightForWidth())
        self.btDifferenzialAmplifier.setSizePolicy(sizePolicy2)
        self.btDifferenzialAmplifier.setMinimumSize(QSize(88, 34))

        self.verticalLayout_4.addWidget(self.btDifferenzialAmplifier, 0, Qt.AlignTop)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 580, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionVersion)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionVersion.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.lbTitleResistor.setText(QCoreApplication.translate("MainWindow", u"<b>Resistors<b>", None))
        self.btVoltageDivider.setText(QCoreApplication.translate("MainWindow", u"Voltage Divider", None))
        self.btLoadedVoltageDivider.setText(QCoreApplication.translate("MainWindow", u"Loaded Voltage Divider", None))
        self.btPassiveLowPassFilter.setText(QCoreApplication.translate("MainWindow", u"Passive Low-Pass Filter", None))
        self.btPassiveHighPassFilter.setText(QCoreApplication.translate("MainWindow", u"Passive High-Pass Filter", None))
        self.lbTitleIc.setText(QCoreApplication.translate("MainWindow", u"<b>ICs<b>", None))
        self.bt555OnDelay.setText(QCoreApplication.translate("MainWindow", u"NE555 On-Delay", None))
        self.bt555OffDelay.setText(QCoreApplication.translate("MainWindow", u"NE555 Off-Delay", None))
        self.lbTitleOpamp.setText(QCoreApplication.translate("MainWindow", u"<b>OpAmps<b>", None))
        self.btAmplifier.setText(QCoreApplication.translate("MainWindow", u"Amplifier", None))
        self.btInvertedAmplifier.setText(QCoreApplication.translate("MainWindow", u"Inverted Amplifier", None))
        self.lbTitleTransitor.setText(QCoreApplication.translate("MainWindow", u"<b>Transistors<b>", None))
        self.btDifferenzialAmplifier.setText(QCoreApplication.translate("MainWindow", u"Differenzial Amplifier", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

