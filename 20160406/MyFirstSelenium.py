# coding = utf-8


from selenium import webdriver
# from selenium.webdriver.common.keys import keys
from selenium.webdriver.common import keys

driver = webdriver.Firefox()
driver.get('http://www.python.org')
assert 'python' in driver.title
elem = driver.find_element_by_name('q')
elem.send_keys('pycon')
elem.send_keys(keys.RETURN)
assert 'No results found.' not in driver.page_source
driver.close()