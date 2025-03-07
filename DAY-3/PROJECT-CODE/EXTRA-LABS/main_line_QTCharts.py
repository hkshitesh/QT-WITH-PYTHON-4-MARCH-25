import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtCore import QPointF


class LineChartApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt Charts - Line Chart Example")
        self.setGeometry(100, 100, 600, 400)

        # Create a line series and add data points
        series = QLineSeries()
        data_points = [(0, 5), (1, 15), (2, 25), (3, 20), (4, 30)]
        for x, y in data_points:
            series.append(QPointF(x, y))

        # Create a chart and add the series
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Simple Line Chart")
        chart.createDefaultAxes()  # Auto-create X and Y axes

        # Create a ChartView to display the chart
        chart_view = QChartView(chart)
        chart_view.setRenderHint(chart_view.renderHints())  # Enable smooth rendering

        # Set up the layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(chart_view)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LineChartApp()
    window.show()
    sys.exit(app.exec())
