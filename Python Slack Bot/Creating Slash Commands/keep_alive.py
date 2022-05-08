from flask import Flask, request, Response
from threading import Thread
import slack_sdk as slack
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

app = Flask('')

@app.route('/')
def home():
    return "The bot is alive!!"

@app.route('/greet', methods=['POST'])
def greet_command():
  data = request.form
  channel_id = data.get('channel_id')
  client.chat_postMessage(channel=channel_id, text="Howdy, How are you doing?")
  return Response(), 200

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
