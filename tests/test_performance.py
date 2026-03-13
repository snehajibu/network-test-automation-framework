from performance.iperf_runner import IperfRunner
from utils.config_loader import load_config

def test_network_performance():

    config = load_config()
    server_ip = config["server"]["ip"]
    min_expected = config["performance"]["min_throughput"]

    iperf = IperfRunner(server_ip)
    output = iperf.run_test()
    print(output)
    throughput = iperf.extract_throughput(output)
    assert throughput is not None, "Throughput not detected from iperf output"
    assert throughput >= min_expected
