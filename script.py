import os
import random
import subprocess
import time
from datetime import datetime

CODE_FOLDER = "code"

# Verify folder exists
if not os.path.isdir(CODE_FOLDER):
    raise Exception(f"Folder '{CODE_FOLDER}' not found. Run this notebook from the root of the repo.")

# Get all file paths inside the code folder
files = []
for root, dirs, filenames in os.walk(CODE_FOLDER):
    for name in filenames:
        files.append(os.path.join(root, name))


iterations = random.randint(1, 10)
print(f"Running {iterations} iterations...")
for i in range(iterations):
    print(f"\n--- Iteration {i+1}/{iterations} ---")

    # Append a blank line to every file
    for f in files:
        with open(f, "a", encoding="utf-8") as fp:
            fp.write("\n")

    # Create a branch name
    branch_name = f"auto-blankline-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{i}"
    print("Creating branch:", branch_name)

    # Checkout new branch
    subprocess.run(["git", "checkout", "-b", branch_name], check=True)

    # Stage changes
    subprocess.run(["git", "add", "."], check=True)

    # Commit
    subprocess.run(["git", "commit", "-m", f"Iteration {i+1}: appended blank lines"], check=True)

    # Push branch
    subprocess.run(["git", "push", "--set-upstream", "origin", branch_name], check=True)

    # Merge into main
    subprocess.run(["git", "checkout", "main"], check=True)
    subprocess.run(["git", "pull"], check=True)
    subprocess.run(["git", "merge", branch_name], check=True)

    # Push merge to main
    subprocess.run(["git", "push"], check=True)

    print(f"Sleeping 10 seconds...")
    time.sleep(10)