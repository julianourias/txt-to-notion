import requests
import glob
import os

from repositories.configs import ConfigRepository
from repositories.folders import FolderRepository


class FolderService:
    def __init__(self) -> None:
        self.config_repository = ConfigRepository()
        self.headers = self.config_repository.get_headers()
        self.notion_id = self.config_repository.get_notion_id()
        self.config_id = self.config_repository.get_config_id()
        
        self.folder_repository = FolderRepository()
    
    def create_folder_on_notion(self, title):
        data = {
            "parent": { 
                "type": "page_id",
                "page_id": self.notion_id  
            },
            "icon": {
                "emoji": "📁"
            },
            "properties": {
                "title": [
                    {
                        "text": {
                            "content": title
                        }
                    }
                ]
            }
        }

        response = requests.post('https://api.notion.com/v1/pages', headers=self.headers, json=data)
        
        return response
    
    def create_folder(self, path):
        try:
            response = self.create_folder_on_notion(path)  
            print(response)

            if response.status_code == 200:
                self.folder_repository.insert_folder(path, response.json()['id'], self.config_id)
            else:
                raise Exception('Failed to create folder on Notion')
        except Exception as e:
            return e