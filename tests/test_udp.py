import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fuzzer.protocols.udp import send_udp

def test_udp_send():
    ip = '127.0.0.1'
    port = 9999
    response = send_udp(ip, port, b"fuzz-test")
    assert isinstance(response, bytes)