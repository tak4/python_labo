import socket

# SOCK_DGRAM : UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('127.0.0.1', 50010))
    while True:
        data, addr = s.recvfrom(1024)
        print('data: {}, addr: {}'.format(data, addr))
