from flask import Flask, request, Response
from threading import Thread
import slack_sdk as slack
import os
from pathlib import Path
from dotenv import load_dotenv
from slackeventsapi import SlackEventAdapter

#Set the path of .env file using pathlib
token_path=Path('.') / '.env'
#loading env with load_dotenv function of python-dotenv module
load_dotenv(dotenv_path=token_path)
#saving bot api token as variable
bot_api_token=os.environ['bot_token']

client=slack.WebClient(token=bot_api_token)

app = Flask('')
#Note that this piece of code should be added just after the assigning of app variable
slack_event_adapter=SlackEventAdapter(os.environ['signing_token'], '/slack/events', app)

@app.route('/')
def home():
    return "The bot is alive!!"

@app.route('/greet', methods=['POST'])
def greet_command():
  data = request.form
  channel_id = data.get('channel_id')
  client.chat_postMessage(channel=channel_id, text="Howdy, How are you doing?")
  return Response(), 200

@slack_event_adapter.on('reaction_added')
def reaction(payload):
  event = payload.get('event', {})
  channel_id = event.get('item', {}).get('channel')
  user_id = event.get('user')
  client.chat_postMessage(channel=channel_id, text=f"<@{user_id}>, you just reacted to a message.")

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
