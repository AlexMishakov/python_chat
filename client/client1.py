import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
sock.connect(('localhost', 55000))  # подключемся к серверному сокету

msg = input('massage: ')
sock.send(bytes(msg, encoding = 'UTF-8'))  # отправляем сообщение
data = sock.recv(1024)  # читаем ответ от серверного сокета
sock.close()  # закрываем соединение
print(data)

input("Press enter to exit")