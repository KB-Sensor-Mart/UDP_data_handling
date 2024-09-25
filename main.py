import socket
import json
import logging
from typing import Tuple

class UDPServer:
    def __init__(self, ip: str, port: int, buffer_size: int = 1024, json_file:str = "udp_data.json"):
        self.server_ip = ip
        self.server_port = port
        self.buffer_size = buffer_size
        self.json_file = None
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #setup the logging 
        logging.basicConfig(
            filename="server.log",
            level = logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
        )
        self.logger = logging.getLogger()
        try:
            print("server is started and binding up the address")
            self.logger.info(f"Binding UDP server on {self.server_ip}:{self.server_port}")
            self.sock.bind((self.server_ip, self.server_port))  # Bind the socket to IP and port
            self.logger.info(f"UDP server started on {self.server_ip}:{self.server_port}")
            print(f"UDP server started on {self.server_ip}:{self.server_port}")
            print("To stop server press (Ctrl+C)")
        except Exception as e:
            self.logger.error(f"Failed to bind the UDP socket: {e}")
            raise

    def receive_data(self) -> Tuple[str, Tuple[str, int]]:
        """
        Receive data from the client over UDP.
        :return: Decoded data and client address.
        """
        try:
            self.logger.info("Server is running andn waiting for data...")
            data, addr = self.sock.recvfrom(self.buffer_size)  # Receive data from client
            decoded_data = data.decode()
            self.logger.info(f"Received data from {addr}: {decoded_data}")
            print("Data received and written in json file")
            return decoded_data, addr
        except socket.error as e:
            self.logger.info(f"Error receiving data: {e}")
            raise
        
    def store_data(self, data: dict):
        """
        Store received data in a JSON file.
        :param data: The data to be stored.
        """
        try:
            if not self.json_file:
                raise ValueError("No file set for storing Json Data.")
            with open(self.json_file, 'a') as json_file:  # Open the file in append mode
                json.dump(data, json_file)
                json_file.write("\n")  # Ensure each data entry is on a new line
            self.logger.info(f"Data successfully stored in {self.json_file}")
        except Exception as e:
            self.logger.error(f"Failed to write data to JSON file: {e}")
            raise e

    def start(self):
        self.json_file = json_file
        """
        Start the UDP server and listen for incoming data.
        """
        logging.info("Server is now running and waiting for incoming data.")
        while True:
            try:
                data, addr = self.receive_data()
                json_data = {"address": addr, "message": data}
                self.store_data(json_data)
            except KeyboardInterrupt:
                print("server shutting down...")
                self.logger.info("Server shutting down...")
                break
            except Exception as e:
                self.logger.error(f"An error occurred during execution: {e}")


if __name__ == "__main__":
    # Set IP, Port, and JSON file name
    server_ip = "192.168.31.131"
    server_port = 62200
    json_file = "udp_data.json"
    
    # Create and start the UDP server
    try:
        udp_server = UDPServer(server_ip, server_port, json_file=json_file)
        udp_server.start()
    except Exception as e:
        logging.critical(f"Server failed to start: {e}")