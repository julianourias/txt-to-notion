from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFileDialog

from repositories.folders import FolderRepository
from repositories.configs import ConfigRepository
from services.folders import FolderService

class AddPastaWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.repository = FolderRepository()
        self.service = FolderService()

        layout = QVBoxLayout()

        # Path to Directory
        self.path_label = QLabel("Path to Directory:")
        self.path_input = QLineEdit()
        layout.addWidget(self.path_label)
        layout.addWidget(self.path_input)

        # Button to open file explorer
        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.open_file_explorer)
        layout.addWidget(self.browse_button)
        
        # Save Button
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_data)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def open_file_explorer(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.path_input.setText(directory)

    def save_data(self):
        path = self.path_input.text()

        if not path:
            QMessageBox.warning(self, "Input Error", "Path are required")
            return

        row = self.repository.get_folder_by_path(path)
        if row:
            QMessageBox.warning(self, "Input Error", "Path already exists")
            return
        
        self.service.create_folder(path)

        QMessageBox.information(self, "Success", "Folder successfully added ")