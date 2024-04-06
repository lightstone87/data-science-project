import sys

from PySide6.QtCore import Slot, QObject, QThread
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QQmlProperty

from source.py import main

class WorkerThread(QThread):
    def __init__(self, parent, file_path, folder_path, file_type):
        super().__init__()
        self.parent = parent
        self.file_path = file_path
        self.folder_path = folder_path
        self.file_type = file_type

    def run(self):
        # 오래 걸리는 작업 수행
        if self.file_type == 0:
            main.load_file(self.parent, self.file_path, self.folder_path)
        else:
            main.load_file_sn(self.parent, self.file_path, self.folder_path)
            

class MainWindow(QQmlApplicationEngine):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.load("./source/qml/main.qml")
        self.rootContext().setContextProperty("MainWindow", self)
        self.window = self.rootObjects()[0]

        self.file_title_text = self.window.findChild(QObject, "file_title_text")
        self.file_title_name = QQmlProperty(self.file_title_text, "file_name")

        self.file_dialog = self.window.findChild(QObject, "file_dialog")
        self.file_dialog.selected_file_signal.connect(self.selected_file)

        self.convert_file_button = self.window.findChild(QObject, "convert_file_button")
        self.convert_file_button_text = QQmlProperty(self.convert_file_button, "button_text")
        self.convert_file_button.convert_file_signal.connect(self.convert_file)

    @Slot()
    def selected_file(self, file_url):
        file_path = file_url.split("file:///")[1]
        # file_name = file_url.split("/")[-1]
        self.file_title_name.write(file_path)
        self.convert_file_button_text.write("파일 변환")

    @Slot()
    def convert_file(self, file_path, folder_path, file_type):
        folder_path = folder_path.split("file:///")[1]
        self.worker_thread = WorkerThread(self, file_path, folder_path, file_type)
        self.worker_thread.start()

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)

    window = MainWindow(app)

    sys.exit(app.exec())
