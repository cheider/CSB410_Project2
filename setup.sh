(#!/usr/bin/env bash)
set -euo pipefail

# Configuration
ENV_FILE="environment.yml"
ENV_NAME="project2"

echo "Creating default folders..."
mkdir -p outputs outputs/models outputs/checkpoints outputs/figures outputs/logs data/processed

if command -v conda >/dev/null 2>&1; then
	echo "Found conda. Creating/updating environment from ${ENV_FILE} (name=${ENV_NAME})..."
	# Try to create; if it fails (already exists) try update
	if ! conda env create -f "${ENV_FILE}" -n "${ENV_NAME}"; then
		echo "Environment may already exist — attempting to update it instead..."
		conda env update -f "${ENV_FILE}" -n "${ENV_NAME}"
	fi
	echo "Environment ready. Activate with:"
	echo "  conda activate ${ENV_NAME}"
else
	echo "ERROR: conda not found in PATH. Install Miniconda/Anaconda and re-run this script." >&2
	exit 1
fi

cat <<'USAGE'

Next steps (examples):

- Activate the environment:
	conda activate project2

- Run the primary notebook interactively:
	jupyter notebook main.ipynb
	# or
	jupyter lab

- Execute the notebook headless and save outputs:
	jupyter nbconvert --to notebook --execute main.ipynb --output outputs/main_executed.ipynb

- Run tests:
	pytest tests/

- (Optional) Use papermill to parameterize runs:
	pip install papermill
	papermill main.ipynb outputs/main_run.ipynb -p some_param value

Notes:
- This script assumes a POSIX shell (Git Bash, WSL, macOS, Linux). On Windows CMD/PowerShell, run the commands manually or use WSL/Git Bash.
- Large model artifacts should be stored externally (Google Drive, S3) or tracked with Git LFS.

USAGE

echo "Setup complete."

