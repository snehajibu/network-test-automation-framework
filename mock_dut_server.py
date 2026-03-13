import socket
from utils.config_loader import load_config
from utils.logger import setup_logger

config = load_config()
logger = setup_logger()

HOST = config["server"]["ip"]
PORT = config["server"]["port"]

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()

logger.info(f"Mock DUT Server running on {HOST}:{PORT}")

while True:
    conn,addr = server.accept()
    logger.info(f"Client connected: {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            logger.info("Client disconnected")
            break
        message = data.decode()
        logger.info(f"Received: {message}")
        conn.sendall(message.encode())
    conn.close()

