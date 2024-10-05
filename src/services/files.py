import requests
import glob
import os

from repositories.configs import ConfigRepository
from repositories.files import FileRepository
from repositories.folders import FolderRepository


class ServiceFile:
    def __init__(self) -> None:
        self.config_repository = ConfigRepository()
        self.headers = self.config_repository.get_headers()
        
        self.folder_repository = FolderRepository()
        self.file_repository = FileRepository()
        
    def _get_paragraphs(self, content):
        paragraphs = []
        batch_size = 2000
        
        for i in range(0, len(content), batch_size):
            paragraph = {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": str(content[i:i+batch_size])
                            }
                        }
                    ],
                    "color": "default"
                }
            }
            
            paragraphs.append(paragraph)
            
        return paragraphs
    
    def create_file_on_notion(self, notion_id, title, content):
        data = {
            "parent": { 
                "type": "page_id",
                "page_id": notion_id  
            },
            "icon": {
                "emoji": "🗒️"
            },
            "properties": {
                "title": [
                    {
                        "text": {
                            "content": title
                        }
                    }
                ]
            },
            "children": self._get_paragraphs(content)
        }

        response = requests.post('https://api.notion.com/v1/pages', headers=self.headers, json=data)
        
        return response
    
    def create_file(self, txt_file, notion_id):
        try:
            with open(txt_file, 'r', encoding='utf-8') as file:
                content = file.read()
            
            response = self.create_file_on_notion(notion_id, os.path.basename(txt_file), content)
            
            print(response.json())

            if response.status_code == 200:
                self.file_repository.insert_file(os.path.basename(txt_file), response.json()['id'], response.json()['last_edited_time'], 1)
            else:
                raise Exception('Failed to create file on Notion')
        except Exception as e:
            return e