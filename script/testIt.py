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
data = [
    [4, 9, 2],
    [1, 0, 0],
    [3, 5, 0],
    [3, 3, 2],
    [7, 8, 9],
]
print(type(data))