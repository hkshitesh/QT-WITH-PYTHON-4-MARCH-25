import QtQuick 6.0
import QtQuick.Controls 6.0

ApplicationWindow {
    visible: true
    width: 400
    height: 250
    title: "QML-Python Integration"

    Column {
        anchors.centerIn: parent
        spacing: 10

        Text {
            id: label
            text: "Enter your name:"
            font.pixelSize: 18
        }

        TextField {
            id: nameInput
            width: 200
            placeholderText: "Type here..."
        }

        Button {
            text: "Submit"
            onClicked: {
                backend.processName(nameInput.text)  // Call Python function
            }
        }

        Label {
            id: responseText
            text: backend.responseText  // Direct binding
            font.pixelSize: 16
        }
    }
}
