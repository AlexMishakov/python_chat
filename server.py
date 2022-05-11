import socket
import threading
import json
from datetime import datetime

def listen_user(conn, addr):
    while True:
        try:
            data = conn.recv(1024)
            msg = data.decode('UTF-8')
            send_obj = json.loads(msg)
            now = datetime.now()
            send_obj['date_time'] = now.strftime("%d/%m/%Y %H:%M:%S")
            print(send_obj)
            bt = bytes(json.dumps(send_obj), encoding='UTF-8')
            send_all(conn, bt)
        except:
            print(addr, 'disconnected')
            conn.close()
            conn_list.remove(conn)
            break

def send_all(conn_from, msg):
    for conn in conn_list:
        if conn != conn_from:
            conn.send(msg)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(30)
print('Server start')

conn_list = []

while True:
    conn, addr = sock.accept()
    conn_list.append(conn)
    print('connected: ', addr)
    conn_thread = threading.Thread(target=listen_user, args=(conn, addr,))
    conn_thread.start()
