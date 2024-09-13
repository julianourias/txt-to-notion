# Create a Integration to get key
https://www.notion.so/profile/integrations/form/new-integration

# Create a ".env" file on the root of this project and put your key and a database id
```
NOTION_TOKEN="your_token"
DATABASE_ID="your_database_id"
```

# get you database id
To get the DATABASE_ID for your Notion database, follow these steps:

Open Notion: Go to your Notion workspace and open the database you want to use.

Copy the Database URL:

Click on the three dots in the upper-right corner of the database page.
Select "Copy link" to copy the URL of the database.
Extract the Database ID:

The URL will look something like this: https://www.notion.so/yourworkspace/Your-Database-Name-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
The DATABASE_ID is the part after the last slash and before any query parameters, typically a 32-character string of letters and numbers.
For example, if the URL is:

The DATABASE_ID is:

Update your .env file with the correct DATABASE_ID:

Now your script will be able to use the correct DATABASE_ID to interact with your Notion database.

# Add permission to your database
https://developers.notion.com/docs/create-a-notion-integration#give-your-integration-page-permissions
