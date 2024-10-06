from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFileDialog, QHBoxLayout

from repositories.folders_repository import FolderRepository
from repositories.configs_repository import ConfigRepository
from services.folders_service import FolderService
from PyQt6.QtGui import QIcon, QPixmap

class AddPastaWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.repository = FolderRepository()
        self.service = FolderService()

        layout = QVBoxLayout()

        # Path to Directory
        self.path_label = QLabel("Criar pasta no Notion:")
        self.path_input = QLineEdit()
        layout.addWidget(self.path_label)

        # Button to open file explorer
        self.open_file_explorer_button = QPushButton()
        
        folder_icon = QIcon(QPixmap("src\\assets\\folder.svg"))
        self.open_file_explorer_button.setIcon(folder_icon)
        self.open_file_explorer_button.clicked.connect(self.open_file_explorer)

        path_layout = QHBoxLayout()
        path_layout.addWidget(self.path_input)
        path_layout.addWidget(self.open_file_explorer_button)
        layout.addLayout(path_layout)
        
        # Save Button
        self.save_button = QPushButton("Adicionar Pasta")
        self.save_button.clicked.connect(self.save_data)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def open_file_explorer(self):
        directory = QFileDialog.getExistingDirectory(self, "Selecione a Pasta")
        if directory:
            self.path_input.setText(directory)

    def save_data(self):
        path = self.path_input.text()

        if not path:
            QMessageBox.warning(self, "Input Error", "Preencha o campo de pasta")
            return

        row = self.repository.get_folder_by_path(path)
        if row:
            QMessageBox.warning(self, "Input Error", "Pasta já adicionada")
            return
        
        self.service.create_folder(path)

        QMessageBox.information(self, "Success", "Pasta adicionada com sucesso")