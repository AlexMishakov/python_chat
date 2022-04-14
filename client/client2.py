import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect(('localhost', 55000))
    msg = input('massage: ')
    sock.send(bytes(msg, encoding = 'UTF-8'))
    sock.close()
except:
    print("Connection failed")

input("Press enter to exit")