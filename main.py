from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

CELL_NUMBER = "123456789"

service = Service("/Users/kumail/Documents/Development/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_TPR=r86400&f_WT=2&geoId=103644278&keywords=python%20developer&location=United%20States")
driver.maximize_window()

sign_in_button = driver.find_element(By.CLASS_NAME, "cta-modal__primary-btn")
time.sleep(3)
sign_in_button.click()

email_input = driver.find_element(By.ID, 'username')
email_input.send_keys("EMAIL")

password_input = driver.find_element(By.ID, 'password')
password_input.send_keys("PASSWORD")

time.sleep(3)

sign_in_button_2 = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in_button_2.click()

time.sleep(3)

all_jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for job in all_jobs:
    print("called")
    job.click()
    time.sleep(2)

    try:
        apply_now_button = driver.find_element(By.CLASS_NAME, 'jobs-apply-button--top-card')
        apply_now_button.click()
        time.sleep(5)

        phone_number = driver.find_element(By.CLASS_NAME, "")
        if phone_number.text == "":
            phone_number.send_keys(CELL_NUMBER)

        submit_button = driver.find_element(By.CSS_SELECTOR, 'footer button')

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")

time.sleep(5)
driver.quit()

