from PySide6.QtWidgets import QApplication
from mainWindow import MainWindow
import sys

app = QApplication(sys.argv)

mainWindow = MainWindow(app)
mainWindow.show()

app.exec()