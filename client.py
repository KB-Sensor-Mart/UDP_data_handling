import socket
import time

class UDPClient:
    def __init__(self, server_ip: str, server_port: int, interval: float=2.0):
        """Initialize the UDP client with server IP and port."""
        self.server_ip = server_ip
        self.server_port = server_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket
        self.interval = interval
    

    def send_data(self, message: str):
        """Send a message to the UDP server."""
        try:
            print(f"Sending message to {self.server_ip}:{self.server_port}")
            self.sock.sendto(message.encode(), (self.server_ip, self.server_port))  # Send message
            print("Message sent!")
        except Exception as e:
            print(f"Failed to send message: {e}")
    
    def start_sending(self,message:str):
        try:
            while True:
                self.send_data(message)
                time.sleep(self.interval)
        except KeyboardInterrupt:
            print("Client Stopped")
        except Exception as e:
            print(f"error occured")
            
if __name__ == "__main__":
    # Server IP and port (must match the server settings)
    server_ip = "192.168.31.131"  # Localhost for testing on the same machine
    server_port = 8000       # Make sure the port matches the server port
    # Create client and send data
    client = UDPClient(server_ip, server_port, interval=2.0)
    message = "Hello UDP"
    
    # Example messages
    client.start_sending(message)