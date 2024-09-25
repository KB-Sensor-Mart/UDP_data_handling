# UDP Server Data Logger

This project implements a UDP server that listens for incoming UDP messages, stores the received data in a JSON file, and logs all events and errors. The server is capable of receiving data from sensors or other devices over the network.

## Features
- **UDP Server**: The server binds to a specified IP address and port, listening for UDP messages.
- **Data Storage**: The received messages are stored in a JSON file, where each data entry is recorded on a new line.
- **Logging**: Server activities (start, stop, received messages, errors) are logged into a file (`server.log`).
- **Scalable Design**: The server can handle multiple clients by processing incoming data in a continuous loop.

## Getting Started

### Prerequisites
- **Python 3.6+**
- The following Python modules:
  - `socket` (standard library)
  - `json` (standard library)
  - `logging` (standard library)

### Installation

1. **Clone the Repository**:
   git clone https://github.com/your-username/udp-server-data-logger.git
   cd udp-server-data-logger
2. **Create virtual environment**:
    python -m venv env
    source env/bin/activate  # On Windows use: env\Scripts\activate
3. **install dependecies**:
    pip install -r requirements.txt  


### Running the Server

1. **Edit the configuration in main.py:**

    server_ip = "192.168.31.102"  # Replace with your IP address
    server_port = 62200  # Choose an available port number
    json_file = "udp_data.json"  # File where data will be stored

2. **Run the server:**

    python main.py
 
The server will start listening for incoming UDP data.
    
