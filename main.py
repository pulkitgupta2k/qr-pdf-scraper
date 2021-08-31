from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, time
import json

driver = webdriver.Chrome('./chromedriver')

data = {}

def get_link(link):
    driver.get(link)
    for i in range(0, 84):
        get_page(i)
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_DOWN)
        html.send_keys(Keys.DOWN)
        html.send_keys(Keys.DOWN)
        sleep(0.5)
        
    

def get_page(pg_no):
    page = driver.find_elements_by_xpath("//div[@class='page']")[pg_no]
    page_html = page.get_attribute('innerHTML')
    page_number = page.get_attribute('data-page-number')
    with open(f"data/{page_number}.html", "w") as f:
        f.writelines(page_html)
    print(page_number)


if __name__ == "__main__":
    get_link("https://qrcodes.pro/JvXJFz")
    driver.close()