import socket
import json

class UDPServer:
    def __init__(self, ip: str, port: int, buffer_size: int = 1024):
        self.server_ip = ip
        self.server_port = port
        self.buffer_size = buffer_size
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            print(f"Binding UDP server on {self.server_ip}:{self.server_port}")
            self.sock.bind((self.server_ip, self.server_port))  # Bind the socket to IP and port
            print(f"UDP server started on {self.server_ip}:{self.server_port}")
        except Exception as e:
            print(f"Failed to bind the UDP socket: {e}")

    def receive_data(self):
        print("DEBUG: Waiting for data")
        data, addr = self.sock.recvfrom(self.buffer_size)  # Receive data from client
        print(f"DEBUG: Received data from {addr}: {data.decode()}")
        return data.decode() , addr
    
    def store_data(self, data: dict , file_name: str):
        try:
            with open(file_name, 'a') as json_file:  # Open the file in append mode
                json.dump(data, json_file)
                json_file.write("\n")  # Ensure each data entry is on a new line
            print(f"Data stored in {file_name}")
        except Exception as e:
            print(f"Failed to write data to JSON file: {e}")

    def start(self, json_file: str):
        while True:
            try:
                print("DEBUG: Server is running and waiting for data...")
                data, addr = self.receive_data()
                json_data = {"address": addr, "message": data}
                self.store_data(json_data, json_file)
            except KeyboardInterrupt:
                print("Server shutting down...")
                break
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Set IP, Port, and JSON file name
    server_ip = "0.0.0.0"
    server_port = 8000
    json_file = "udp_data.json"
    # Create and start the UDP server
    udp_server = UDPServer(server_ip, server_port)
    udp_server.start(json_file)