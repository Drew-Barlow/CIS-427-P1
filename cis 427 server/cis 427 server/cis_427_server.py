# Drew Barlow
import socket

PORT_NUM = 6810
NUM_REQUESTS_ALLOWED = 5
NUM_BYTES = 1024
HEADER = 10

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((socket.gethostname(), PORT_NUM))

server_socket.listen(NUM_REQUESTS_ALLOWED)

# Function to let the user login
def login():
    user = client_socket.recv(NUM_BYTES)
    user = user.decode("utf-8")

    if user == "root root22":
        print(user)
        print("SUCCESS")
        solve()
        logout()
        shutdown()
    elif user == "john john22":
        print(user)
        print("SUCCESS")
        solve()
        logout()
        shutdown()
    elif user == "sally sally22":
        print(user)
        print("SUCCESS")
        solve()
        logout()
        shutdown()
    elif user == "qiang qiang22":
        print(user)
        print("SUCCESS")
        solve()
        logout()
        shutdown()
    else:
        client_socket.send(bytes("FAILURE: Please provide correct username and password. Try again. ", "utf-8"))

# Function to solve for circle or rectangle
def solve():
    eq = client_socket.recv(NUM_BYTES)
    eq = eq.decode("utf-8")
   

# Function that displays the list of solutions
def list():
    msg = client_socket.recv(NUM_BYTES)
    msg = msg.decode("utf-8")

# Function to logout the user   
def logout():
    clientMessageLogout = client_socket.recv(NUM_BYTES)
    clientMessageLogout = clientMessageLogout.decode("utf-8")
    if clientMessageLogout == "LOGOUT":
        print("200 OK")

# Function to shutdown the server
def shutdown():
    clientMessageShutdown = client_socket.recv(NUM_BYTES)
    clientMessageShutdown = clientMessageShutdown.decode("utf-8")
    if clientMessageShutdown == "SHUTDOWN":
        print("200 OK")
        client_socket.shutdown(socket.SHUT_RDWR)
        server_socket.close()

# Loop that accepts any new clients
while True:
    client_socket, address = server_socket.accept()

    print(f"Connection established with client at {address}")
    openingMessage = "Server connection established!"
    #openingMessage = f"{len(openingMessage):<{HEADER}}" + openingMessage
    client_socket.send(bytes(openingMessage, "utf-8"))

    def openFile():
        with open('logins.txt','r') as file:
            lines = file.readlines()
    login()
    



    

    