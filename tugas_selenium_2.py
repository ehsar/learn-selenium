from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def handle_alert(alert_type = 'accept', input_text = None):
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    print(f"Alert Text: {alert.text}")
    
    if input_text:
        alert.send_keys(input_text)
    
    if alert_type == 'accept':
        alert.accept()
        print("Alert accept (OK)")

    elif alert_type == 'dismiss':
        alert.dismiss()
        print("Alert dismiss (Cancel)")

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver  = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)

try:
    driver.get("https://demoqa.com/alerts")

    # Simple Alert
    alert_button1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "alertButton")))
    driver.execute_script("arguments[0].scrollIntoView(true);", alert_button1)
    alert_button1.click()
    handle_alert('accept')

    # Timer Alert 5 Detik
    alert_button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "timerAlertButton")))
    driver.execute_script("arguments[0].scrollIntoView(true);", alert_button2)
    alert_button2.click()
    handle_alert('accept')

    # Confirm Alert (OK)
    alert_button3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "confirmButton")))
    driver.execute_script("arguments[0].scrollIntoView(true);", alert_button3)
    alert_button3.click()
    handle_alert('accept')
    response_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "confirmResult")))
    print("Confirm alert accept - Response Text:", response_text.text)

    # Confirm Alert (Cancel)
    alert_button3.click()
    handle_alert('dismiss')
    response_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "confirmResult")))
    print("Confirm alert dismiss - Response Text:", response_text.text)

    # Prompt Alert
    alert_button4 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "promtButton")))
    driver.execute_script("arguments[0].scrollIntoView(true);", alert_button4)
    alert_button4.click()
    handle_alert('accept', input_text="Bersama saya dimari!")
    response_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "promptResult")))
    print("Prompt alert - Response Text:", response_text.text)

except Exception as e:
    print("Terjadi error:", e)

finally:
    driver.quit()