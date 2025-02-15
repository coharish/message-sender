#!/usr/bin/env python
# coding: utf-8

# In[13]:

import csv
import argparse
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pdb
from time import sleep


# Set up argument parser
parser = argparse.ArgumentParser(description='WhatsApp Automation Script')
parser.add_argument('--message', type=str, required=True, help='Message to send')
parser.add_argument('--filepath', type=str, required=False, help='File path to send')
parser.add_argument('--contacts', type=str, required=True, help='Path to contacts CSV file')
args = parser.parse_args()

# Specify the path to the user data directory
user_data_dir = "/Users/coharish/Library/Application Support/Google/Chrome/Default"

# Set up Chrome options to use the user data directory
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")

# Initialize the Chrome driver with the specified options
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver,600)

# Read recipient names and messages from CSV file
recipients = []

with open(args.contacts, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        recipients.append(row)

for recipient in recipients:
    receiver = recipient['name']
    message = args.message.replace("\\n", "\n")  # Replace escaped newlines with actual newlines
    filepath = args.filepath

    print("receiver", receiver)
    try:
        # Locate the search input field
        search_input = wait.until(ec.presence_of_element_located((By.XPATH, '//div[@aria-label="Search"][@role="textbox"]')))

         # Clear the search input field by clicking the clear button if available
        try:
            clear_button = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, '//button[@aria-label="Cancel search"]')))
            clear_button.click()
        except:
            pass

        # Select all text in the search input field and delete it
        search_input.send_keys(Keys.CONTROL + 'a')
        search_input.send_keys(Keys.DELETE)

        # sleep(1)
        # Enter the text into the search input field and press Enter
        search_input.send_keys(receiver + Keys.ENTER)
        print("search_input", receiver)

        # Check if "No chats, contacts or messages found" message is displayed
        try:
            no_results_message = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, '//span[contains(text(), "No chats, contacts or messages found")]')))
            print(f"No contact found for {receiver}. Skipping to next contact.")
            continue
        except:
            pass

    except Exception as e:
        print(f"Error locating search input or entering text: {e}")
        continue

    try:
        # Locate the first element in the search results
        first_element = wait.until(ec.presence_of_element_located((By.XPATH, '//div[@aria-label="Search results."]//div[@role="listitem"][2]')))

        # Click on the first element
        first_element.click()

        if filepath:
            # Upload the file
            attachment = wait.until(ec.presence_of_element_located((By.XPATH, '//button[@title="Attach"]')))
            attachment.click()

            image_box = wait.until(ec.presence_of_element_located((By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')))
            image_box.send_keys(filepath)
            sleep(1)

            send_btn = wait.until(ec.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]')))
            send_btn.click()

            sleep(1)
            print("Image sent to", receiver)
        
        if message:
            # Locate the "Type a message" input field
            message_input = wait.until(ec.presence_of_element_located((By.XPATH, '//div[@aria-label="Type a message"][@role="textbox"]')))

            # Split the message by new lines and send each part separately
            for part in message.split('\n'):
                message_input.send_keys(part)
                message_input.send_keys(Keys.SHIFT, Keys.ENTER)

            # Enter the text into the input field and press Enter
            message_input.send_keys(Keys.ENTER)

            print("Message sent to", receiver)

    except Exception as e:
        print(f"Error sending message to {receiver}: {e}")
        continue

sleep(1)
print("All messages sent.")
# %%
