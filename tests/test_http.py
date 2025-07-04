import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fuzzer.protocols.http import send_http

def test_http_send():
    url = "https://httpbin.org/post"
    result = send_http(
        url=url,
        method="POST",
        headers={"Content-Type": "application/json"},
        body='{"username": "admin", "password": "fuzz"}'
    )
    
    assert isinstance(result, dict)
    assert "status_code" in result or "error" in result