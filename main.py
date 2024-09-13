import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the Notion API key from environment variables
NOTION_TOKEN = os.getenv('NOTION_TOKEN')

# Define the URL
url = 'https://api.notion.com/v1/blocks/b55c9c91-384d-452b-81db-d1ef79372b75/children'

# Define the headers
headers = {
    'Authorization': f'Bearer {NOTION_TOKEN}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}

# Define the data payload
data = {
    "children": [
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Lacinato kale"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
                            "link": {
                                "url": "https://en.wikipedia.org/wiki/Lacinato_kale"
                            }
                        }
                    }
                ]
            }
        }
    ]
}

# Make the PATCH request
response = requests.patch(url, headers=headers, data=json.dumps(data))

# Check the response
if response.status_code == 200:
    print("Blocks updated successfully!")
else:
    print(f"Failed to update blocks: {response.status_code}")
    print(response.text)