from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from repositories.folders import FolderRepository
from repositories.configs import ConfigRepository

class AddPastaWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.repository = FolderRepository()
        self.config_repository = ConfigRepository()

        layout = QVBoxLayout()

        # Path to Directory
        self.path_label = QLabel("Path to Directory:")
        self.path_input = QLineEdit()
        layout.addWidget(self.path_label)
        layout.addWidget(self.path_input)

        # Notion ID
        self.notion_id_label = QLabel("Notion ID:")
        self.notion_id_input = QLineEdit()
        layout.addWidget(self.notion_id_label)
        layout.addWidget(self.notion_id_input)

        # Save Button
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_data)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_data(self):
        path = self.path_input.text()
        notion_id = self.notion_id_input.text()
        config_id = self.config_repository.get_config_id()

        if not path or not notion_id:
            QMessageBox.warning(self, "Input Error", "All fields are required")
            return

        if not config_id:
            QMessageBox.warning(self, "Configuration Error", "Please set up configuration first")
            return
        
        self.repository.insert_folder(path, notion_id, config_id)

        QMessageBox.information(self, "Success", "Data saved successfully")