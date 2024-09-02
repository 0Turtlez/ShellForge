import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ShellForge")
        self.setGeometry(1400, 600, 1000, 1000)
        self.setWindowIcon(QIcon('Shellforgeicon.jpg'))

        label = QLabel("Pizza", self)
        label.setFont(QFont("Arial", 48))
        label.setGeometry(0,0,1200,100)
        label.setStyleSheet("color: rgb(255, 0, 0);"
                            "background-color: rgb(255, 0, 255);"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;"
                            )
        # label.setAlignment(Qt.AlignTop) # Vertically Top
        # label.setAlignment(Qt.AlignBottom) # Vertically Bottom
        # label.setAlignment(Qt.AlignVCenter) # Vertically center

        # label.setAlignment(Qt.AlignRight) # Horizontally right
        label.setAlignment(Qt.AlignHCenter) # Horizontally center
        # label.setAlignment(Qt.AlignLeft) # Horizontally Left



def main():
    app = QApplication(sys.argv) # If the app will not be using command line args the pass in empty list []

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()







