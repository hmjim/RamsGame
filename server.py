from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room
from engine import RamsEngine
import database

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
engine = RamsEngine()
rooms = {}


@socketio.on('join_room')
def on_join(data):
    room = data['room']
    join_room(room)
    if room not in rooms:
        rooms[room] = {'players': [], 'table': [], 'state': 'waiting'}
    rooms[room]['players'].append(request.sid)
    emit('status', {'msg': 'Игрок присоединился'}, room=room)


@socketio.on('get_leaderboard')
def send_top():
    top_data = database.get_top()
    emit('leaderboard_data', {'top': top_data})


if __name__ == '__main__':
    database.init_db()
    # Слушаем на всех интерфейсах (0.0.0.0), порт 5000
    socketio.run(app, host='0.0.0.0', port=5000)

