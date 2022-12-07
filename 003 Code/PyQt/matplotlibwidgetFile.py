from PyQt5.QtWidgets import*
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class matplotlibWidget(QWidget):

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        #fig = Figure(figsize=(5, 20))
        self.canvas = FigureCanvas()
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        plt.rc('font', size = 7)
        
        self.setLayout(vertical_layout)