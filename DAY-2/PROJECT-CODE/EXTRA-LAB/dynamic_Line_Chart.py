import sys
import pandas as pd
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QTimer
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import os

class LiveChartApp(QWidget):
    def __init__(self, excel_file):
        super().__init__()
        self.excel_file = excel_file

        self.setWindowTitle("Live Excel Line Chart Viewer")
        self.setGeometry(200, 200, 600, 500)

        # Layout setup
        self.layout = QVBoxLayout()

        # QLabel to display chart
        self.label = QLabel("Chart will appear here")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

        # Timer to refresh chart every 5 seconds
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_chart)
        self.timer.start(5000)  # 5 seconds interval

        self.update_chart()  # Initial chart display

    def update_chart(self):
        """ Reads Excel data and updates the chart """
        if not os.path.exists(self.excel_file):
            self.label.setText("Excel file not found!")
            return

        try:
            # Read Excel data
            df = pd.read_excel(self.excel_file)

            # Check for required columns
            if "Date" not in df.columns or "Sales ($)" not in df.columns:
                self.label.setText("Invalid Excel format! Ensure columns: Date, Sales ($)")
                return

            # Convert date column to datetime format
            df["Date"] = pd.to_datetime(df["Date"])

            # Generate line chart
            fig, ax = plt.subplots()
            ax.plot(df["Date"], df["Sales ($)"], marker="o", linestyle="-", color="b", label="Sales Trend")
            ax.set_xlabel("Date")
            ax.set_ylabel("Sales ($)")
            ax.set_title("Live Sales Over Time")
            ax.legend()
            ax.grid()

            # Save figure as image
            chart_path = "live_chart.png"
            fig.savefig(chart_path)
            plt.close(fig)

            # Display the chart in QLabel
            self.display_chart(chart_path)

        except Exception as e:
            self.label.setText(f"Error reading Excel: {e}")

    def display_chart(self, chart_path):
        pixmap = QPixmap(chart_path)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

if __name__ == "__main__":
    excel_file = "data.xlsx"  # Change this if using a different file

    app = QApplication(sys.argv)
    window = LiveChartApp(excel_file)
    window.show()
    sys.exit(app.exec())
