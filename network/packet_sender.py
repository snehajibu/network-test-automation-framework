import logger
from utils.logger import setup_logger
logger = setup_logger()

class PacketSender:
    def __init__(self,device):
        self.device = device

    def send(self,message):
        logger.info(f"PacketSender sending message: {message}")
        return self.device.send_packet(message)

    def send_ping(self):
        logger.info("Sending PING command")
        return self.device.send_packet("PING")

    def send_version_request(self):
        logger.info("Requesting VERSION")
        return self.device.send_packet("VERSION")
