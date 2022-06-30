from selenium import webdriver
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

chrome_options = Options()
chrome_options.add_argument("--headless")

country_name = []
loc_name = []
pm25 = []
country_1 = []

def run():
    global country_list, country_name
    driver.get("https://openaq.org/")
    sleep(3)
    driver.find_element("xpath",'''//*[@id="page-prime-nav"]/div[1]/div/ul/li[2]/a''').click()
    sleep(3)
    driver.find_element("xpath",'''//*[@id="nav-group-open-data"]/div/ul/li[1]/a''').click()
    sleep(3)
    driver.find_element("xpath",'''//*[@id="app-container"]/div/main/section/div/div[1]/div/div[1]/div/a[2]''').click()
    sleep(3)
    driver.find_element("xpath",'''/html/body/div[6]/div/div/ul/label[6]''').click()
    sleep(3)
    driver.find_element("xpath",'''//*[@id="app-container"]/div/main/section/div/div[1]/div/div[1]/div/a[1]''').click()
    sleep(3)

    country = driver.find_element("xpath",'''/html/body/div[5]/div/div/ul''').text
    # Converting it to list of strings
    country_name = country.split('\n')

    countries = driver.find_element("xpath",'''/html/body/div[5]/div/div/ul''')
    country_list = countries.find_elements(By.CLASS_NAME,'drop__menu-item')


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
sleep(2)

i=0
for i in range(20):
    run()

    country_list[i].click()
    sleep(3)
    try:
        artical_1 = driver.find_element(By.CLASS_NAME,'''inpage__results''')
        artical_2 = artical_1.find_elements(By.TAG_NAME,'article')

        if len(artical_2)!=0:
            #location_name = driver.find_element("xpath",'/html/body/div[1]/div/main/section/div/div[3]/div[2]/article[1]/div/header/div[1]/h1').text
            #location_name = location_name.split('\n')

            artical_2[0].find_element(By.CLASS_NAME,'cfa-go').click()
            sleep(3)

            pm25_value = driver.find_element("xpath",'''/html/body/div[1]/div/main/section/div/div[2]/article[2]/div/div/ul/li/h1''').text

            country_1.append(country_name[i])
            #loc_name.append(location_name[0])
            pm25.append(pm25_value)
            #print(pm25_value)
            #print(location_name[0])

    except Exception as e:
        print(e)

driver.quit()

df = pd.DataFrame()
df['Country'] = country_1
#df['Location']=loc_name
df['PM2.5'] = pm25
df.to_excel('df.xlsx',index=False)