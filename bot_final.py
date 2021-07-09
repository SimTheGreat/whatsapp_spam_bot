import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/path/to/chromedriver")
contact = input('enter contact as saved on whatsapp')
text = input('enter text')


driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")

#inp_xpath_search is the full xpath to the search section
inp_xpath_search = "/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]"
input_box = driver.find_element_by_xpath(inp_xpath_search)
#enters the contacts name
input_box.send_keys(contact)


#finds the correct contact and clicks on it
selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
time.sleep(2)
selected_contact.click()
time.sleep(2)

#finds the text section
inp_xpath = "/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div/div[2]"
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)

input_box.send_keys(text + Keys.ENTER)#here you it writes and sends the text
time.sleep(2)
