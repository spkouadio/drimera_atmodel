"""import sys

import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import numpy as np  # Importing numpy just for generating a sample image
from six import BytesIO


# Step 1: Create matplotlib figure and plot image
def generate_sample_image():
    # Replace this with your own image data or loading mechanism
    # For this example, I'm generating a sample image using numpy
    width, height = 400, 300
    image_data = np.random.rand(height, width)  # Sample random grayscale image
    return image_data

image_data = generate_sample_image()
plt.imshow(image_data, cmap='gray')  # You can set the colormap to your preference
plt.axis('off')  # Turn off axis for a cleaner display

# Step 2: Convert matplotlib figure to QPixmap
def fig_to_pixmap(fig):
    # Save the figure to a buffer
    buf = BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', pad_inches=0, transparent=True)
    buf.seek(0)

    # Convert the buffer to QPixmap
    pixmap = QPixmap()
    pixmap.loadFromData(buf.read())
    buf.close()

    return pixmap

# Step 3: Create QGraphicsScene and QGraphicsView to display the image
app = QApplication(sys.argv)
scene = QGraphicsScene()
view = QGraphicsView(scene)

# Convert the matplotlib figure to QPixmap
figure_pixmap = fig_to_pixmap(plt.gcf())

# Create a QGraphicsPixmapItem to display the image
pixmap_item = scene.addPixmap(figure_pixmap)

# Fit the image to the view and center it
view.setSceneRect(0, 0, figure_pixmap.width(), figure_pixmap.height())
view.setAlignment(Qt.AlignCenter)

# Show the QGraphicsView
view.show()

# Start the application event loop
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QProgressBar, QApplication,
                             QVBoxLayout, QHBoxLayout, QLabel, QFileDialog)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, pyqtSignal, QSettings, QStandardPaths

import requests
import subprocess


################################################


################################################
class Downloader(QWidget):
    def __init__(self, *args, **kwargs):
        super(Downloader, self).__init__(*args, **kwargs)

        self.settings = QSettings("MyDownloader", "MyDownloader")
        self.setWindowTitle("Downloader")

        self.setWindowIcon(QIcon.fromTheme("download"))
        layout = QVBoxLayout(self)
        hlayout = QHBoxLayout()

        self.dpath = ""
        print(self.dpath)
        self.readSettings()
        self.url = ""
        self.fname = ""

        self.setFixedSize(600, 170)

        # Download Button
        self.pushButton = QPushButton(self, maximumWidth=100)
        self.pushButton.setToolTip('<b>Download</b>')
        self.pushButton.setText("Download")
        self.pushButton.setIcon(QIcon.fromTheme("download"))
        hlayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

        # Cancel Button
        self.cancelButton = QPushButton(self, maximumWidth=100)
        self.cancelButton.setText("Cancel")
        self.cancelButton.setIcon(QIcon.fromTheme("cancel"))
        hlayout.addWidget(self.cancelButton)
        self.cancelButton.setEnabled(False)
        self.cancelButton.clicked.connect(self.on_cancelButton_clicked)

        # Settings Button
        self.settingsButton = QPushButton(self, maximumWidth=32)
        self.settingsButton.setToolTip("choose Download Folder")
        self.settingsButton.setIcon(QIcon.fromTheme("folder"))
        hlayout.addWidget(self.settingsButton)
        self.settingsButton.clicked.connect(self.on_settingsButton_clicked)

        # Space to align Buttons left
        empty = QWidget()
        hlayout.addWidget(empty)

        # Bar
        self.progressBar = QProgressBar(self, minimumWidth=300)
        self.progressBar.setFixedHeight(14)
        self.progressBar.setValue(0)
        self.progressBar.hide()

        # Url Field
        self.urlfield = QLineEdit()
        self.urlfield.setPlaceholderText("URL")
        self.urlfield.textChanged.connect(self.extractFilename)
        layout.addWidget(self.urlfield)

        # Name Field
        self.namefield = QLineEdit()
        self.namefield.setPlaceholderText("Filename")
        layout.addWidget(self.namefield)

        layout.addWidget(self.progressBar)

        # StatusBar
        self.lbl = QLabel("status")
        layout.addLayout(hlayout)
        layout.addWidget(self.lbl)

        self.lbl.setText(f"Ready - Download Path: {self.dpath}")

        self.clip = QApplication.clipboard()
        if self.clip.text().startswith("http"):
            self.urlfield.setText(self.clip.text())

    def on_settingsButton_clicked(self):
        path = QFileDialog.getExistingDirectory(self, "Select Folder", self.dpath)
        if path:
            self.dpath = path
            self.settings.setValue("folder", self.dpath)
            self.lbl.setText(f"changed Download Path to: {self.dpath}")
        else:
            return

    def writeSettings(self):
        self.settings.setValue("folder", self.dpath)

    def readSettings(self):
        if self.settings.contains("folder"):
            self.dpath = self.settings.value("folder")
        else:
            self.dpath = QStandardPaths.standardLocations(QStandardPaths.MoviesLocation)[0]

    def extractFilename(self):
        t = self.urlfield.text().split('/')[-1]
        self.namefield.setText(f"{self.dpath}/{t}")

    def on_pushButton_clicked(self):
        if self.urlfield.text().startswith("http") or self.urlfield.text().startswith("ftp"):
            the_url = self.urlfield.text()
            the_filesize = requests.get(the_url, stream=True).headers['Content-Length']
            the_filepath = self.namefield.text()
            the_fileobj = open(the_filepath, 'wb')
            #### Create a download thread
            self.downloadThread = downloadThread(the_url, the_filesize, the_fileobj, buffer=10240)
            self.downloadThread.download_proess_signal.connect(self.set_progressbar_value)
            self.downloadThread.start()
            self.lbl.setText("Download started ...")
            self.progressBar.show()
            self.cancelButton.setEnabled(True)

    # Setting progress bar
    def set_progressbar_value(self, value):
        self.progressBar.setValue(value)
        if value == 100:
            self.lbl.setText("Download success!")
            self.sendMessage()
            self.progressBar.hide()

    def on_cancelButton_clicked(self):
        self.downloadThread.terminate()
        self.lbl.setText("Download cancelled")
        self.cancelButton.setEnabled(False)

    def sendMessage(self):
        title = 'Downloader'
        message = 'Download success!'
        icon = "info"
        timeout = 5000
        msg = ["notify-send", "-i", icon, title, message, '-t', str(timeout)]
        subprocess.Popen(msg)


##################################################################
# Download thread
##################################################################
class downloadThread(QThread):
    download_proess_signal = pyqtSignal(int)  # Create signal

    def __init__(self, url, filesize, fileobj, buffer):
        super(downloadThread, self).__init__()
        self.url = url
        self.filesize = filesize
        self.fileobj = fileobj
        self.buffer = buffer

    def run(self):
        try:
            rsp = requests.get(self.url, stream=True)  # Streaming download mode
            offset = 0
            for chunk in rsp.iter_content(chunk_size=self.buffer):
                if not chunk: break
                self.fileobj.seek(offset)  # Setting Pointer Position
                self.fileobj.write(chunk)  # write file
                offset = offset + len(chunk)
                proess = offset / int(self.filesize) * 100
                self.download_proess_signal.emit(int(proess))  # Sending signal
            #######################################################################
            self.fileobj.close()  # Close file
            self.exit(0)  # Close thread


        except Exception as e:
            print(e)


####################################
# Program entry
####################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Downloader()
    w.show()
    sys.exit(app.exec_())