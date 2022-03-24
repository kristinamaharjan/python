import time
from selenium import webdriver
import demoji
import os
import csv

fields = ['url','review']

#change the driver details here replace it with your line of chrome driver
driver = webdriver.Chrome("C:\\Users\\Legion\\PycharmProjects\\pythonProject\\chromedriver.exe")

# opening the file containing data of URL for extraction
dir = os.getcwd()
fullpath = os.path.join(dir,"productsurl")
f = open(fullpath, "r")
final_x = f.readlines()
print(final_x)
maindata = []

# extracting the individual url from the file using the loop
for url in final_x:

    #creating try catch block fro error checking
    try:
        #creating a data list
        #using driver to open the individual url
        driver.get(url)
        #adding a pause
        time.sleep(3)

        #scrolling
        driver.execute_script("window.scrollTo(0, 600);")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 800);")


        #using xpath to get the desired html block i.e getting the class content under class item and extracting its text and adding in list
        for x in driver.find_elements_by_xpath(
                '//*[contains(concat( " ", @class, " " ), concat( " ", "item", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "content", " " ))]'):
            data = []
            data.append(url.replace("\n",''))
            texttoadd = x.text

            #filtering emoji
            textfilter =demoji.replace(texttoadd,"")
            data.append(str(textfilter).replace("\n",""))
            maindata.append(data)


    except Exception as e:
        print("Errror"+str(e))

print(maindata)

#writing in csv file
with open('data.csv','w', newline='') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(maindata)

driver.close()