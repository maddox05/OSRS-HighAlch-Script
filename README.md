# OSRS-HighAlch-Script

This is a simple Python script that automates the high alching process in the popular game Old School RuneScape (OSRS).

## Features

- Reads a hotkey from a `hotkey.txt` file and uses it to perform the high alching action.
- Introduces random delays between each action to mimic human-like behavior and avoid detection by the game's anti-bot system.
- Continuously loops the high alching process until the script is manually stopped.

## Requirements

- Python 3.x
- `pyautogui` library (install with `pip install pyautogui`)

## Usage

1. Create a `hotkey.txt` file in the same directory as the script and add the hotkey you want to use for high alching (e.g., "e").
2. Run the script using the following command:
   python main.py
3. The script will start high alching items in your inventory automatically. You can let it run in the background while you do other tasks.

## Disclaimer

This script is intended for personal use only. Automated scripts or bots that interact with OSRS may be against the game's terms of service and could result in your account being banned. Use this script at your own risk.

## License

This project is licensed under the [MIT License](LICENSE).
