import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

data_positive = [
    {
        'title'   : 'Success to Login', 
        'username': 'Admin', 
        'password': 'admin123'
    },
]

data_negative = [
    {
        'title'   : 'Fail to Login, username and password empty', 
        'username': '', 
        'password': ''
    },
    {
        'title'   : 'Fail to Login, username empty', 
        'username': '', 
        'password': 'admin123'
    },
    {
        'title'   : 'Fail to Login, password empty', 
        'username': 'Admin', 
        'password': ''
    },
    {
        'title'   : 'Fail to Login, wrong username', 
        'username': 'AdminSalah', 
        'password': 'admin123'
    },
    {
        'title'   : 'Fail to Login, wrong password', 
        'username': 'Admin', 
        'password': 'admin123Salah'
    },
    {
        'title'   : 'Fail to Login, wrong username and password', 
        'username': 'AdminSalah', 
        'password': 'admin123Salah'
    },
]

@pytest.fixture

def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver  = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    yield driver

    driver.close()

@pytest.mark.parametrize('positive_case', data_positive, ids=[case['title'] for case in data_positive])
def test_login_positive(setup, positive_case):
    username_field = setup.find_element(By.NAME, 'username')
    password_field = setup.find_element(By.NAME, 'password')
    submit_button  = setup.find_element(By.XPATH, "//button[@type='submit']")

    username_field.send_keys(positive_case['username'])
    password_field.send_keys(positive_case['password'])
    submit_button.click()

    dashboard_url   = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
    dashboard_title = "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']"

    get_url   = setup.current_url
    get_title = setup.find_element(By.XPATH, dashboard_title).text

    assert get_url   == dashboard_url
    assert get_title == 'Dashboard'

@pytest.mark.parametrize('negative_case', data_negative, ids=[case['title'] for case in data_negative])
def test_login_negative(setup, negative_case):
    username_field = setup.find_element(By.NAME, 'username')
    password_field = setup.find_element(By.NAME, 'password')
    submit_button  = setup.find_element(By.XPATH, "//button[@type='submit']")

    username_field.send_keys(negative_case['username'])
    password_field.send_keys(negative_case['password'])
    submit_button.click()

    alert_username = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//input[@name='username']/parent::div/following-sibling::span[text()='Required']"
    alert_password = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//input[@name='password']/parent::div/following-sibling::span[text()='Required']"

    if negative_case['username'] == '':
        username_required = WebDriverWait(setup, 10).until(EC.presence_of_element_located((By.XPATH, alert_username)))
        assert username_required.is_displayed()

    if negative_case['password'] == '':
        password_required = WebDriverWait(setup, 10).until(EC.presence_of_element_located((By.XPATH, alert_password)))
        assert password_required.is_displayed()

    if negative_case['username'] != '' and negative_case['password'] != '':
        alert_content = setup.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text
        assert alert_content == 'Invalid credentials'
