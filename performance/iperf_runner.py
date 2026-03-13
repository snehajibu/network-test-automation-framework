import subprocess
import re

import logger
from utils.logger import setup_logger

logger = setup_logger()

class IperfRunner:
    def __init__(self,server_ip):
        self.server_ip = server_ip

    def run_test(self):
        logger.info(f"Running iperf test against {self.server_ip}")
        command = ["iperf3","-c",self.server_ip,"-t","5"]
        result = subprocess.run(command,capture_output=True,text = True)
        logger.info("iperf test completed")
        return result.stdout

    def extract_throughput(self,output):
        match = re.search(r'(\d+\.?\d*)\s+([MG])bits/sec', output)
        if match:
            throughput = float(match.group(1))
            logger.info(f"Detected throughput: {throughput}")
            return throughput

        logger.warning("Throughput not detected")
        return None