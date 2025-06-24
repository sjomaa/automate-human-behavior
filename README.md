# Automate Human Behavior

This project uses Python and Selenium to simulate human-like browsing and email actions for automation or testing purposes.

## What the Script Does
- Logs into LinkedIn with a test account (replace credentials in `main.py`).
- Simulates scrolling and browsing on LinkedIn.
- Opens Gmail and simulates sending an email (requires manual login or automation setup).

## Requirements
- Python 3.7+
- Google Chrome browser
- ChromeDriver (matching your Chrome version, in your PATH)
- Selenium Python package

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/sjomaa/automate-human-behavior.git
   cd automate-human-behavior
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Download ChromeDriver:**
   - Download from: https://sites.google.com/chromium.org/driver/
   - Place the `chromedriver` executable in a directory included in your system PATH.

## Usage
1. **Edit `main.py`**
   - Replace `test_username` and `test_password` with your LinkedIn test account credentials.
2. **Run the script:**
   ```sh
   python main.py
   ```

## Notes
- For Gmail automation, you may need to log in manually or set up automation for Google login (not included for security reasons).
- The script simulates human-like delays and scrolling to avoid detection as a bot.

## Disclaimer
This script is for testing purposes only. Do not use it to violate the terms of service of any website.