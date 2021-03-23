from flask import Flask, request
from vkaudiotoken import get_vk_official_token

app = Flask(__name__)


@app.route('/token.get', methods=['POST'])
def get_token():
    login = request.args.get('login')
    password = request.args.get('password')
    token = get_vk_official_token(login=login, password=password)
    return token


if __name__ == '__app__':
    app.run()
