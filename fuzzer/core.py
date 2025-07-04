from fuzzer.inputs.mutation import mutate
from fuzzer.protocols.tcp import send_tcp
from fuzzer.protocols.udp import send_udp
from fuzzer.protocols.http import send_http

def fuzz_once(protocol: str, target: dict, base_payload: bytes, mutation_count: int=5):
    """
    Executes a single fuzzing attempt using the selected protocol.
    
    Args:
        protocol: Protocol to use (tcp, udp, or http).
        target: Contains IP/port for TCP/UDP, or URL and method for HTTP.
        base_payload: Valid payloads to mutate.
        mutation_count: Number of mutations per input.
        
    Returns:
        dict: Result of the send operation (response or error).
    """
    mutated_payload = mutate(base_payload, mutation_count)
    
    if protocol == "tcp":
        return {
            "payload": mutated_payload.hex(),
            "response": send_tcp(target["ip"], target["port"], mutated_payload)
        }
        
    elif protocol == "udp":
        return {
            "payload": mutated_payload.hex(),
            "response": send_udp(target["ip"], target["port"], mutated_payload)
        }
    elif protocol == "http":
        raw_result = send_http(
            url=target["url"],
            method=target.get("method", "POST"),
            headers=target.get("headers", {}),
            body=mutated_payload
        )
        
        status = raw_result.get("status_code", 0)
        status_group = "other"

        if 200 <= status < 300:
            status_group = "2xx ✅"
        elif 400 <= status < 500:
            status_group = "4xx ⚠️"
        elif 500 <= status < 600:
            status_group = "5xx ❌"

        return {
            "payload": mutated_payload.decode(errors="replace"),
            "response": raw_result,
            "status_group": status_group
        }

        
    else:
        raise ValueError(f"Unsupported protocol: {protocol}")