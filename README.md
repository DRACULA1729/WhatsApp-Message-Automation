# WhatsApp Message Automation

This Python script automates sending multiple WhatsApp messages to a specified phone number using the pywhatkit library and pyautogui for keyboard simulation.

## Features

- Reads messages from a text file
- Sends multiple messages sequentially
- Works with WhatsApp Web

## Prerequisites

Before running this script, make sure you have the following installed:

- Python 3.x
- pywhatkit
- pyautogui

You can install the required packages using pip:

```bash
pip install pywhatkit pyautogui
```
# Usage
1.
Clone this repository or download the testScript.py file.
2.
Create a text file named message.txt in the same directory as the script. Each line in this file will be sent as a separate message.
3.
Open testScript.py and modify the following variables:
- file_path: Path to your message.txt file

- phone_number: The recipient's phone number (including country code)
4.
Run the script:
README.md
python testScript.py
5.
5. The script will open WhatsApp Web and start sending messages. Make sure you're logged in to WhatsApp Web on your default browser.

**How it Works**
----------------

1. The script reads all lines from the specified text file.
2. It uses pywhatkit to open WhatsApp Web and send the first message.
3. For subsequent messages, it uses pyautogui to simulate keyboard inputs, typing and sending each message.

**Note**
--------

* Ensure you're logged in to WhatsApp Web before running the script.
* Be cautious when using automation scripts with messaging platforms to avoid violating terms of service or spamming.

**License**
---------

This project is open source and available under the MIT License.

**Contributing**
--------------

Contributions, issues, and feature requests are welcome.

**Author**
---------

DRACULA1729 

