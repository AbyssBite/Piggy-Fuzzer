import os
import json
from datetime import datetime
import base64

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


def encode_bytes(obj):
    """Recursively convert all byte objects to UTF-8 strings or Base64."""
    if isinstance(obj, bytes):
        try:
            return obj.decode("utf-8")
        except UnicodeDecodeError:
            return base64.b64encode(obj).decode("ascii")

    elif isinstance(obj, dict):
        return {k: encode_bytes(v) for k, v in obj.items()}

    elif isinstance(obj, list):
        return [encode_bytes(i) for i in obj]

    return obj


def log_result(campaign: str, target: dict, result: dict):
    filename = os.path.join(LOG_DIR, f"{campaign.replace(' ', '_')}.log.jsonl")
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "target": target,
        "result": encode_bytes(result),
    }

    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")
        print(f"[✓] Logged result to {filename}")
    except Exception as e:
        print(f"[✗] Failed to write log: {e}")
        print("Entry was:", log_entry)
