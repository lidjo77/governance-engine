import sys
import os


def main():
    print("Governance Engine v0.2.0")
    print("Checking for policy.yml...")

    if not os.path.exists("policy.yml"):
        print("❌ ERROR: policy.yml not found in repository root.")
        sys.exit(1)

    print("✅ policy.yml found.")
    print("Engine completed successfully.")
    sys.exit(0)
