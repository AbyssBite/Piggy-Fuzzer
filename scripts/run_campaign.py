import time
import yaml
import sys
import os

# Fix path so we can import from fuzzer/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fuzzer.core import fuzz_once
from fuzzer.logger import log_result
from fuzzer.monitor import monitor


def run_campaign(config_path: str):
    with open(config_path) as f:
        config = yaml.safe_load(f)

    print("[*] Loaded config:", config)

    campaign_name = config.get("campaign", "UnnamedCampaign")
    base_payload = bytes(
        config["payload"].encode("utf-8").decode("unicode_escape"), "latin1"
    )
    iterations = config.get("iterations", 10)
    mutation_count = config.get("mutation_count", 5)
    rate_limit = config.get("rate_limit", 0.1)

    for i in range(iterations):
        print(f"[{i + 1}/{iterations}] Fuzzing...")
        try:
            monitored = monitor(
                fuzz_once,
                protocol=config["protocol"],
                target=config["target"],
                base_payload=base_payload,
                mutation_count=mutation_count,
            )

            # Console debug output
            print(
                f"[{i + 1}] Duration: {monitored['duration']}s | Timeout: {monitored['timeout']} | Crash: {monitored['crash']}"
            )

            # Save to logs
            log_result(campaign_name, config["target"], monitored)

        except Exception as e:
            print(f"[{i + 1}] Error during fuzzing: {str(e)}")

        time.sleep(rate_limit)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/run_campaign.py <path_to_config.yaml>")
        sys.exit(1)

    run_campaign(sys.argv[1])
