from itertools import product
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://test.salesforce.com")
# import webbot
chromedriver_path = "chromedriver"
print(chromedriver_path)
x = ""
print("Do you have list already? Y/N")
x = input();
if x == "N":
  min_len = int(input("Enter minimn length of password: "))
  max_len = int(input("Enter maxium length of password: "))
  counter = 0
  character = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
  
  file_open = open("Wordlist.txt",'w')
  
  for i in range(min_len,max_len+1):
    for j in product(character,repeat=i):
      word = "".join(j)
      file_open.write(word)
      file_open.write('\n')
      counter+=1
  print("Wordlist of {} passwords created".format(counter))
