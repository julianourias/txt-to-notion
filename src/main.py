import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget
from PyQt6.QtGui import QIcon

from screens.configs_screen import ConfigEntryWidget
from screens.folders_screen import AddPastaWidget
from screens.files_screen import NotionFileCreatorWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TXT to Notion")
        self.setGeometry(100, 100, 400, 300)
        
        # Set application icon
        self.setWindowIcon(QIcon('src\\assets\\file.svg'))

        layout = QVBoxLayout()

        self.tabs = QTabWidget()
        self.data_entry_widget = ConfigEntryWidget()
        self.add_pasta_widget = AddPastaWidget()
        self.notion_file_creator_widget = NotionFileCreatorWidget()

        self.tabs.addTab(self.data_entry_widget, "Configuração")
        combined_widget = QWidget()
        combined_layout = QVBoxLayout()
        combined_layout.addWidget(self.add_pasta_widget)
        combined_layout.addWidget(self.notion_file_creator_widget)
        combined_widget.setLayout(combined_layout)

        self.tabs.addTab(combined_widget, "Sincronização")

        layout.addWidget(self.tabs)
        self.setLayout(layout)

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())