import sys
import os
from governance_engine.policy_loader import load_policy
from governance_engine.rule_engine import enforce_migration_requires_architecture


def main():
    print("Governance Engine v0.4.0")

    if not os.path.exists("policy.yml"):
        print("❌ ERROR: policy.yml not found in repository root.")
        sys.exit(1)

    load_policy()

    enforce_migration_requires_architecture()

    print("Engine completed successfully.")
    sys.exit(0)
