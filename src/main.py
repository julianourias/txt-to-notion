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
        self.setWindowIcon(QIcon('_internal\\assets\\file.svg'))

        layout = QVBoxLayout() 
        self.tabs = QTabWidget()
        
        # Add config screen no a tab
        self.data_entry_widget = ConfigEntryWidget()
        self.tabs.addTab(self.data_entry_widget, "Configuração")
        
        # Add folder and file screen on the same tab
        combined_widget = QWidget()
        combined_layout = QVBoxLayout()
        
        self.add_pasta_widget = AddPastaWidget()
        self.notion_file_creator_widget = NotionFileCreatorWidget()
        
        combined_layout.addWidget(self.add_pasta_widget)
        combined_layout.addWidget(self.notion_file_creator_widget)
        combined_widget.setLayout(combined_layout)

        self.tabs.addTab(combined_widget, "Sincronização")

        layout.addWidget(self.tabs)
        self.setLayout(layout)

# Init PyQT6 application
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())