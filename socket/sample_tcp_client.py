import socket

# SOCK_STREAM : TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 50010))
    s.sendall(b'hello')
    print('sendall')
    data = s.recv(1024)
    print(repr(data))
