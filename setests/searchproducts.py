#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver

# create a new Firefox Session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
#driver.get("http://demo.magentocommerce.com/")
driver.get("https://www.google.com/")

# get the search textbox
search_field = driver.find_element_by_name("q")
search_field.clear()

#enter search keyword and submit
search_field.send_keys("Skyrim")
search_field.submit()

# get all the anchor elements which have product name displayed
# currently on result page using find elements_by_xpath method
products = driver.find_elements_by_xpath("//h3[@class='r']/a")

# get the number of anchor elements found
print("Found " + str(len(products)) + " products: ")

#iterate through each anchor elements and print the text that is 
# name of product
for product in products:
    print(product.text)

# close the browser window
driver.quit()
