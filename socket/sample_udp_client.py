import socket

# SOCK_DGRAM : UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b'hello TDP', ('127.0.0.1', 50010))
