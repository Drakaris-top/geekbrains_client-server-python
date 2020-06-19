from socket import  SOCK_DGRAM, socket
sock = socket(type=SOCK_DGRAM)

try:
    while True:
        data = 'Hello, servak'
        sock.sendto(data.encode('utf-8'), ('localhost', 9090))
        msg, addr = sock.recvfrom(1024)
        print(msg.decode('utf-8'))
finally:
    sock.close()