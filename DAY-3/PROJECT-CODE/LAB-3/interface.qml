import QtQuick 6.2
import QtQuick.Controls 6.2

ApplicationWindow {
    visible: true
    width: 400
    height: 200
    title: "Update Label from Python"

    Column {
        anchors.centerIn: parent
        spacing: 10

        Label {
            id: displayText
            objectName: "displayText"  // Important: Assign objectName for findChild()
            text: "Original Text"
            font.pixelSize: 16
        }

        Button {
            text: "Update Text"
            onClicked: backend.updateText()  // Call Python function
        }
    }
}
