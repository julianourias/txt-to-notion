import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget

from screens.configs import ConfigEntryWidget
from screens.folders import AddPastaWidget
from screens.files import NotionFileCreatorWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Notion Data Manager")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.tabs = QTabWidget()
        self.data_entry_widget = ConfigEntryWidget()
        self.add_pasta_widget = AddPastaWidget()
        self.notion_file_creator_widget = NotionFileCreatorWidget()

        self.tabs.addTab(self.data_entry_widget, "Configuração")
        self.tabs.addTab(self.add_pasta_widget, "Pastas")
        self.tabs.addTab(self.notion_file_creator_widget, "Arquivos")

        layout.addWidget(self.tabs)
        self.setLayout(layout)

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())