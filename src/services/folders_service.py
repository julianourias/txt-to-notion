import requests

from repositories.configs_repository import ConfigRepository
from repositories.folders_repository import FolderRepository

NOTION_API_URL = "https://api.notion.com/v1"


class FolderService:
    def __init__(self) -> None:
        self.config_repository = ConfigRepository()
        self.folder_repository = FolderRepository()
    
    def _create_folder_on_notion(self, title):
        data = {
            "parent": { 
                "type": "page_id",
                "page_id": self.config_repository.get_notion_id()
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

        response = requests.post(F'{NOTION_API_URL}/pages', headers=self.config_repository.get_headers(), json=data)
        
        return response
    
    def create_folder(self, path):
        try:
            response = self._create_folder_on_notion(path)  
            
            print(response.json())

            if response.status_code == 200:
                self.folder_repository.insert_folder(path, response.json()['id'], self.config_repository.get_config_id())
            else:
                raise Exception('Failed to create folder on Notion')
        except Exception as e:
            return e