from PySide6.QtCharts import QBarSet, QBarSeries, QChart, QChartView, QBarCategoryAxis
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class BarChartApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt Charts - Bar Chart Example")
        self.setGeometry(100, 100, 600, 400)

        # Create a bar set
        set0 = QBarSet("Category A")
        set0.append([10, 20, 30, 40, 50])  # Add values

        # Create a bar series and add the set
        series = QBarSeries()
        series.append(set0)

        # Create the chart
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Simple Bar Chart")

        # Set X-axis labels
        categories = ["Jan", "Feb", "Mar", "Apr", "May"]
        axisX = QBarCategoryAxis()
        axisX.append(categories)
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)

        # Display the chart
        chart_view = QChartView(chart)
        layout = QVBoxLayout()
        layout.addWidget(chart_view)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
