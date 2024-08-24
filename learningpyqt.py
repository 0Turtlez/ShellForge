import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ShellForge")
        self.setGeometry(1400, 600, 1000, 1000)
        self.setWindowIcon(QIcon('Shellforgeicon.jpg'))

        label = QLabel("Whereas disregard and contempt for human rights have resulted ")
        label.setFont(QFont("Arial", 48))
        label.setGeometry(0,0,500,100)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("background-color: rgb(255, 255, 0);")

        self.setCentralWidget(label)

def main():
    app = QApplication(sys.argv) # If the app will not be using command line args the pass in empty list []

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()







