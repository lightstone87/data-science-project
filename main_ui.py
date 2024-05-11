import sys
import os
import webbrowser

from PySide6.QtCore import Slot, QObject, QThread
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QQmlProperty

from source.py import main

# qml 파일 로드하기 위해 qml 파일 경로 전처리 과정 필요
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class WorkerThread(QThread):
    def __init__(self, parent, file_list, folder_path, file_type):
        super().__init__()
        self.parent = parent
        self.file_list = file_list
        self.folder_path = folder_path
        self.file_type = file_type

    def run(self):
        # 오래 걸리는 작업 수행
        # 1학년 전용
        if self.file_type == 0:
            for i in self.file_list:
                main.load_file_1st(self.parent, i, self.folder_path)
        
        # 오래 걸리는 작업 수행
        # 2~3학년 전용
        elif self.file_type == 1:
            for i in self.file_list:
                main.load_file(self.parent, i, self.folder_path)

        # 오래 걸리는 작업 수행
        # 수능 전용
        else:
            for i in self.file_list:
                main.load_file_sn(self.parent, i, self.folder_path)

class MainWindow(QQmlApplicationEngine):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.load(resource_path("./source/qml/main.qml"))
        self.rootContext().setContextProperty("MainWindow", self)
        self.window = self.rootObjects()[0]

        self.file_title_text = self.window.findChild(QObject, "file_title_text")
        self.file_title_name = QQmlProperty(self.file_title_text, "file_name")

        self.file_dialog = self.window.findChild(QObject, "file_dialog")
        self.file_dialog.selected_file_signal.connect(self.selected_file)

        self.convert_file_button = self.window.findChild(QObject, "convert_file_button")
        self.convert_file_button_text = QQmlProperty(self.convert_file_button, "button_text")
        self.convert_file_button.convert_file_signal.connect(self.convert_file)

        self.link_button = self.window.findChild(QObject, "link_button")
        self.link_button.link_button_signal.connect(self.link)
        
    @Slot()
    def selected_file(self, file_url):
        self.file_list = [i.toString() for i in file_url]
        self.file_list = [i.split("file:///")[1] for i in self.file_list]
        # file_name_list = [i.split("/")[-1] for i in file_list]

        file_count = len(self.file_list)
        if file_count == 1:
            self.file_title_name.write(self.file_list[0])
        else:
            self.file_title_name.write(f"{self.file_list[0]} 외 {file_count - 1}개")

        self.convert_file_button_text.write("파일 변환")


    @Slot()
    def convert_file(self, folder_path, file_type):
        folder_path = folder_path.split("file:///")[1]
        self.worker_thread = WorkerThread(self, self.file_list, folder_path, file_type)
        self.worker_thread.start()

    @Slot()
    def link(self):
        webbrowser.open_new("https://school.jbedu.kr/solnae")
        
if __name__ == '__main__':
    app = QGuiApplication(sys.argv)

    window = MainWindow(app)

    sys.exit(app.exec())