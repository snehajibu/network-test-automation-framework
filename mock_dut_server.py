import socket
from utils.config_loader import load_config
from utils.logger import setup_logger

config = load_config()
logger = setup_logger()

HOST = config["server"]["ip"]
PORT = config["server"]["port"]

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

server.bind((HOST,PORT))
server.listen()

logger.info(f"Mock DUT Server running on {HOST}:{PORT}")

while True:
    conn,addr = server.accept() #2 sockets now, server -> listens only, conn -/. send/receives data
    logger.info(f"Client connected: {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            logger.info("Client disconnected")
            break
        message = data.decode().strip()
        logger.info(f"Received: {message}")

        if message == "HELLO":
            response = "ACK"
        elif message == "PING":
            response = "PONG"
        elif message == "VERSION":
            response = "VERSION_1.0"
        elif message == "STATUS":
            response = "OK"
        elif message == "RESET":
            response = "RESET DONE"
        else:
            response = "ERROR"
        logger.info(f"Sending response: {response}")
        conn.sendall(response.encode())
    conn.close()

