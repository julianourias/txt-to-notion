import requests
import os
from difflib import HtmlDiff
from datetime import datetime, timedelta

from repositories.configs_repository import ConfigRepository
from repositories.files_repository import FileRepository
from repositories.folders_repository import FolderRepository


class ServiceFile:
    def __init__(self) -> None:
        self.config_repository = ConfigRepository()
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
    
    def _create_file_on_notion(self, folder_notion_id, title, content):
        data = {
            "parent": { 
                "type": "page_id",
                "page_id": folder_notion_id  
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

        response = requests.post('https://api.notion.com/v1/pages', headers=self.config_repository.get_headers(), json=data)
        
        return response
        
    def _get_file_from_notion(self, file_notion_id):
        response = requests.get(f'https://api.notion.com/v1/pages/{file_notion_id}', headers=self.config_repository.get_headers())
        
        return response.json()
        
    def _patch_file_on_notion(self, file_notion_id, content):
        blocks = self._get_all_file_blocks(file_notion_id)
        
        for block in blocks['results']:
            if block['type'] == 'paragraph':
                requests.delete(f'https://api.notion.com/v1/blocks/{block["id"]}', headers=self.config_repository.get_headers())
        
        data = {
            "children": self._get_paragraphs(content)
        }

        response = requests.patch(f'https://api.notion.com/v1/blocks/{file_notion_id}/children', headers=self.config_repository.get_headers(), json=data)
        
        return response
    
    def _get_all_file_blocks(self, file_notion_id):
        response = requests.get(f'https://api.notion.com/v1/blocks/{file_notion_id}/children?page_size=100', headers=self.config_repository.get_headers())
        
        return response.json()
    
    def _get_content_notion(self, file_notion_id):
        blocks = self._get_all_file_blocks(file_notion_id)
        
        content = ''
        for block in blocks['results']:
            if block['type'] == 'paragraph':
                rich_text_list = block['paragraph']['rich_text']
                
                if len(rich_text_list) > 0:
                    content += f"{rich_text_list[0]['text']['content']}\n"
        
        return content
    
    def sync_file(self, txt_file, folder_notion_id, folder_id):
        try:
            file = self.file_repository.get_file_by_pasta_id_and_nome(folder_id, os.path.basename(txt_file))
            
            with open(txt_file, 'r', encoding='utf-8') as file_txt:
                content = file_txt.read()
            
            if file:
                print('File already exists')
                file_id, file_nome, file_notion_id, file_data_atualizacao, file_pasta_id = file
                
                file_notion = self._get_file_from_notion(file_notion_id)
                
                last_edited_notion = datetime.strptime(file_notion['last_edited_time'], '%Y-%m-%dT%H:%M:%S.%fZ') - timedelta(hours=3)
                last_edited_locally = datetime.fromtimestamp(os.path.getmtime(txt_file))
                
                last_file_sync = datetime.strptime(file_data_atualizacao, '%Y-%m-%dT%H:%M:%S.%fZ')
                
                if last_edited_locally > last_file_sync:
                    print('File has been modified')
                    
                    if last_edited_notion > last_file_sync:
                        print('File has been modified on Notion and locally')
                        d = HtmlDiff()
                        
                        content_notion = self._get_content_notion(file_notion_id) 
                        
                        html_diff = d.make_file(content_notion.splitlines(), content.splitlines())
                        
                        with open("diff.html", "w", encoding="utf-8") as f:
                            f.write(html_diff)
                        
                        raise Exception('Arquivo possui modificações não baixadas do notion, faça o merge de acordo com o arquivo gerado e envie novamente as atualizações')
                    else:
                        print('File has been modified only locally')
                        response = self._patch_file_on_notion(file_notion_id, content)
                        
                        print(response.json())
                        
                        if response.status_code == 200:
                            self.file_repository.update_file(file_id, datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
                        else:
                            raise Exception('Failed to update file on Notion')
                elif last_edited_notion > last_file_sync:
                    print('File has been modified on Notion')
                    content_notion = self._get_content_notion(file_notion_id) 
                    
                    with open(txt_file, 'w', encoding='utf-8') as file_txt:
                        file_txt.write(content_notion)
                        
                    self.file_repository.update_file(file_id, datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
                    
                else:
                    print('File has not been modified')
            
            else:
                print('File does not exist on Notion')
                response = self._create_file_on_notion(folder_notion_id, os.path.basename(txt_file), content)
                
                print(response.json())

                if response.status_code == 200:
                    self.file_repository.insert_file(os.path.basename(txt_file), response.json()['id'], datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'), folder_id)
                else:
                    raise Exception('Failed to create file on Notion')
        
        except Exception as e:
            print(e)
            raise e