import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.15
import QtQuick.Layouts 2.15
import Qt.labs.platform
import QtQuick.Dialogs

ApplicationWindow {
    id: window
    objectName: "window"
    visible: true
    width: 800
    height: 550
    title: "성적표 처리 프로그램"
    
    Material.theme: Material.Dark
    Material.accent: Material.Orange
    // Material.foreground: Material.Grey
    // Material.primary: Material.Grey

    GridLayout {
        id: content_grid
        rows: 6
        columns: 1

        anchors.centerIn: parent
        
        columnSpacing: 20
        rowSpacing: 40
        Text {
            id: supertitle
            text: qsTr("고등학교 성적표 변환 프로그램")
            color: Material.color(Material.Orange)
            font.pixelSize: 45
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter

            Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
        }  

        Text {
            id: file_help_text
            text: qsTr("아래 버튼을 클릭하여 성적표 유형을 선택하세요.")
            color: Material.color(Material.Orange)
            font.pixelSize: 25
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter

            Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
            }

        RowLayout {
            id: file_type_layout
            objectName: "file_type_layout"

            property var checked_type: 0

            Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
            RadioButton {
                checked: true
                text: qsTr("1학년 학평")
                font.pixelSize: 15
                Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
                onToggled: {
                    file_type_layout.checked_type = 0
                }
            }
            RadioButton {
                text: qsTr("2~3학년 학평")
                font.pixelSize: 15
                Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
                onToggled: {
                    file_type_layout.checked_type = 1
                }
            }
            RadioButton {
                text: qsTr("3학년 모평 & 수능")
                font.pixelSize: 15
                Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
                onToggled: {
                    file_type_layout.checked_type = 2
                }
            }
        }

        Button {
            id: select_file_button
            objectName: "select_file_button"

            text: qsTr("파일 선택")
            Material.foreground: Material.Orange

            Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter

            MouseArea
            {
                id: select_file_button_area
                anchors.fill: parent
                cursorShape: Qt.PointingHandCursor

                onPressed: file_dialog.open()
            }
        }

        Text {
            id: file_title_text
            objectName: "file_title_text"

            property string file_name: "없음"
            text: qsTr("선택 파일 : "+ file_name)

            Layout.preferredWidth: 300
            elide: Text.ElideMiddle
            
            color: Material.color(Material.Orange)
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter

            Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
        }

        Text {
            id: file_type_text
            text: qsTr("아래 버튼을 클릭하여 저장 위치를 선택하세요.")
            font.pixelSize: 25
            color: Material.color(Material.Orange)
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter

            Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
        }

        
                
        Button {
            id: convert_file_button
            objectName: "convert_file_button"

            property string button_text: "파일 저장"
            signal convert_file_signal(string forlder_path, var file_type_layout)
            text: qsTr(button_text)
            Material.foreground: Material.Orange
            Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter

            MouseArea
            {
                id: convert_file_button_area
                anchors.fill: parent
                cursorShape: Qt.PointingHandCursor

                onPressed: {
                    if (file_title_text.file_name == "없음") { print("파일을 선택해주세요.") }
                    else { folder_dialog.open() }
                }
            }
        }
    }


    Rectangle {
        width: 100 // 여백을 포함한 실제 너비
        height: 100 // 여백을 포함한 실제 높이
        anchors.bottom: parent.bottom
        anchors.right: parent.right
        anchors.margins: 15
        color: "transparent"
        MouseArea{
            id: school_link
            objectName: "link_button"
            signal link_button_signal()
            anchors.fill: parent
            cursorShape: Qt.PointingHandCursor
            onPressed: {
                link_button_signal()
            }
        }
        GridLayout {
            id: sub_grid
            rows: 2
            columns: 1
            anchors.centerIn: parent
            Image {
                sourceSize.width: 100
                // sourceSize.height: 100
                Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
                source: "../img/profile.jpg"
            }
            Text {
                color: Material.color(Material.Orange)
                Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
                font.pointSize: 10
                text: "솔내고 송경석"
            }
        }
    }


    FileDialog {
        id: file_dialog
        objectName: "file_dialog"

        signal selected_file_signal(var lst)
        title: "파일 선택"

        // folder: StandardPaths.writableLocation(StandardPaths.Desktop)
        fileMode: FileDialog.OpenFiles
        nameFilters: ["PDF 파일 (*.pdf)"]
        onAccepted: {
            // 파일이 선택되었을 때 처리할 로직 추가 가능
            selected_file_signal(selectedFiles)
        }
    }

    FolderDialog {
        id: folder_dialog
        objectName: "folder_dialog"

        signal selected_dir_signal(string str)
        title: "폴더 선택"
        
        // folder: StandardPaths.writableLocation(StandardPaths.Desktop)

        onAccepted: {
            // 폴더가 선택되었을 때 처리할 로직 추가 가능
            convert_file_button.convert_file_signal(selectedFolder, file_type_layout.checked_type) 
        }
    }
}