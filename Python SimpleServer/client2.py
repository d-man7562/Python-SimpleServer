import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("141.114.159.120",8080))
msg = b""
while True:
    chunk = s.recv(1024)
    if not chunk:
        break
    msg+=chunk
# msg = s.recv(1024)
print(msg.decode("utf-8"))