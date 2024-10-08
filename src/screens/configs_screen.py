from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QStyle
from PyQt6.QtGui import QIcon, QPixmap

from repositories.configs_repository import ConfigRepository


class ConfigEntryWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.repository = ConfigRepository()

        layout = QVBoxLayout()

        # Notion ID RAIZ
        self.notion_id_label = QLabel("Notion ID ou URL da Página:")
        self.notion_id_input = QLineEdit()
        layout.addWidget(self.notion_id_label)
        layout.addWidget(self.notion_id_input)
        
        # Notion Key
        self.notion_key_label = QLabel("Notion Key:")
        layout.addWidget(self.notion_key_label)
        
        # Button to toggle password visibility
        self.notion_key_input = QLineEdit()
        self.notion_key_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.toggle_visibility_button = QPushButton()
        self.toggle_visibility_button.setCheckable(True)
        
        # Set button Icon
        eye_icon = QIcon(QPixmap("src\\assets\\eye.svg"))
        self.toggle_visibility_button.setIcon(eye_icon)
        self.toggle_visibility_button.toggled.connect(self._toggle_password_visibility)

        # Add key input and button in row
        key_layout = QHBoxLayout()
        key_layout.addWidget(self.notion_key_input)
        key_layout.addWidget(self.toggle_visibility_button)
        layout.addLayout(key_layout)

        # Save Button
        self.save_button = QPushButton("Salvar")
        self.save_button.clicked.connect(self._save_config)
        layout.addWidget(self.save_button)

        self.setLayout(layout)
        self._load_existing_config()

    def _toggle_password_visibility(self, checked):
        if checked:
            self.notion_key_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.notion_key_input.setEchoMode(QLineEdit.EchoMode.Password)

    def _load_existing_config(self):
        config = self.repository.get_config()

        if config:
            notion_key, notion_id = config
            self.notion_key_input.setText(notion_key)
            self.notion_id_input.setText(notion_id)

    def _save_config(self):
        notion_key = self.notion_key_input.text()
        notion_url = self.notion_id_input.text()

        if not notion_key or not notion_url:
            QMessageBox.warning(self, "Input Error", "Preencha todos os campos")
            return

        # Extract id from this url https://www.notion.so/Notes-{NOTION_ID}, is after - so we split by - and get the last element
        notion_id = notion_url.split('-')[-1]

        self.repository.insert_config(notion_key, notion_id)

        QMessageBox.information(self, "Success", "Configurações salvas com sucesso")