import socket


def send_udp(ip: str, port: int, data: bytes, timeout: float = 2.0) -> bytes:
    """
    Sends data over a UDP socket and waits for a response.

    Args:
        ip (str): Target IP address.
        port (int): Target UDP port.
        data (bytes): Payload to send.
        timeout (float): Timeout in seconds.

    Returns:
        bytes: Response received or empty bytes on timeout.
    """

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(timeout)
        sock.sendto(data, (ip, port))
        return sock.recv(4096)

    except (socket.timeout, socket.error):
        return b""

    finally:
        sock.close()
