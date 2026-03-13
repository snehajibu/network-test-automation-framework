from utils.config_loader import load_config
from device.dut_device import DUTDevice
from network.tcp_client import TCPClient


def test_dut_connectivity(dut):

    response = dut.send_packet("HELLO")
    assert response == "HELLO"
