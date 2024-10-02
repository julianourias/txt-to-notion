import requests
import glob
import os

from repositories.configs import ConfigRepository
from repositories.files import FileRepository


class ServiceFile:
    def __init__(self) -> None:
        self.config_repository = ConfigRepository()
        self.headers = self.config_repository.get_headers()
        self.notion_id = self.config_repository.get_notion_id()
        
        self.file_repository = FileRepository()
    
    def create_file_on_notion(self, title, content):
        data = {
            "parent": { 
                "type": "page_id",
                "page_id": self.notion_id  
            },
            "icon": {
                "emoji": "🥬"
            },
            "cover": {
                "external": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/6/62/Tuscankale.jpg"
                }
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
            "children": [
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": str(content)
                                }
                            }
                        ],
                        "color": "default"
                    }
                }
            ]
        }

        response = requests.post('https://api.notion.com/v1/pages', headers=self.headers, json=data)
        
        return response
    
    def create_files(self, path):
        txt_files = glob.glob(os.path.join(path, '*.txt'))

        try:
            for txt_file in txt_files:
                with open(txt_file, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                response = self.create_file_on_notion(os.path.basename(txt_file), content)
                
                print(response)

                if response.status_code == 200:
                    self.file_repository.insert_file(os.path.basename(txt_file), response.json()['id'], response.json()['last_edited_time'], 1)
                else:
                    raise Exception('Failed to create file on Notion')
        except Exception as e:
            return e