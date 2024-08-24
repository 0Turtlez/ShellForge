import csv
import sys
import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QScrollArea, QFrame


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Intialize Window Settings
        self.init_ui()

    def init_ui(self):
        ''' Intialize the main UI settings'''
        self.setWindowTitle('Shell Forge')
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

                self.add_mod_info(
                    row_number,
                    name,
                    webpage_URL,
                    description,
                    thumbnail,
                    authors,
                    downloads,
                )
                print(row)

    def add_mod_info(self, row_number, name, link, description, thumbnail, authors, downloads):
        # Load the thumbnail image from the URL and display it
        thumbnail_label = QLabel()
        pixmap = QPixmap()
        pixmap.loadFromData(requests.get(thumbnail).content)
        thumbnail_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))

        labels = [
            QLabel(f"\n\n{row_number}."),
            #QLabel(f"<a href='{thumbnail}'>Mod Thumbnail Link"),
            QLabel(f"Mod Name: {name}"),
            QLabel(f"Mod Description: {description}"),
            QLabel(f"<a href='{link}'>Mod Link"),
            QLabel(f"Mod Author(s): {authors}"),
            QLabel(f"Mod Download Count: {downloads}\n\n"),
        ]

        # Add the image label first
        self.scroll_layout.addWidget(thumbnail_label)

        for label in labels:
            # Set the text format to allow for rich text (HTML)
            label.setTextFormat(Qt.RichText)
            # Allow links to be clickable and open in a web browser
            label.setOpenExternalLinks(True)
            # Add the label to the layout
            self.scroll_layout.addWidget(label)


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
        # Replace this with reading the csv





app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()



'''
TODO:
- Get images to visualize on windo 
- Favoritess


'''
