import subprocess
import sys
import fnmatch


def get_changed_files():
    try:
        result = subprocess.run(
            ["git", "diff", "origin/main...HEAD", "--name-only"],
            capture_output=True,
            text=True,
            check=True,
        )
        files = result.stdout.strip().split("\n")
        return [f for f in files if f]
    except Exception as e:
        print(f"❌ ERROR: Failed to get changed files: {e}")
        sys.exit(1)


def matches_pattern(file, patterns):
    for pattern in patterns:
        if fnmatch.fnmatch(file, pattern):
            return True
    return False


def enforce_documents(policy):
    changed_files = get_changed_files()
    documents = policy.get("documents", {})

    for name, doc in documents.items():
        required_file = doc.get("file")
        patterns = doc.get("required_on_changes", [])
        level = doc.get("level", "blocking")

        trigger = any(
            matches_pattern(f, patterns) for f in changed_files
        )

        if trigger:
            if required_file not in changed_files:
                message = f"Document '{required_file}' must be updated when changing matching files for {name}."

                if level == "blocking":
                    print(f"❌ ERROR: {message}")
                    sys.exit(1)
                else:
                    print(f"⚠️ WARNING: {message}")

    print("✅ All document rules passed.")
