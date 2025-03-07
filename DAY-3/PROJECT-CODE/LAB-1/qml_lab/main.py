import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal


class Backend(QObject):
    """Handles QML interactions and updates UI from Python."""
    responseText = Signal(str)

    @Slot(str)
    def processName(self, name):
        """Updates the UI text directly via Signal."""
        print(f"Received name: {name}")
        self.responseText.emit(f"Hello, {name}!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    backend = Backend()
    engine.rootContext().setContextProperty("backend", backend)  # Expose backend to QML

    engine.load("main.qml")
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
