import pytest
from utils.config_loader import load_config
from network.tcp_client import TCPClient
from device.dut_device import DUTDevice

@pytest.fixture
def dut():
    """
    Provides a connected DUT device for tests
    """
    config = load_config()

    ip = config["server"]["ip"]
    port = config["server"]["port"]

    client = TCPClient(ip,port)
    client.connect()

    device = DUTDevice(client)
    yield device

    device.close()