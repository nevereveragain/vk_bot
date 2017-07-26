# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, json
import settings
import messageHandler

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return settings.confirmation_token
    elif data['type'] == 'message_new':
        messageHandler.create_answer(data['object'], settings.token, settings.moderator_id)
    return 'ok'
