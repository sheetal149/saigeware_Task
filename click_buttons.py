from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("https://webdriveruniversity.com/Click-Buttons/index.html")
wait = WebDriverWait(driver, 10)


def close_dialog():
    try:
        dialog = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-dialog")))
        close_button = dialog.find_element(By.CSS_SELECTOR, ".close")
        close_button.click()
    except Exception as e:
        print(f"No dialog box to close: {e}")


button1 = wait.until(EC.element_to_be_clickable((By.ID, "button1")))
button1.click()
time.sleep(2)
close_dialog()


button2 = wait.until(EC.element_to_be_clickable((By.ID, "button2")))
driver.execute_script("arguments[0].click();", button2)
time.sleep(2)
close_dialog()


button3 = wait.until(EC.element_to_be_clickable((By.ID, "button3")))
ActionChains(driver).move_to_element(button3).click().perform()
time.sleep(2)
close_dialog()


time.sleep(15)
driver.quit()
