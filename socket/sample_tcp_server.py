import socket

# SOCK_STREAM : TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 50010))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print('data: {}, addr {}'.format(data, addr))
                conn.sendall(b'Received: ' + data)

