import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fuzzer.protocols.tcp import send_tcp


def test_tcp_send():
    ip = "127.0.0.1"
    port = 8080
    response = send_tcp(ip, port, b"GET / HTTP/1.1\r\nHost: localhost\r\n\t\n")
    assert isinstance(response, bytes)
