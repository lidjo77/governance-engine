import sys
import os
from governance_engine.policy_loader import load_policy
from governance_engine.rule_engine import enforce_documents


def main():
    print("Governance Engine v0.5.0")

    if not os.path.exists("policy.yml"):
        print("❌ ERROR: policy.yml not found in repository root.")
        sys.exit(1)

    policy = load_policy()

    enforce_documents(policy)

    print("Engine completed successfully.")
    sys.exit(0)
