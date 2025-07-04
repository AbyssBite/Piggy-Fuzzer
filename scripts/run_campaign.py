import time
import yaml
import base64

from fuzzer.core import fuzz_once
from fuzzer.logger import log_result


def run_campaign(config_path: str):
    with open(config_path) as f:
        config = yaml.safe_load(f)

    print("[*] Loaded config:", config)

    base_payload = bytes(
        config["payload"].encode("utf-8").decode("unicode_escape"), "latin1"
    )
    iterations = config.get("iterations", 10)
    mutation_count = config.get("mutation_count", 5)
    rate_limit = config.get("rate_limit", 0.1)

    for i in range(iterations):
        print(f"[{i + 1}/{iterations}] Fuzzing...")
        try:
            result = fuzz_once(
                protocol=config["protocol"],
                target=config["target"],
                base_payload=base_payload,
                mutation_count=mutation_count,
            )
            print(f"[{i + 1}] Result:", result)
            log_result(config["campaign"], config["target"], result)
        except Exception as e:
            print(f"[{i + 1}] Error:", str(e))
        time.sleep(rate_limit)


if __name__ == "__main__":
    import sys

    run_campaign(sys.argv[1])