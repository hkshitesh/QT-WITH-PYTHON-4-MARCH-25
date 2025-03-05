import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class LineChartApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Line Chart Example')

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a FigureCanvas to embed the Matplotlib plot
        self.canvas = FigureCanvas(Figure())
        layout.addWidget(self.canvas)

        self.draw_line_chart()  # Create and display the line chart

    def draw_line_chart(self):
        x = [1, 2, 3, 4, 5]
        y = [10, 15, 13, 17, 20]

        ax = self.canvas.figure.add_subplot(111)
        ax.plot(x, y, marker='o', linestyle='-')
        ax.set_xlabel('X-Axis')
        ax.set_ylabel('Y-Axis')
        ax.set_title('Line Chart Example')

        self.canvas.draw()
def run_app():
    app = QApplication(sys.argv)
    ex = LineChartApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run_app()
