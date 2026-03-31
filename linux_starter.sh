#!/bin/bash
echo "--- iovozaurs-AI Launcher for Linux ---"

if ! command -v python3 &> /dev/null
then
    echo "[!] Python 3.12 not found please dowload it (sudo apt install python3.12)."
    exit
fi

echo "[*] Checking and installing requirements from requirements.txt..."
if [ -f "requirements.txt" ]; then
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    echo "[+] Sussecs"
else
    echo "[!] File requirements.txt not found. skip dowload."
fi

echo "[*] Started iovozaurs-AI..."
python3 iovozaurs-ai.py
