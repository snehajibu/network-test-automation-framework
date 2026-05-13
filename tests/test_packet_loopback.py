from network.tcp_client import TCPClient
from device.dut_device import DUTDevice
from utils.config_loader import load_config
from network.packet_sender import PacketSender

def test_packet_loopback(dut):

    sender = PacketSender(dut) # packet sender -> DUTDevice -> TCPClient


    response = sender.send_ping()

    assert response == "PONG"
