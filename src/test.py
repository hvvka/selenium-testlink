from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get('http://magento.softwaretestingboard.com/')

# get the search textbox
search_field = driver.find_element_by_name('q')
search_field.clear()
# enter search keyword and submit
search_field.send_keys('t-shirt')
search_field.submit()

# en = driver.find_element_by_id('search')
# en.submit()

element = WebDriverWait(driver, 30).until(
    lambda x: x.find_elements_by_xpath("//p[@class='toolbar-amount']"))

# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method <li class="">
products = driver.find_elements_by_xpath("//div[@class='product-item-info']")

# get the number of anchor elements found
print('Found ' + str(len(products)) + ' products:')

# iterate through each anchor element and
# print the text that is name of the product
for product in products:
    print(product.text)

# close the browser window
driver.quit()
