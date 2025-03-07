import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QStringListModel, QObject, Slot
from PySide6.QtQml import QQmlApplicationEngine


class Backend(QObject):
    def __init__(self):
        super().__init__()
        self._model = QStringListModel(["Item 1", "Item 2", "Item 3"])  # Initial list items

    @Slot()
    def addItem(self):
        """Adds a new item to the list."""
        current_items = self._model.stringList()
        current_items.append(f"Item {len(current_items) + 1}")
        self._model.setStringList(current_items)

    @Slot()
    def removeItem(self):
        """Removes the last item from the list."""
        current_items = self._model.stringList()
        if current_items:
            current_items.pop()
            self._model.setStringList(current_items)

    def get_model(self):
        """Expose the model to QML."""
        return self._model


def main():
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    backend = Backend()
    engine.rootContext().setContextProperty("backend", backend)
    engine.rootContext().setContextProperty("listModel", backend.get_model())  # Explicitly expose model

    engine.load("main.qml")
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
