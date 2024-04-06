import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.15
import QtQuick.Layouts 2.15
import Qt.labs.platform 1.0

ApplicationWindow {
    id: window
    objectName: "window"
    visible: true
    width: 600
    height: 500
    title: "성적표 처리 프로그램"
    
    Material.theme: Material.Dark
    Material.accent: Material.Orange
    // Material.foreground: Material.Grey
    // Material.primary: Material.Grey

    GridLayout {
        id: content_grid
        rows: 7
        columns: 2

        anchors.centerIn: parent
        
        columnSpacing: 20
        rowSpacing: 40
        Text {
            id: file_help_text
            text: qsTr("아래 버튼을 클릭하여 성적표 PDF 파일을 선택하세요.")
            color: Material.color(Material.Orange)
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter

            Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
        }

        Button {
            id: select_file_button
            objectName: "select_file_button"

            text: qsTr("파일 찾기")
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
            text: qsTr("아래 버튼을 클릭하여 성적표 종류를 선택하세요.")
            color: Material.color(Material.Orange)
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
                text: qsTr("기본")
                Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
                onToggled: {
                    file_type_layout.checked_type = 0
                }
            }
            RadioButton {
                text: qsTr("수능")
                Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
                onToggled: {
                    file_type_layout.checked_type = 1
                }
            }
        }
        Image {
            source: "file:///C:/Users/skfmj/Desktop/work_space/pdf_to_xlsx/전주솔내고 마크.jpg"
        }
        Button {
            id: convert_file_button
            objectName: "convert_file_button"

            property string button_text: "파일 변환"
            signal convert_file_signal(string file_path, string forlder_path, var file_type_layout)
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
        Text {
            color: Material.color(Material.Orange)
            font.pointSize: 24
            text: "전주솔내고등학교"
        }
    }
    FileDialog {
        id: file_dialog
        objectName: "file_dialog"

        signal selected_file_signal(string str)
        title: "파일 선택"
        // folder: StandardPaths.writableLocation(StandardPaths.Desktop)
        nameFilters: ["PDF 파일 (*.pdf)"]
        onAccepted: {
            // 파일이 선택되었을 때 처리할 로직 추가 가능
            selected_file_signal(file)
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
            convert_file_button.convert_file_signal(file_title_text.file_name, folder, file_type_layout.checked_type) 
        }
    }
}