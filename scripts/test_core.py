import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from fuzzer.core import fuzz_once

if __name__ == '__main__':
    result = fuzz_once(
        protocol="tcp",
        target={"ip": "127.0.0.1", "port": 8080},
        base_payload=b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
    )
    
    print(result)