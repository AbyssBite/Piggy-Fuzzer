import requests


def send_http(
    url: str,
    method: str = "GET",
    headers: dict = None,
    body: str = "",
    timeout: float = 2.0
):
    """
    Sends an HTTP request with customizable method, headers, and body.

    Args:
        url (str): Full target URL (e.g., http://localhost:8080/test).
        method (str): HTTP method to use (GET, POST, etc.).
        headers (dict): Optional request headers.
        body (str): Optional request body.
        timeout (float): Timeout in seconds.

    Returns:
        dict: Response object summary (status_code, body, headers) or error.
    """
    
    headers = headers or {}
    
    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            data=body.encode() if isinstance(body, str) else body,
            timeout=timeout
        )
        return {
            "status_code": response.status_code,
            "body": response.text,
            "headers": dict(response.headers) 
        }
    except requests.RequestException as e:
        return {"error": str(e)}