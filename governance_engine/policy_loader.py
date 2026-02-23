import yaml
import sys


def load_policy():
    try:
        with open("policy.yml", "r") as f:
            policy = yaml.safe_load(f)
    except Exception as e:
        print(f"❌ ERROR: Failed to load policy.yml: {e}")
        sys.exit(1)

    if not isinstance(policy, dict):
        print("❌ ERROR: policy.yml must be a valid YAML object.")
        sys.exit(1)

    if "version" not in policy:
        print("❌ ERROR: policy.yml missing 'version' field.")
        sys.exit(1)

    if policy["version"] != 2:
        print("❌ ERROR: Unsupported policy version. Expected version: 2")
        sys.exit(1)

    if "documents" not in policy:
        print("❌ ERROR: policy.yml missing 'documents' section.")
        sys.exit(1)

    print("✅ policy.yml structure is valid (v2).")
    return policy
