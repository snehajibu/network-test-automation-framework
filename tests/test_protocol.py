from network.packet_sender import PacketSender

def test_ping(dut):
    sender = PacketSender(dut)
    response = sender.send_ping()
    assert response == "PONG"

def test_version(dut):
    sender = PacketSender(dut)
    response = sender.send_version_request()
    assert response == "VERSION_1.0"

def test_invalid_command(dut):
    sender = PacketSender(dut)
    response = sender.send("INVALID")
    assert response == "ERROR"
