from socket import SOCK_STREAM, socket

sock = socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print(f'Connected: {addr}')

try:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data.upper())

finally:
    conn.close()