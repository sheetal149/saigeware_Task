from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()

try:
    driver.get("https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")

    wait = WebDriverWait(driver, 10)
    
    
    def select_dropdown_by_index(dropdown_id, index):
        dropdown = wait.until(EC.presence_of_element_located((By.ID, dropdown_id)))
        select = Select(dropdown)
        select.select_by_index(0)  
        print(f"{dropdown_id} set to default state!")
        time.sleep(1)
        select.select_by_index(index)
        print(f"{dropdown_id} item '{select.options[index].text}' selected!")
        time.sleep(2)

    select_dropdown_by_index("dropdowm-menu-1", 2)  
    select_dropdown_by_index("dropdowm-menu-2", 2)  
    select_dropdown_by_index("dropdowm-menu-3", 2)  
      

    
    checkbox_section = wait.until(EC.presence_of_element_located((By.ID, "checkboxes")))
    checkboxes = checkbox_section.find_elements(By.XPATH, ".//input[@type='checkbox']")
    for checkbox in checkboxes:
        if checkbox.is_selected():
            checkbox.click()
    print("Checkboxes set to default state!")
    time.sleep(1)
    
    
    option2_checkbox = checkbox_section.find_element(By.XPATH, "//input[@value='option-2']")
    if not option2_checkbox.is_selected():
        option2_checkbox.click()
    print("Checkbox 'Option 2' selected!")
    time.sleep(2)
    
    
    def select_radio_button(form_id, value):
        form = wait.until(EC.presence_of_element_located((By.ID, form_id)))
        radio_button = form.find_element(By.XPATH, f"//input[@value='{value}']")
        radio_button.click()
        print(f"Radio button '{value}' selected in {form_id}!")
        time.sleep(2)
    
    select_radio_button("radio-buttons", "blue")  
    select_radio_button("radio-buttons-selected-disabled", "lettuce")  
    select_dropdown_by_index("fruit-selects", 2)
    
    print("Keeping the browser open for observation...")
    time.sleep(60)  

finally:
    driver.quit()
    print("WebDriver closed.")
