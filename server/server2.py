import socket
import threading

def listen_user(conn):
    data = conn.recv(1024)
    print(str(data))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')

while True:
    conn, addr = sock.accept()

    print('connected:', addr)

    conn_thread = threading.Thread(target=listen_user, args=(conn,))
    conn_thread.start()

conn.close()