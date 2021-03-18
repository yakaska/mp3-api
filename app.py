import socket

from flask import Flask, jsonify, request
from vk_api import vk_api
from vk_api.audio import VkAudio

from Audio import Track

app = Flask(__name__)


@app.route('/')
def home():
    return "Home"


@app.route('/token', methods=['POST', 'GET'])
def get_token():
    login = request.args.get('login')
    password = request.args.get('password')
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    token = vk_session.token
    return token


@app.route('/audio', methods=['POST', 'GET'])
def get_audio():
    login = request.args.get('login')
    token = request.args.get('token')
    vk_session = vk_api.VkApi(login=login, token=token)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk_audio = VkAudio(vk_session)
    tracks = vk_audio.get_iter()
    songs = []
    for n, track in enumerate(tracks, 1):
        songs.append(Track(track['title'], track['artist'], track['url'], track['track_covers'],
                           track['duration'] * 1000).serialize())
        if len(songs) == 5:
            tracks.close()
            break
    return jsonify(songs)


if __name__ == '__app__':
    app.run()
