import UIClasses.MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

app = QApplication()
mainWindow = UIClasses.MainWindow.MainWindow()

app.exec()