from socket import SOCK_DGRAM, socket

sock = socket(type=SOCK_DGRAM)
sock.bind(('', 9090))


try:
    while True:
        msg, addr = sock.recvfrom(1024)
        print(msg.decode('utf-8'))
        ans = 'Hello, chuvak'
        sock.sendto(ans.encode('utf-8'), addr)

finally:
    sock.close()