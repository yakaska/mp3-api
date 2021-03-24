from flask import Flask, request, jsonify
from vkaudiotoken import get_vk_official_token, TokenException

app = Flask(__name__)


@app.route('/token.get', methods=['GET', 'POST'])
def get_token():
    login = str(request.args.get('login'))
    password = str(request.args.get('password'))
    try:
        token = get_vk_official_token(login=login, password=password)
    except TokenException as ex:
        return jsonify(ex.extra)
    return token


if __name__ == '__app__':
    app.run()
