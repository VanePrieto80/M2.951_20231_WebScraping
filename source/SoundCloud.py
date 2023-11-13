# -*- coding: utf-8 -*-
"""
Created 6-XI-2023

@author: Sergi Benito Ivern
         Vanesa Prieto Prieto
"""

# S'importen les llibreries a utilitzar
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

from cerca_SoundCloud import CERCA, N, NOM_ARXIU
import requests
import sys
import time
import os


# Es declaren les variables que s'utilitzaran durant l'execució del programa
URL = "https://soundcloud.com"


# Es declaren les diferent funcions que s'executaran
def get_robot_txt(url):
    """Llegeix el fitxer robots.txt """ 
    
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    
    req = requests.get(path + "robots.txt", data=None)
    return req.text


def iniciar_chrome():
    """Inicia Chrome amb els paràmetres indicats i retorna driver"""
    
    # Instal·la la versió chromedriver corresponent a la versió del navegador Chrome.
    versio_chromedriver = ChromeDriverManager().install()
    
    # Opcions de Chrome
    options = Options()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}") # Es defineix user_agent personalitzat
    options.add_argument("--headless") # Obre Chrome sense obrir la finestra
    options.add_argument("--start-maximized") # S'indica que la ventana de Chrome serà maximizada
    options.add_argument("--disable-web-security") # Deshabilita la política de la web
    options.add_argument("--disable-extensions") # Deshabilita les extensions de Chrome
    options.add_argument("--disable-notifications") # Bloqueja les notificacions de Chrome
    options.add_argument("--ignore-certificate-errors") # Ignora l'avís "La vostra connexió no és privada"
    options.add_argument("--no-sandbox") # Deshabilita el mode sandbox
    options.add_argument("--log-level=3") # No mostrar les operacions pel terminal
    options.add_argument("--allow-running-insecurite-content") # Desactiva l'avís " Contingut no segur"
    options.add_argument("--no-default-browser-check") # S'evita la comprovació del navegador per defecte
    options.add_argument("--no-first-run") # S'evita les tasques en executar la primera vegada Chrome
    options.add_argument("--no-proxy-server") # Es fan connexions directes
    options.add_argument("--disable-blink-features=AutomationController") # Codifica que no s'està utilitzant Selenium
    
    # Paràmetres a ometre a l'inici de CHROMEDRIVER
    exp_opt = [
        'enable-automation', # No mostrar notificació "Software automatitzat"
        'ignore-certificate-errors' # Ignorar errors de certificats
        ]
    options.add_experimental_option("excludeSwitches", exp_opt)
    
    #Paràmetres que defineixen preferències a CHROMEDRIVER
    prefs = {
        "profile.default_content_setting_values.notifications" : 2, # No permetre notificacions
        "intl.accept_languages" : ["es-ES", "es"] # Definiu l'idioma de Chrome
        }
    options.add_experimental_option("prefs", prefs)
    
    driver = webdriver.Chrome(versio_chromedriver , options=options)
    return driver


def cookies_soundcloud():
    """Acepta les cookies de la web SoundCloud"""
    driver.get(URL + '\soundcloud')
    try:
        element = wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Acepto')]")))
    except TimeoutException:
        print('ERROR: Element cookies no disponible')
        return "Error"
    element.click()


def cerca():
    """Realitza la cerca dins la web segons paràmetre fixat a arxiu cerca.py"""
    try:
        element_busqueda = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "input[type='search']")))
    except TimeoutException:
        print('ERROR: Element cerca no disponible')
        return "Error"
    element_busqueda.send_keys(CERCA)
    element_click = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    element_click.click()
    element_click = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "a[class='g-nav-link sc-link-primary searchOptions__navigationLink sc-text-h4']")))
    element_click.click()
    element_click = wait.until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/div/ul/li[5]/a")))
    element_click.click()
    
    
def descarrega_dades():
    """Es realitza la descàrrega de les dades que es volen obtenir"""
    
    dictlist = []
    print('Ha començat la descarrega de dades\n')
    
    for n in range(N):
        # Es realitza SCROLL
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        
    # Es seleccionen les dades
    elements = driver.find_elements(By.CSS_SELECTOR, "div.searchItem")
    for element in elements:
            
        userStatsDict={}
            
        try:
            title_album = element.find_element(By.CSS_SELECTOR, "a.soundTitle__title").text
        except:
            title_album = 'none'
                
        try:
            artist_album = element.find_element(By.CSS_SELECTOR, "span.soundTitle__usernameText").text
        except:
            artist_album = 'none'
                
        try:
             tracks_album = element.find_element(By.CSS_SELECTOR, "a.compactTrackList__moreLink").text
        except:
             tracks_album = 'none'
               
        try:
            time_posted = element.find_element(By.CSS_SELECTOR, "time.relativeTime").get_attribute("datetime")
        except:
            time_posted = 'none'
                
        try:
            any_album = element.find_element(By.CSS_SELECTOR, "span.sc-font-light").text
        except:
            any_album = 'none'
                 
        try:
            likes = element.find_element(By.CSS_SELECTOR, "button.sc-button-like").text
        except:
            likes = 'none'
                
        try:
            repost = element.find_element(By.CSS_SELECTOR, "button.sc-button-repost").text
        except:
            repost = 'none'
                
        try:
            url_album = element.find_element(By.CSS_SELECTOR, "a.sound__coverArt").get_attribute("href")
        except:
            url_album = 'none'
                
            
        userStatsDict['title_album']=title_album
        userStatsDict['artist_album']=artist_album
        userStatsDict['tracks_album']=tracks_album
        userStatsDict['time_posted']=time_posted
        userStatsDict['any_album']=any_album
        userStatsDict['likes']=likes
        userStatsDict['repost']=repost
        userStatsDict['url_album']=url_album
        dictlist.append(userStatsDict)            
    print('Ha finalitzar la descarrega de dades\n')
    
    # Es crea l'arxiu 
    path = os.path.dirname(os.path.abspath(__file__))
    print("S'ha obert l'arxiu\n")
    arxiu = open(path + NOM_ARXIU, "w+", encoding="utf-8")
    claus = [] 
    for clau in userStatsDict: 
        claus.append(clau)
    
    for i in range(len(claus)): 
        arxiu.write(str(claus[i]) + ";"); 
    arxiu.write("\n");
    
    for i in range(len(dictlist)): 
        for j in range(len(claus)): 
            arxiu.write(str(dictlist[i][claus[j]]) + ";");
        arxiu.write("\n");
        
    arxiu.close()
    print("S'ha tancat l'arxiu\n")
    

##################################MAIN#########################################


if __name__ == '__main__':
    
    # Es mostra per la terminal la URL a realitzar scraping
    print("\nEs mostra la URL a realitzar scraping:")
    print(URL, '\n')
    
    # Es mostra per la terminal l'arxiu robots.txt
    print("\nEs mostra l'arxiu robots.txt:")
    print(get_robot_txt(URL), '\n')
    
    # S'inicia Chrome
    driver = iniciar_chrome()
    print("S'ha iniciat Chrome\n")
    
    # Es mostra per la terminal l'UserAgent
    print("Es mostra l'UserAgent:")
    agent = driver.execute_script("return navigator.userAgent") 
    print(agent, '\n')
    
    # S'Acepten les cookies de SoundClound
    wait = WebDriverWait(driver, 10)
    cookies = cookies_soundcloud()
    if cookies == "Error":
        input("Pulsa ENTER per sortir")
        driver.quit()
        sys.exit(1)
    else:
        print("S'han acceptat les cookies de SoundCloud\n")
    
    # Es realitza la busqueda
    wait = WebDriverWait(driver, 10)
    cerca = cerca()
    if cerca == "Error":
        input("Pulsa ENTER per sortir")
        driver.quit()
        sys.exit(1)
    else:
        print("S'ha realitzat la cerca de " + CERCA + " a SoundCloud\n")
    
    # Es realitza la descarrega de dades
    time.sleep(3)
    descarrega = descarrega_dades()

    # Finalitza l'Scraping, es tanca Chrome i finalitza el programa.
    driver.quit()
    print("Ha finalitzar l'scraping i s'ha tancat Chrome")
