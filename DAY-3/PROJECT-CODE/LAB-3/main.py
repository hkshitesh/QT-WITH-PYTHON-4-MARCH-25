import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal


class Backend(QObject):
    """Handles UI interactions from QML."""

    textUpdated = Signal(str)  # Define a signal for updating the label

    def __init__(self, engine):
        super().__init__()
        self.engine = engine  # Store the engine reference

    @Slot()
    def updateText(self):
        """Updates the Label in QML using findChild()."""
        root_objects = self.engine.rootObjects()
        if not root_objects:
            print("Error: No root objects found!")
            return

        root = root_objects[0]  # Get the main QML object
        label = root.findChild(QObject, "displayText")  # Find Label by objectName

        if label:
            label.setProperty("text", "Text Updated from Python!")  # Update Label
        else:
            print("Error: displayText object not found!")


def main():
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    backend = Backend(engine)
    engine.rootContext().setContextProperty("backend", backend)  # Expose backend to QML

    qml_file = os.path.join(os.path.dirname(__file__), "interface.qml")
    engine.load(qml_file)  # Ensure the QML file loads correctly

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
