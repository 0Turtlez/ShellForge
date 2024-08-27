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
        thumbnail_label = self.populate_images(thumbnail_url)
        #thumbnail_label = self.populate_blank_images()
        # Create labels for name, description, author, downloads, and web URL
        name_label = QLabel(name)
        author_label = QLabel(f"Author(s): {authors}")
        description_label = QLabel(description)
        download_label = QLabel(f"Downloads: {downloads}")
        web_url_label = QLabel(f"<a href='{web_url}'>Web URL</a>")

        # Sets labels maximum / fixed sizes for thumbnail, title
        thumbnail_label.setFixedSize(100,100)
        name_label.setMaximumSize(200, 25)
        author_label.setMaximumSize(200, 25)
        description_label.setMaximumSize(750, 400)
        description_label.setWordWrap(True)

        # Set background color for each label (sub-boxes)
        self.set_label_colors(thumbnail_label,name_label, author_label, description_label, download_label, web_url_label)


        # Allow links to be clickable and open in a web browser
        web_url_label.setTextFormat(Qt.RichText)
        web_url_label.setOpenExternalLinks(True)

        # Create layout for the author, downloads, and web URL (single box)
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(web_url_label)
        bottom_layout.addWidget(download_label)

        # Create layouts for stacking name and description
        title_bar_layout = QHBoxLayout()
        title_bar_layout.addWidget(name_label)
        title_bar_layout.addWidget(author_label)
        title_bar_layout.setAlignment(Qt.AlignLeft)



        # Text Stack
        text_layout = QVBoxLayout()
        text_layout.addLayout(title_bar_layout)
        text_layout.addWidget(description_label)
        text_layout.addLayout(bottom_layout)

        main_layout = QHBoxLayout()
        main_layout.addWidget(thumbnail_label)
        main_layout.addSpacing(0)
        main_layout.addLayout(text_layout)

        # Set the layout for this widget
        self.setLayout(main_layout)

        # Set background color for the entire mod entry (main box)
        self.setStyleSheet("background-color: lightgray; border: 1px solid black;")

    def populate_images(self, thumbnail_url):
        thumbnail_label = QLabel()
        pixmap = QPixmap()
        pixmap.loadFromData(requests.get(thumbnail_url).content)
        thumbnail_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
        return thumbnail_label

    def populate_blank_images(self):
        thumbnail_label = QLabel()
        pixmap = QPixmap(100, 100)
        pixmap.fill(Qt.transparent)
        thumbnail_label.setPixmap(pixmap)
        return thumbnail_label

    def set_label_colors(self, thumbnail_label, name_label, author_label, description_label, download_label, web_url_label):
        thumbnail_label.setStyleSheet("background-color: white;")
        name_label.setStyleSheet("background-color: blue; color: white;")
        description_label.setStyleSheet("background-color: green; color: white;")
        author_label.setStyleSheet("background-color: lightblue;")
        download_label.setStyleSheet("background-color: lightgreen;")
        web_url_label.setStyleSheet("background-color: lightyellow;")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Intialize Window Settings
        self.init_ui()

    def init_ui(self):
        ''' Intialize the main UI settings'''
        self.setWindowTitle('Shell Forge')
        self.setWindowIcon(QIcon('Shellforgeicon.jpg'))

        self.resize(1000, 750)
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
- Get images to visualize on window
- Favoritess
- Image Caching
- Install from pre installed versions that have already been installed to save bandwidth / Space

Complete:
- Create a method that makes it easy to comment out image creation

'''