import logger
from network.tcp_client import TCPClient
from utils.logger import setup_logger
logger = setup_logger()

class DUTDevice:
    def __init__(self,client):
        self.client = client
    def send_packet(self,data):
        logger.info(f"DUT sending packet: {data}")
        self.client.send(data)
        response = self.client.receive()
        logger.info(f"DUT received response: {response}")
        return response

    def receive_packet(self):
        logger.info("Receiving packet from DUT")
        return self.client.receive()

    def close(self):
        logger.info("Closing Connection")
        self.client.close()
