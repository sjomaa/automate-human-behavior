import time
import random
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def coffee_break(min_sec=300, max_sec=1200):
    sleep_time = random.randint(min_sec, max_sec)
    print(f"Sleeping for {sleep_time} seconds (coffee break!)")
    time.sleep(sleep_time)

def selenium_sleep(min_sec=2, max_sec=5):
    sleep_time = random.randint(min_sec, max_sec)
    print(f"Sleeping for {sleep_time} seconds (selenium wait)")
    time.sleep(sleep_time)

# Set up the WebDriver (make sure chromedriver is in your PATH)
driver = webdriver.Chrome()

# Get credentials from environment variables or use defaults
test_username = os.environ.get("LINKEDIN_USERNAME", "test")
test_password = os.environ.get("LINKEDIN_PASSWORD", "test")

try:
    # 1. Open LinkedIn and log in to a test account
    driver.get("https://www.linkedin.com/login")
    selenium_sleep(5, 10)
    # Enter username
    username_field = driver.find_element("id", "username")
    username_field.send_keys(test_username)  # Uses env or default
    # Enter password
    password_field = driver.find_element("id", "password")
    password_field.send_keys(test_password)  # Uses env or default
    # Submit login form
    password_field.send_keys(Keys.RETURN)
    selenium_sleep(5, 10)
    # Simulate scrolling after login
    for _ in range(3):
        driver.find_element("tag name", "body").send_keys(Keys.PAGE_DOWN)
        selenium_sleep(2, 5)

    # Simulate random actions after login
    actions = [
        lambda: driver.find_element("tag name", "body").send_keys(Keys.PAGE_DOWN),
        lambda: driver.find_element("tag name", "body").send_keys(Keys.PAGE_UP),
        lambda: driver.back(),
        lambda: driver.forward(),
        lambda: driver.refresh(),
        # Example: click on the 'My Network' tab if present
        lambda: driver.find_element("xpath", "//a[contains(@href, '/mynetwork')]").click() if driver.find_elements("xpath", "//a[contains(@href, '/mynetwork')]") else None,
        # Example: click on the 'Jobs' tab if present
        lambda: driver.find_element("xpath", "//a[contains(@href, '/jobs')]").click() if driver.find_elements("xpath", "//a[contains(@href, '/jobs')]") else None,
    ]
    for _ in range(100):
        action = random.choice(actions)
        try:
            action()
        except Exception as e:
            print(f"Action failed: {e}")
        selenium_sleep(2, 5)

    coffee_break()

    # 2. Open Gmail and simulate sending an email
    driver.get("https://mail.google.com/")
    selenium_sleep(15, 25)
    # You would need to log in manually or handle login automation
    # Simulate clicking Compose (if logged in)
    try:
        compose_button = driver.find_element("xpath", "//div[text()='Compose']")
        compose_button.click()
        selenium_sleep(2, 4)
        to_field = driver.find_element("name", "to")
        to_field.send_keys("recipient@example.com")
        subject_field = driver.find_element("name", "subjectbox")
        subject_field.send_keys("Automated HR Email")
        body_field = driver.find_element("xpath", "//div[@aria-label='Message Body']")
        body_field.send_keys("Hello, this is a test email sent by an automated HR agent.")
        selenium_sleep(2, 4)
        send_button = driver.find_element("xpath", "//div[text()='Send']")
        send_button.click()
    except Exception as e:
        print("Could not send email automatically. Please log in and try again.")

    coffee_break()

finally:
    driver.quit()