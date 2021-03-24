import requests
from flask import Flask, request, jsonify
from vkaudiotoken import get_vk_official_token, TokenException

app = Flask(__name__)
user_agent = 'VKAndroidApp/5.52-4543 (Android 5.1.1; SDK 22; x86_64; unknown Android SDK built for x86_64; en; 320x240)'


@app.route('/token.get', methods=['GET', 'POST'])
def get_token():
    login = str(request.args.get('login'))
    password = str(request.args.get('password'))
    try:
        token = get_vk_official_token(login=login, password=password)
    except TokenException as ex:
        return jsonify(ex.extra)
    return token


@app.route('/audio.get', methods=['GET', 'POST'])
def get_all_audio():
    count = request.args.get('count')
    access_token = request.args.get('access_token')

    sess = requests.session()
    sess.headers.update({'User-Agent': user_agent})
    response = sess.get(
        "https://api.vk.com/method/audio.get/",
        params=[
                ('count', count),
                ('access_token', access_token),
                ('v', '5.95')]
    )
    print(response.json())
    return response.json()


if __name__ == '__app__':
    app.run()
