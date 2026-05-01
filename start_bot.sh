#!/bin/bash

# Navigate directory
# Get directoryd
cd "$(dirname "$0")"

echo "[HexVoid] Starting bot migration sequence..."

# Activate vir env
if [ -d "venv" ]; then
    echo "[HexVoid] Activating virtual environment..."
    source venv/bin/activate
else
    echo "[HexVoid] Virtual environment not found. Running without venv..."
fi

# Run
echo "[HexVoid] Launching bot.py"
exec python3 bot.py
