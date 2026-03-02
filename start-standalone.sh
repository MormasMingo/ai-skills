#!/bin/bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

EXECUTABLE="$SCRIPT_DIR/dist/skill-packer"

if [ ! -f "$EXECUTABLE" ]; then
    echo "[ERROR] Executable not found: $EXECUTABLE"
    echo "[INFO] Please run build.sh first to build the executable"
    exit 1
fi

echo "[INFO] Starting Skill Packer..."
"$EXECUTABLE"
