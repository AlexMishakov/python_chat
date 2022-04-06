import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect(('localhost', 55000))
    msg = input('massage: ')
    sock.send(bytes(msg, encoding = 'UTF-8'))
    data = sock.recv(1024)
    sock.close()
    print(data)
except:
    print("Connection failed")

input("Press enter to exit")