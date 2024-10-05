
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QComboBox
import glob
import os

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
        
        # Refresh Paths Button
        self.refresh_paths_button = QPushButton("Refresh Paths")
        self.refresh_paths_button.clicked.connect(self.populate_path_dropdown)
        layout.addWidget(self.refresh_paths_button)

        # Create Files Button
        self.create_files_button = QPushButton("Create Files on Notion")
        self.create_files_button.clicked.connect(self.create_files)
        layout.addWidget(self.create_files_button)
        
        # Current File Label
        self.current_file_label = QLabel("|")
        layout.addWidget(self.current_file_label)

        self.setLayout(layout)

        self.populate_path_dropdown()

    def populate_path_dropdown(self):
        paths = self.folder_repository.get_paths()
        self.path_dropdown.clear()
        
        for path in paths:
            self.path_dropdown.addItem(path[0])

    def create_files(self):
        selected_path = self.path_dropdown.currentText()
        
        txt_files = glob.glob(os.path.join(selected_path, '*.txt'))
        folder_id, folder_path, folder_notion_id, config_id = self.folder_repository.get_folder_by_path(selected_path)

        for txt_file in txt_files:
            try:
                self.current_file_label.setText(f"Creating {os.path.basename(txt_file)} file on notion")
                QApplication.processEvents()  # Force GUI update
                
                self.file_service.create_file(txt_file, folder_notion_id, folder_id)
                
                self.current_file_label.setText(f"|")
                QApplication.processEvents()  # Force GUI update
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", f"Failed to create {os.path.basename(txt_file)} file on notion")
            
        QMessageBox.information(self, "Success", f"Files created successfully on Notion")
            