from flask import Flask, render_template, request
import random
from decouple import config
import requests
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
url = 'https://api.telegram.org/bot'

@app.route('/write')
def write():
    return render_template('write.html')




@app.route('/send')
def send():
    text = request.args.get('text')
    requests.get(f'{url}{token}/sendmessage?chat_id={chat_id}&text={text}')
    return render_template("send.html")

@app.route(f'/{token}', methods=["POST"])
def telegram():
    #  request.get_json()
    chat_id = request.get_json()['message']['chat']['id']
    text = request.get_json()['message']['text']   
    if text == "안녕":
        return_text = "hola!"
    elif text == "ㄹㄸ":
        numbers = range(1,46)
        return_text = sorted(random.sample(numbers, 6))
    else :
        return_text = "그말은 뭔 소린지 모르겠어"
    
    
    requests.get(f'{url}{token}/sendmessage?chat_id={chat_id}&text={return_text}')
    return "ok", 200






if __name__ == '__main__':
    app.run(debug=True)
