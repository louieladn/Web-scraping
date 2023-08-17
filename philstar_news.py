from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

app_path = os.path.dirname(sys.executable)

now = datetime.now()
mdy = now.strftime("%m%d%Y")#mmddyy

website = "https://www.philstar.com/"
path = "/home/louie/Downloads/chromedriver-linux64/chromedriver"
#headless
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

Sections = []
Titiles = []
links = []

sections = driver.find_elements(by="xpath", value='//div[@class="carousel__item__section"]')
Titile4 = driver.find_elements(by="xpath", value='//div[@class="carousel__item__title"]')

for section1 in sections:
    for title1 in Titile4:
        section = section1.find_element(by="xpath", value='./a').text
        title = title1.find_element(by="xpath", value='./h2/a').text
        link = title1.find_element(by="xpath", value='./h2/a').get_attribute("href")
        Sections.append(section)
        Titiles.append(title)
        links.append(link)

own_dict = {'Section': Sections, 'Titles': Titiles, 'Links': links}
df_headlines = pd.DataFrame(own_dict)

file_name = f'philstar_news{mdy}.csv'
final_path = os.path.join(app_path, file_name)
df_headlines.to_csv(final_path)
driver.quit()
