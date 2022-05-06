import slack
import os
from pathlib import Path
from dotenv import load_dotenv

#Set the path of .env file using pathlib
token_path=Path('.') / '.env'
#loading env with load_dotenv function of python-dotenv module
load_dotenv(dotenv_path=token_path)
#saving bot api token as variable
bot_api_token=os.environ['bot_token']

client=slack.WebClient(token=bot_api_token)
client.chat_postMessage(channel='#blogs',text='Hello Webmatrices Readers !')
print("Bot is ready!")
