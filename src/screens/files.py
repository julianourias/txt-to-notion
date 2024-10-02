
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QComboBox

from services.files import ServiceFile
from repositories.folders import FolderRepository

class NotionFileCreatorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.file_service = ServiceFile()
        self.folder_repository = FolderRepository()

        layout = QVBoxLayout()
        
        # Path Dropdown
        self.path_label = QLabel("Select Path:")
        self.path_dropdown = QComboBox()
        layout.addWidget(self.path_label)
        layout.addWidget(self.path_dropdown)

        # Create Files Button
        self.create_files_button = QPushButton("Create Files on Notion")
        self.create_files_button.clicked.connect(self.create_files)
        layout.addWidget(self.create_files_button)

        self.setLayout(layout)

        self.populate_path_dropdown()

    def populate_path_dropdown(self):
        paths = self.folder_repository.get_paths()
        for path in paths:
            self.path_dropdown.addItem(path[0])

    def create_files(self):
        selected_path = self.path_dropdown.currentText()

        try:
            self.file_service.create_files(selected_path)
            QMessageBox.information(self, "Success", f"Files created successfully on Notion")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to create files on Notion")