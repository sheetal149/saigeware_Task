from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    
    driver.get("https://webdriveruniversity.com/To-Do-List/index.html")

    
    wait = WebDriverWait(driver, 10)
    input_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Add new todo']")))

   
    new_todo = "Study Selenium"
    input_field.send_keys(new_todo)
    input_field.send_keys("\n")  


    time.sleep(2)
    todos = driver.find_elements(By.XPATH, "//ul/li")
    for todo in todos:
        if new_todo in todo.text:
            print(f"New to-do item '{new_todo}' added successfully!")
            break
    else:
        print(f"New to-do item '{new_todo}' not found in the list.")

   
    print("Keeping the browser open for observation...")
    time.sleep(30)  

finally:
    driver.quit()
    print("WebDriver closed.")
