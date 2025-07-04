import socket

def send_tcp(ip: str, port: int, data: bytes, timeout: float = 2.0) -> bytes:
    '''
    Sends data over a TCP connection and receives the response.
    
    Args:
        ip (str): Target IP address.
        port (int): Target TCP port.
        data (bytes): Payload to send.
        timeout (float): Socket timeout in seconds.
        
    Returns:
        bytes: Response received or empty bytes in timeout.
    '''
    
    try:
        with socket.create_connection((ip, port), timeout=timeout) as sock:
            sock.sendall(data)
            sock.settimeout(timeout)
            return sock.recv(4096)
    except (socket.timeout, socket.error):
        return b''