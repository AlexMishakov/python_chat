import socket
import threading
import json

def listen_server():
    while True:
        data = sock.recv(1024)
        obj_str = data.decode('UTF-8')
        send_obj = json.loads(obj_str)
        print(send_obj['date_time'], send_obj['name'], ':', send_obj['msg'])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))

listen_thread = threading.Thread(target=listen_server)
listen_thread.start()

name = 'Vova'

while True:
    msg = input()
    send_obj = {
        'name': name,
        'msg': msg
    }
    bt = bytes(json.dumps(send_obj), encoding='UTF-8')
    sock.send(bt)