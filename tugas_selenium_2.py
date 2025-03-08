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
    alertButton1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "alertButton")))
    driver.execute_script("arguments[0].scrollIntoView(true);", alertButton1)
    alertButton1.click()
    handle_alert('accept')

    # Timer Alert 5 Detik
    alertButton2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "timerAlertButton")))
    driver.execute_script("arguments[0].scrollIntoView(true);", alertButton2)
    alertButton2.click()
    handle_alert('accept')

    # Confirm Alert (OK)
    alertButton3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "confirmButton")))
    driver.execute_script("arguments[0].scrollIntoView(true);", alertButton3)
    alertButton3.click()
    handle_alert('accept')
    response = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "confirmResult")))
    print("Confirm alert accept - Response Text:", response.text)

    # Confirm Alert (Cancel)
    alertButton3.click()
    handle_alert('dismiss')
    response = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "confirmResult")))
    print("Confirm alert dismiss - Response Text:", response.text)

    # Prompt Alert
    alertButton4 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "promtButton")))
    driver.execute_script("arguments[0].scrollIntoView(true);", alertButton4)
    alertButton4.click()
    handle_alert('accept', input_text="Bersama saya dimari!")
    response = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "promptResult")))
    print("Prompt alert - Response Text:", response.text)

except Exception as e:
    print("Terjadi error:", e)

finally:
    driver.quit()