from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import numpy as np


#define ave pts array needed 
avePtsArray = []

def click_trios():

    # Construct the XPath for the desired button with text '三排'
    button_xpath = "//button[contains(text(), '三排')]"

    # Find the button element
    button = driver.find_element(By.XPATH, button_xpath)

    # Click the button to open the options
    button.click()









#drop down menu gots to be a clicked
def click_drop(option_text, element_tag):
    # Replace 'your-option-text' with the text content of the option you want to click
    #option_text = "2023永劫无间职业联赛春季赛"

    # Replace 'your-element-tag' with the HTML tag of the option element (e.g., 'li')
    #element_tag = "li"

    # Construct the XPath for the desired option
    option_xpath = f"//{element_tag}[contains(text(), '{option_text}')]"

    # Wait for the dropdown to be clickable
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".el-select.match-select.compete-select"))
    )

    # Click the dropdown to open the options
    dropdown.click()

    # Find and click the specific option
    option_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, option_xpath))
    )
    option_element.click()

def find_header(table_box):
        # Extract data from the table-box
    row = table_box.find_element(By.CLASS_NAME, "tr")
    td_elements = row.find_elements(By.CLASS_NAME, "td")
        
    scrape_header(td_elements)
    rows = table_box.find_elements(By.CLASS_NAME, "tr")[1:]
    for row in rows:
            
                    # Find the specific div with class 'td' and print its text
        td_elements = row.find_elements(By.CLASS_NAME, "td")
        
        scrape_header(td_elements)

def scrape_header(td_elements):
        rank = td_elements[0].text
        print(f"Rank: {rank}")
        

        team_name = td_elements[1].text
        team_name = team_name.replace(" " , "")
        team_name = team_name.strip()
        print(f"Team: {team_name}")

        total_points = td_elements[2].text
        print(f"Total Points: {total_points}")
        avePts = float(total_points)/12
        global avePtsArray
        avePtsArray.append(avePts)
        print(f"Average Points per Game: {avePts}")
        print("")
        print("")

def find_body(body):    
            # Extract data from the table-box
    rows = body.find_elements(By.CLASS_NAME, "tr")
    for row in rows:
        td_elements = row.find_elements(By.CLASS_NAME, "td")
        for element in td_elements:
            elementT = element.text
            print(f"{elementT}")

def scrape_body():
    print()












# URL of the webpage
url = "https://www.yjwujian.cn/match/#/event-data"

# Initialize Safari driver
driver = webdriver.Safari()

# Navigate to the URL
driver.get(url)

# Locate and click the button
click_trios()
click_drop("2023永劫无间职业联赛春季赛", "li")

try:
    # Wait for the table-wrap to be present on the page
    table_wrap = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "table-wrap"))
    )

    # Scroll down to trigger the loading of the table-box
    driver.execute_script("arguments[0].scrollIntoView();", table_wrap)
    
    # Wait for a moment to ensure the content is loaded
    time.sleep(2)


    # Now try to locate the table-box
    table_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "table-body"))
    )

    find_header(table_box)

    body = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "scroll-area.scroll-style"))
    )
    #find_body(body)
    for table in body:
        print("found table")
        
    

finally:
    avePtsArray = np.array(avePtsArray)# Close the browser window
    print(avePtsArray)
    driver.quit()
