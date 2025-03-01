from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.minimize_window()

listUrl = [
    "https://www.tiket.com",
    "https://www.tokopedia.com",
    "https://www.orangsiber.com",
    "https://www.idejongkok.com",
    "https://www.kelasotomesyen.com"
]

for url in listUrl:
    driver.get(url)
    sleep(2)
    title = driver.title
    trimmedUrl = url.replace("https://", "").replace("www.", "")
    print(f"{trimmedUrl} - {title}")

driver.quit()