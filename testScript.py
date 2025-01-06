import pywhatkit as kit
import time
import pyautogui

# Function to read all lines from a text file
def read_all_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# Function to send WhatsApp messages sequentially
def send_whatsapp_messages(phone_number, messages):
    # Open WhatsApp Web and send the first message
    kit.sendwhatmsg_instantly(phone_number, messages[0].strip())
    time.sleep(10)  # Wait for WhatsApp Web to load

    # Send the remaining messages using keyboard inputs
    for message in messages[1:]:
        pyautogui.write(message.strip())  # Type the message
        pyautogui.press('enter')  # Send the message
        time.sleep(2)  # Add a small delay between messages

if __name__ == "__main__":
    file_path = 'message.txt'  # Replace with your text file path
    phone_number = '+919876543210'  # Replace with the recipient's phone number
    
    # Read all lines from the file
    messages = read_all_lines_from_file(file_path)
    
    # Send all messages sequentially
    send_whatsapp_messages(phone_number, messages)