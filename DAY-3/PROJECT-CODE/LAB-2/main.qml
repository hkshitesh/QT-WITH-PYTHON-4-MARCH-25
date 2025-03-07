import QtQuick 6.2
import QtQuick.Controls 6.2

ApplicationWindow {
    visible: true
    width: 400
    height: 500
    title: "Dynamic ListView"

    Column {
        anchors.fill: parent
        spacing: 10
        padding: 10

        Button {
            text: "Add Item"
            onClicked: backend.addItem()
        }

        Button {
            text: "Remove Last Item"
            onClicked: backend.removeItem()
        }

        ListView {
            id: listView
            width: parent.width
            height: 400
            model: listModel  // Ensure correct model reference

            delegate: Rectangle {
                width: listView.width
                height: 50
                color: "lightblue"
                border.color: "black"

                Text {
                    anchors.centerIn: parent
                    text: model.display  // Correct reference to model data
                    font.pixelSize: 16
                }
            }
        }
    }
}
