from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    
    driver.get("https://webdriveruniversity.com/Click-Buttons/index.html")
    
    wait = WebDriverWait(driver, 10)
    
    def close_dialog():
        try:
            dialog = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-dialog")))
            close_button = dialog.find_element(By.CSS_SELECTOR, ".close")
            close_button.click()
            print("Dialog box closed!")
        except Exception as e:
            print("No dialog box to close. {e}")   

    # --- Regular Click ---
    print("Waiting for Regular Click button to be present...")
    button1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@id='button1']")))
    print("Regular Click button is visible. Clicking now...")
    button1.click()
    print("Regular Click button clicked!")
    time.sleep(2)  
    close_dialog()  

   # --- JavaScript Click ---
    print("Waiting for JavaScript Click button to be present...")
    button2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#button2")))
    print("JavaScript Click button is visible. Clicking now...")
    driver.execute_script("arguments[0].click();", button2)
    print("JavaScript Click button clicked!")
    time.sleep(2)  
    close_dialog()  

    # --- Action Move & Click ---
    print("Waiting for Action Move & Click button to be present...")
    button3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#button3")))
    print("JavaScript Click button is visible. Clicking now...")
    driver.execute_script("arguments[0].click();", button3)
    print("JavaScript Click button clicked!")
    time.sleep(2)  
    close_dialog()  
    
    print("Keeping the browser open for  observation...")
    time.sleep(40)  

finally:
    
    driver.quit()
    print("WebDriver closed.")
