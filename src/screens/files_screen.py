
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QComboBox, QHBoxLayout
from PyQt6.QtGui import QIcon, QPixmap
import glob
import os

from services.files_service import ServiceFile
from repositories.folders_repository import FolderRepository

class NotionFileCreatorWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.file_service = ServiceFile()
        self.folder_repository = FolderRepository()

        layout = QVBoxLayout()
        
        # Path Dropdown
        self.path_label = QLabel("Selecione a Pasta:")
        self.path_dropdown = QComboBox()
        layout.addWidget(self.path_label)
        
        # Refresh Paths Button
        self.refresh_folders_button = QPushButton()
        
        # Set button Icon
        folder_icon = QIcon(QPixmap("_internal\\assets\\refresh.svg"))
        self.refresh_folders_button.setIcon(folder_icon)
        self.refresh_folders_button.setFixedWidth(30)
        self.refresh_folders_button.clicked.connect(self._populate_path_dropdown)

        # Add key input and button in row
        path_layout = QHBoxLayout()
        path_layout.addWidget(self.path_dropdown)
        path_layout.addWidget(self.refresh_folders_button)
        layout.addLayout(path_layout)
        
        # Create Files Button
        self.create_files_button = QPushButton("Sincronizar Arquivos")
        self.create_files_button.clicked.connect(self._sync_files)
        layout.addWidget(self.create_files_button)
        
        # Current File Label
        self.current_file_label = QLabel("")
        layout.addWidget(self.current_file_label)

        self.setLayout(layout)

        self._populate_path_dropdown()

    def _populate_path_dropdown(self):
        paths = self.folder_repository.get_paths()
        self.path_dropdown.clear()
        
        for path in paths:
            self.path_dropdown.addItem(path[0])

    def _sync_files(self):
        selected_path = self.path_dropdown.currentText()
        
        txt_files = glob.glob(os.path.join(selected_path, '*.txt'))
        folder_id, folder_path, folder_notion_id, config_id = self.folder_repository.get_folder_by_path(selected_path)

        for txt_file in txt_files:
            try:
                self.current_file_label.setText(f"Sincronizando arquivo {os.path.basename(txt_file)} ao Notion...")
                QApplication.processEvents()  # Force GUI update
                
                self.file_service.sync_file(txt_file, folder_notion_id, folder_id)
                
                self.current_file_label.setText(f"")
                QApplication.processEvents()  # Force GUI update
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", f"Falha ao sincronizar arquivo {os.path.basename(txt_file)} ao Notion: {e}")
            
        QMessageBox.information(self, "Success", f"Arquivos sincronizados com sucesso ao Notion!")
            