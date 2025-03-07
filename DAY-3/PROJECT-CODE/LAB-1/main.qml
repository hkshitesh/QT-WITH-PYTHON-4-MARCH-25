import QtQuick 6.0
import QtQuick.Controls 6.0

ApplicationWindow {
    visible: true
    width: 400
    height: 200
    title: "QML with Python"

    Column {
        anchors.centerIn: parent
        spacing: 10

        Text {
            id: label
            text: "Click the button!"
            font.pixelSize: 20
        }

        Button {
            text: "Click Me"
            onClicked: {
                label.text = "Button Clicked!"
                backend.processClick()  // Call Python function
            }
        }
    }
}
