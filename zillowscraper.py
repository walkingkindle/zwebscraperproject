import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import lxml
import json
import json
import requests
from bs4 import BeautifulSoup
import pandas
import time



GOOGLE_FORMS_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeUgI37LUjS9h5cGFsiiYGWhO40Mbv3ziIWZoY32fT9R7a3oQ/viewform?usp=sf_link"                  #MY SUPERFICIAL FORM


url = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56035891894531%2C%22east%22%3A-122.30630008105469%2C%22south%22%3A37.6956022862589%2C%22north%22%3A37.85489581746633%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
#random zillow url for San Francisco Apartemtns for rent
headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': 'zguid=23|%24ca6368b9-7b92-4d51-ab67-c2be89065efd; _ga=GA1.2.1460486079.1621047110; _pxvid=7fa13d96-b528-11eb-9860-0242ac120012; _gcl_au=1.1.2025797213.1621047113; __gads=ID=66253ab863481044:T=1621047113:S=ALNI_MZr3mehwm2Wjo7NOrmalVtEcJSXag; __pdst=50987f626deb4767a53b5d8ca2ea406a; _fbp=fb.1.1621047115574.1019382068; _pin_unauth=dWlkPU5EVm1PRGRpTVRBdE5UTTFaUzAwWlRBNExUZzJZall0TWpZMU1HWTBNV0ppWlRkbA; G_ENABLED_IDPS=google; userid=X|3|231a9d744e104379%7C3%7CiEt8bkUx9hWaFeyCeAwN9tHl_T0d0Cq-kynGuEvNYr4%3D; loginmemento=1|c2274ba4a4ad76bbe89263d30695c182e9177b9c40a2691f3054987d66a944be; zjs_user_id=%22X1-ZU158jhpb2klds9_4wzn7%22; zgcus_lbut=; zgcus_aeut=189997416; zgcus_ludi=b44a961b-c7ef-11eb-a48f-96824e7eff50-18999; optimizelyEndUserId=oeu1623111792776r0.8778663892923859; _cs_c=1; WRUIDAWS=3326630244368428; visitor_id701843=248614376; visitor_id701843-hash=4be116fbd77089f953bfb6eaf5996ef92662a6ef7d237d3c49f154ffaf4eaa9295c64fb254b106bdff234e183c94498c01af2aab; __stripe_mid=80125db1-17d1-4fc5-ae37-86b12a68709cf3da6d; g_state={"i_p":1627697570928,"i_l":4}; zjs_anonymous_id=%22ca6368b9-7b92-4d51-ab67-c2be89065efd%22; _gac_UA-21174015-56=1.1626042638.Cj0KCQjwraqHBhDsARIsAKuGZeH8gi095UkXfohW-WWvyLosdmTdL8cfJwgAabYF9hS2XU6JlXqpWLcaAq5SEALw_wcB; _gcl_aw=GCL.1626042640.Cj0KCQjwraqHBhDsARIsAKuGZeH8gi095UkXfohW-WWvyLosdmTdL8cfJwgAabYF9hS2XU6JlXqpWLcaAq5SEALw_wcB; zgsession=1|1edd82e6-372a-4546-bc8b-c2bbadfd29b4; DoubleClickSession=true; fbc=fb.1.1626412984774.IwAR2QM6bzrTskAWN5Sk8UnmPlAxb1HRy1h1GRch888QqXfczHZZWb2vDZfIw; _fbc=fb.1.1626413249162.IwAR2QM6bzrTskAWN5Sk8UnmPlAxb1HRy1h1GRch888QqXfczHZZWb2vDZfIw; _csrf=lV2BBFim7Vy2gFTn--PUt0VA; _gaexp=GAX1.2.w27igyYtRQaAa8XQM3MjDw.18837.2!VDVoDKTnRcyv8f4FAcJ8PA.18915.2!Khnq27RoQmSe5DEusmh5xA.18913.3; _gid=GA1.2.705011419.1630004829; FSsampler=707279376; __CT_Data=gpv=26&ckp=tld&dm=zillow.com&apv_82_www33=26&cpv_82_www33=26&rpv_82_www33=13; OptanonConsent=isIABGlobal=false&datestamp=Fri+Aug+27+2021+12%3A39%3A52+GMT-0600+(Mountain+Daylight+Time)&version=5.11.0&landingPath=NotLandingPage&groups=1%3A1%2C3%3A1%2C4%3A1&AwaitingReconsent=false; _cs_id=41cbdc9c-bb0b-aad9-9521-b1328a65ff77.1623111795.22.1630089665.1630089591.1.1657275795752; utag_main=v_id:01796deff9e3001a59964343177e03079002907100838$_sn:41$_se:2$_ss:0$_st:1630255637884$dc_visit:38$ses_id:1630253822479%3Bexp-session$_pn:1%3Bexp-session$dcsyncran:1%3Bexp-session$tdsyncran:1%3Bexp-session$dc_event:2%3Bexp-session$dc_region:us-east-1%3Bexp-session$ttd_uuid:7b8796ca-44dd-45c9-97d9-bcb642d04cd1%3Bexp-session; JSESSIONID=6CB8C410E0FE216644E8C3A0D0851618; ZILLOW_SID=1|AAAAAVVbFRIBVVsVEklf443J474nftKzJe5PKLD80sujgHvySB7tGcqZunX3BDDH9VwceMqGMTPC54%2F0q4CH%2BfmwsC6P; KruxPixel=true; _derived_epik=dj0yJnU9ai1PSUp1eHZ2Y3J3d0c2NVU1N3BBOFlHbnRBOGFzT0smbj1vLWRISDFwdUNoblN5MjQ4cTVyN213Jm09MSZ0PUFBQUFBR0VzRjRVJnJtPTEmcnQ9QUFBQUFHRXNGNFU; KruxAddition=true; search=6|1632872450375%7Crect%3D40.241821806991595%252C-103.77545313688668%252C39.18758562803622%252C-106.02765040251168%26disp%3Dmap%26mdm%3Dauto%26type%3Dhouse%252Cmultifamily%252Ctownhouse%26fs%3D1%26fr%3D0%26mmm%3D1%26rs%3D0%26ah%3D0%09%0911093%09%09%09%09%09%09; _uetsid=d5e0465006a011ecbe3bd1a0f1c47d01; _uetvid=987e1c70c40a11ebaed8859af36f82fb; _px3=ba45c3df5d5d63d4d9780a102253cd60b21ab52b04778344e332e05474011c21:oCvapPXE6jD0rCXhSf4UjtEC2U956148EDyiWwRFOF8z5vwK63/hC8OWsk09O61g1spnZw64iXApZu1wOmKpyA==:1000:68UzJ5+ar5XwNm61bm41bhSHp8Zp1PfQQlL/5tcqdUIJ3RmA106//vvYGewCCwmln6acqbDAVKgqfB8Th05yX0Cw0TBW7dhfNdeNRjp9bxeLvKqZ56yuW+aVoYYp/zj6MNKv9c16vKlP771xSdCgUTvZ0CDmh7Ng55sHugOHt/jj+2Zmp2WLnuYR4rf7SEndqWBbAyQhhG4BKeyrZyEMpA==; AWSALB=3BIj2fUDeYgoAcLKaZdMkcyTzWSof62v91DQuCssJMyknlpZWcRcVnUU5Me29AcnFcjg1k9H2ehS6N0rSwxo4w8lmEvFCy6hgQfKm1HH8oVoWtpICS36NoLMMxmZ; AWSALBCORS=3BIj2fUDeYgoAcLKaZdMkcyTzWSof62v91DQuCssJMyknlpZWcRcVnUU5Me29AcnFcjg1k9H2ehS6N0rSwxo4w8lmEvFCy6hgQfKm1HH8oVoWtpICS36NoLMMxmZ',
            'referer': 'https://www.google.com/',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'sec-ch-ua-mobile': '?1',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36'
          }
response = requests.get(url=url,headers=headers).text
soup = BeautifulSoup(response,'html.parser')
chrome_driver_path = r'C:\Users\User\AppData\Local\SeleniumBasic\chromedriver.exe'
ser = Service(chrome_driver_path)

#Setting up selenium and Beautiful Soup
driver = webdriver.Chrome(service=ser)
driver.get(GOOGLE_FORMS_URL)

link = soup.find_all(class_='StyledPropertyCardDataWrapper-c11n-8-81-1__sc-1omp4c3-0 fEStTH property-card-data')
javascript_data = soup.find('script', {'data-zrr-shared-data-key': 'mobileSearchPageStore'}).text
json_data = json.loads(javascript_data.split('--')[1])
filter_data = json_data["cat1"]["searchResults"]['listResults']
#parsing the JSON data from the javascript key

all_adresses = []
#[new_item for item in list]
for adress in filter_data:
    real_adress = adress['statusText']
    all_adresses.append(real_adress)
filtered_apartments = [a for a in all_adresses if a != "Apartment for rent"]
print(filtered_apartments)
prices = []
for n in range(len(filtered_apartments)):
    try:
        sample_price = filter_data[n]['units'][0]['price']
    except KeyError:
        pass
    prices.append(sample_price)
print(prices)

all_links = []
for n in range(len(filtered_apartments)):
    link = 'https://www.zillow.com/' + filter_data[n]['detailUrl']
    all_links.append(link)
#getting the pricesn links and adresses from json
print(all_links)

ADDRESS_CLASS = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
PRICE_CLASS = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
LINK_CLASS = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
submit_button = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'



for n in range(len(all_links)):
    time.sleep(5)
    find_adress = driver.find_element(By.XPATH, ADDRESS_CLASS)
    find_adress.click()
    find_adress.send_keys(filtered_apartments[n])
    time.sleep(5)
    find_price = driver.find_element(By.XPATH,PRICE_CLASS)
    find_price.click()
    find_price.send_keys(prices[n])
    time.sleep(5)
    find_link = driver.find_element(By.XPATH, LINK_CLASS)
    find_link.click()
    find_link.send_keys(all_links[n])
    time.sleep(5)
    submit_button_ = driver.find_element(By.XPATH, submit_button)
    submit_button_.click()
    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
    print(n)

#Using Selenium to complete all the forms.