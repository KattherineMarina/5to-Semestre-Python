# Kattherine Guadalupe Marina Cazares 951

import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def request(url):
    r = requests.get(url)
    print(r.status_code)
    return r

def driver():
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--window-size=1200,1200")
    return webdriver.Chrome(service=service, options=options)

def amazon(driver):
    product = input("Ingresa un producto: ")
    num = int(input("¿Cuántos deseas analizar? "))

    driver.get("https://www.amazon.com.mx/?&tag=hydramzkw0mx"
               "-20&ref=pd_sl_7l5x99tvs0_e&adgrpid=58066742059&hvpone="
               "&hvptwo=&hvadid=589380799182&hvpos=&hvnetw=g&hvrand=161339476"
               "67328115426&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9073855"
               "&hvtargid=kwd-10573980&hydadcr=13958_13399146")

    search_box = driver.find_element(By.NAME, "field-keywords")
    search_box.send_keys(product)
    search_box.submit()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "s-main-slot")))
    soup = BeautifulSoup(driver.page_source, "html.parser")

    return soup.find_all("div", attrs={"class": "s-card-container"})[:num]

def dataf(div_list):
    datos = {"nombre": [], "rating": [], "precio": [], "fecha": []}

    for div in div_list:
        nombre = div.find("h2", attrs={"class": "a-size-base-plus a-color-base a-text-normal"})
        rating = div.find("i", attrs={"class": "a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"})
        precio = div.find("span", attrs={"class": "a-price-whole"})
        fecha = div.find("span", attrs={"class": "a-color-base a-text-bold"})
        datos["nombre"].append(nombre.text.strip() if nombre else "")
        datos["rating"].append(rating.text.strip() if rating else "")
        datos["precio"].append(precio.text.strip() if precio else "")
        datos["fecha"].append(fecha.text.strip() if fecha else "")

    return pd.DataFrame(datos)

def main():
    txtbuscar = request("https://www.amazon.com.mx/ref=nav_logo")
    navegador = driver()
    div_list = amazon(navegador)
    df_data = dataf(div_list)
    print(df_data)
    df_data.to_csv("amazon.csv")
    print(navegador.title)
    navegador.quit()

if __name__ == "__main__":
    main()