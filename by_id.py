from selenium import webdriver

#making driver
driver = webdriver.Chrome("C:\\Users\\Legion\\PycharmProjects\\pythonProject\\chromedriver.exe")

#passing url to crawl
url = "https://www.daraz.com.np/products/digicom-wired-headphone-dg-w7-i105611049-s1029419496.html?spm=a2a0e.searchlist.list.1.703c1f1cEEKn7N&search=1"
#asking driver to get url
driver.get(url)
#getting element with that id
title = driver.find_element_by_id("module_product_price_1").text
print(title)
driver.close()

