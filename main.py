import requests
import json
from dotenv import load_dotenv
import os
import glob

# Load environment variables from .env file
load_dotenv()

# Get the Notion API key from environment variables
NOTION_API_KEY = os.getenv('NOTION_API_KEY')
PAGE_ID = os.getenv('PAGE_ID')
# Define the path to the directory containing the .txt files
DIRECTORY_PATH = os.getenv('DIRECTORY_PATH')

# Define the URL
url = 'https://api.notion.com/v1/pages'

# Define the headers
headers = {
    'Authorization': f'Bearer {NOTION_API_KEY}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}

# Use glob to find all .txt files in the directory
txt_files = glob.glob(os.path.join(DIRECTORY_PATH, '*.txt'))

# Loop through each file and read its contents
for file_path in txt_files:
    with open(file_path, 'r', encoding='UTF-8') as file:
        content = file.read()
        print(content)
        title = file_path.title()

        # Define the data payload
        data = {
            "parent": {
                "type": "page_id",
                "page_id": PAGE_ID
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
                    "paragraph": {
                        "rich_text": [
                            {
                                "text": {
                                    "content": content,
                                },
                            }
                        ],
                        "color": "default"
                    }
                }
            ]
        }

        # Make the POST request
        print(data)
        response = requests.post(url, headers=headers, data=json.dumps(data))

        # Check the response
        if response.status_code == 200:
            print("Page created successfully!")
            print(response.json())
        else:
            print(f"Failed to create page: {response.status_code}")
            print(response.text)