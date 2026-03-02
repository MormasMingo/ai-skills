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

echo "[INFO] Checking dependencies..."

if ! $PYTHON_CMD -c "import colorama" 2>/dev/null; then
    echo "[INFO] Installing colorama..."
    pip install colorama
fi

if ! $PYTHON_CMD -c "import keyboard" 2>/dev/null; then
    echo "[INFO] Installing keyboard..."
    pip install keyboard
fi

echo "[INFO] Starting Skill Packer..."
$PYTHON_CMD main.py
