# Create a Integration to get key
https://www.notion.so/profile/integrations/form/new-integration

# Create a ".env" file on the root of this project and put your key, directory and a page id
```
NOTION_API_KEY="your_token"
PAGE_ID="your_page_id"
DIRECTORY_PATH="directory_of_yours_txt"
```

# get you page id
To get the PAGE_ID for your Notion page, follow these steps:

Open Notion: Go to your Notion workspace and open the page you want to use.

The URL will look something like this: https://www.notion.so/yourworkspace/Your-Database-Name-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
The PAGE_ID is the part after the last slash and before any query parameters, typically a 32-character string of letters and numbers.
For example, if the URL is:

The PAGE_ID is:

Update your .env file with the correct PAGE_ID:

Now your script will be able to use the correct PAGE_ID to interact with your Notion page.

# Add permission to your page
https://developers.notion.com/docs/create-a-notion-integration#give-your-integration-page-permissions

# Run the script
```
python main.py
```