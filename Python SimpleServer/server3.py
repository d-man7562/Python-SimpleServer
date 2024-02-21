import socket
import os
import subprocess
import time
PORT  = 8080
current_directory = os.getcwd()
SERVER = socket.gethostbyname(socket.gethostname())
ADDY = (SERVER, PORT)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ADDY))


server_socket.listen(3)
print(f"Server Started and listening on {ADDY}")
while True:
    clientsocket,addr = server_socket.accept()
    print(f"Connection from {addr} successful!")
    clientsocket.send(bytes("Welcome to my Minecraft server, user!".encode("utf-8"))) 
    clientsocket.send(bytes(f"\n\nGo to http://{SERVER}:8000".encode("utf-8")))
    clientsocket.send(bytes("\n\nOne moment...\n\n".encode("utf-8")))
    time.sleep(3)
    
    subprocess.run(["python", "-m", "http.server"], cwd=current_directory)
    # clientsocket.close()
    clientsocket.close()
    











    
# DisconnectMessage = "!DISCONNECT"
# link_message = f"Click <a href='http://{SERVER}:{PORT}/'>here</a> to view the contents of the folder."
    # clientsocket.send(bytes("Goto http://{SERVER}:8000 to view the contents of the folder.").encode("utf-8"))
    # clientsocket.send(bytes("\nGoto http://141.114.159.120:8000 to view the contents of the folder.".encode("utf-8")))