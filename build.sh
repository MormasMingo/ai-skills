#!/bin/bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "[INFO] Checking Python installation..."
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "[ERROR] Python is not installed"
    exit 1
fi

PYTHON_CMD=$(command -v python3 || command -v python)

echo "[INFO] Installing build dependencies..."
pip install pyinstaller

echo "[INFO] Building executable..."
pyinstaller --onefile --name skill-packer --console main.py

echo "[INFO] Build complete!"
echo "[INFO] Executable location: dist/skill-packer"
