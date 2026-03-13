from network.tcp_client import TCPClient
from device.dut_device import DUTDevice
from utils.config_loader import load_config
import time


def test_stress_packets(dut):

    for i in range(100):
        packet = f"STRESS_PACKET_{i}"
        response = dut.send_packet(packet)
        assert response == packet
        time.sleep(0.01)
