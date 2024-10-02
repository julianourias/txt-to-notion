from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from repositories.configs import ConfigRepository


class ConfigEntryWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.repository = ConfigRepository()

        layout = QVBoxLayout()

        # Notion Key
        self.notion_key_label = QLabel("Notion Key:")
        self.notion_key_input = QLineEdit()
        layout.addWidget(self.notion_key_label)
        layout.addWidget(self.notion_key_input)

        # Notion ID RAIZ
        self.notion_id_label = QLabel("Notion ID:")
        self.notion_id_input = QLineEdit()
        layout.addWidget(self.notion_id_label)
        layout.addWidget(self.notion_id_input)

        # Save Button
        self.save_button = QPushButton("Salvar")
        self.save_button.clicked.connect(self.save_config)
        layout.addWidget(self.save_button)

        self.setLayout(layout)
        self.load_existing_config()


    def load_existing_config(self):
        config = self.repository.get_config()

        if config:
            notion_key, notion_id = config
            self.notion_key_input.setText(notion_key)
            self.notion_id_input.setText(notion_id)

    def save_config(self):
        notion_key = self.notion_key_input.text()
        notion_id = self.notion_id_input.text()

        if not notion_key or not notion_id:
            QMessageBox.warning(self, "Input Error", "All fields are required")
            return

        self.repository.insert_config(notion_key, notion_id)

        QMessageBox.information(self, "Success", "Data saved successfully")