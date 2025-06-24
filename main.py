import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def random_sleep(min_sec=300, max_sec=1200):
    sleep_time = random.randint(min_sec, max_sec)
    print(f"Sleeping for {sleep_time} seconds (coffee break!)")
    time.sleep(sleep_time)

# Set up the WebDriver (make sure chromedriver is in your PATH)
driver = webdriver.Chrome()

try:
    # 1. Open LinkedIn and log in to a test account
    driver.get("https://www.linkedin.com/login")
    random_sleep(5, 10)
    # Enter username
    username_field = driver.find_element("id", "username")
    username_field.send_keys("test_username")  # Replace with your test username
    # Enter password
    password_field = driver.find_element("id", "password")
    password_field.send_keys("test_password")  # Replace with your test password
    # Submit login form
    password_field.send_keys(Keys.RETURN)
    random_sleep(5, 10)
    # Simulate scrolling after login
    for _ in range(3):
        driver.find_element("tag name", "body").send_keys(Keys.PAGE_DOWN)
        random_sleep(2, 5)

    random_sleep(10, 20)

    # 2. Open Gmail and simulate sending an email
    driver.get("https://mail.google.com/")
    random_sleep(15, 25)
    # You would need to log in manually or handle login automation
    # Simulate clicking Compose (if logged in)
    try:
        compose_button = driver.find_element("xpath", "//div[text()='Compose']")
        compose_button.click()
        random_sleep(2, 4)
        to_field = driver.find_element("name", "to")
        to_field.send_keys("recipient@example.com")
        subject_field = driver.find_element("name", "subjectbox")
        subject_field.send_keys("Automated HR Email")
        body_field = driver.find_element("xpath", "//div[@aria-label='Message Body']")
        body_field.send_keys("Hello, this is a test email sent by an automated HR agent.")
        random_sleep(2, 4)
        send_button = driver.find_element("xpath", "//div[text()='Send']")
        send_button.click()
    except Exception as e:
        print("Could not send email automatically. Please log in and try again.")

    random_sleep(10, 20)

finally:
    driver.quit()