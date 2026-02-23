import subprocess
import sys


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


def enforce_migration_requires_architecture():
    changed_files = get_changed_files()

    migration_changed = any(
        f.startswith("supabase/migrations/") for f in changed_files
    )

    architecture_changed = "ARCHITECTURE.md" in changed_files

    if migration_changed and not architecture_changed:
        print("❌ ERROR: Migration changed but ARCHITECTURE.md was not updated.")
        sys.exit(1)

    print("✅ Rule check passed.")
