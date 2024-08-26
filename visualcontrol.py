import csv
import sys
import requests
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout, QFrame


class ModEntry(QWidget):
    def __init__(self, row_number, name, description, thumbnail_url, authors, downloads, web_url, parent=None):
        super(ModEntry, self).__init__(parent)

        # Load the thumbnail image from the URL and display it
        thumbnail_label = QLabel()
        pixmap = QPixmap()
        pixmap.loadFromData(requests.get(thumbnail_url).content)
        thumbnail_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))

        # Create labels for name, description, author, downloads, and web URL
        name_label = QLabel(name)
        description_label = QLabel(description)
        author_label = QLabel(f"Author(s): {authors}")
        download_label = QLabel(f"Downloads: {downloads}")
        web_url_label = QLabel(f"<a href='{web_url}'>Web URL</a>")

        # Set background color for each label (sub-boxes)
        thumbnail_label.setStyleSheet("background-color: white;")
        name_label.setStyleSheet("background-color: blue; color: white;")
        description_label.setStyleSheet("background-color: green; color: white;")
        author_label.setStyleSheet("background-color: lightblue;")
        download_label.setStyleSheet("background-color: lightgreen;")
        web_url_label.setStyleSheet("background-color: lightyellow;")

        # Allow links to be clickable and open in a web browser
        web_url_label.setTextFormat(Qt.RichText)
        web_url_label.setOpenExternalLinks(True)

        # Create layout for the author, downloads, and web URL (single box)
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(author_label)
        bottom_layout.addWidget(download_label)
        bottom_layout.addWidget(web_url_label)

        # Create layouts for stacking name and description
        text_layout = QVBoxLayout()
        text_layout.addWidget(name_label)
        text_layout.addWidget(description_label)
        text_layout.addLayout(bottom_layout)

        main_layout = QHBoxLayout()
        main_layout.addWidget(thumbnail_label)
        main_layout.addLayout(text_layout)

        # Set the layout for this widget
        self.setLayout(main_layout)

        # Set background color for the entire mod entry (main box)
        self.setStyleSheet("background-color: lightgray; border: 1px solid black;")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Intialize Window Settings
        self.init_ui()

    def init_ui(self):
        ''' Intialize the main UI settings'''
        self.setWindowTitle('Shell Forge')
        self.setWindowIcon(QIcon('Shellforgeicon.jpg'))

        self.resize(2000, 1500)
        self.center_window()


        # Create Scroll area and loadcontent
        self.create_scroll_area()
        self.populate_mod_data()

    def create_scroll_area(self):
        ''' Create the scroll area '''
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)        # Create a layout for the central widget

        # Scroll Area and content
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QFrame()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)
        #  self.scroll_content.setLayout(self.scroll_layout)

        # Add scroll area to the main layout
        self.layout.addWidget(self.scroll_area)

    def populate_mod_data(self):
        with open('data/mainmenu.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for index, row in enumerate(reader, start=1):
                row_number = str(index)
                name = row['Mod_Name']
                description = row['Description']
                thumbnail = row['Thumbnail_URL']
                webpage_URL = row['WebPage_URL']
                authors = row['Author_Name']
                downloads = row['Downloads']

                mod_entry = ModEntry(row_number, name, description, thumbnail, authors, downloads, webpage_URL, self)
                self.scroll_layout.addWidget(mod_entry)

    def center_window(self):
        # Get the geometry of the window
        window_geometry = self.frameGeometry()

        # Get the screen resolution
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        screen_geometry = QApplication.desktop().screenGeometry(screen)

        # Calculate the center point
        center_point = screen_geometry.center()

        # Move the window to the center point
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()



'''
TODO:
- Get images to visualize on windo 
- Favoritess


'''
