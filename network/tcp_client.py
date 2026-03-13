import socket
from utils.logger import setup_logger
logger = setup_logger()

class TCPClient:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.sock = None

    def connect(self):
        logger.info(f"Connecting to {self.ip}:{self.port}")
        self.sock = socket.create_connection((self.ip,self.port),timeout=5)
        logger.info("Connection Established")

    def send(self,data):
        logger.info(f"Sending packets :{data}")
        self.sock.sendall(data.encode())

    def receive(self,buffer_size=1024):
        data = self.sock.recv(buffer_size)
        response = data.decode()
        logger.info(f"Received response: {response}")
        return data.decode()

    def close(self):
        if self.sock:
            logger.info("Closing Connection")
            self.sock.close()
            self.sock = None
