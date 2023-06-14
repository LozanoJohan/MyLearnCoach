import logging
import json
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

class CourseraScrapper:
    def __init__(self, minimum):
        
        self.minimum = minimum
        self.driver = self.init_chrome()
        self.courses = self.search_coursera(self.minimum)
        self.driver.quit()

    def init_chrome():

        logging.basicConfig(level=logging.INFO)
        ruta= ChromeDriverManager(path='./chromedriver').install()
        options = Options()
        user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        options.add_argument(f"user-agent={user_agent}")
        options.add_argument("--window-size=970,1080")
        options.add_argument("--disable-web-security")
        options.add_argument("disable-extensions")
        options.add_argument("--disable.notifications")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--no-sandbox")
        options.add_argument("--los-level=3")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--no-default-browser-check")
        options.add_argument("--no-first-run")
        options.add_argument("--no-proxy-server")
        options.add_argument("--disable-blink-features=AutomationControlled")

        exp_opt=['enable_automation','ignore-certificate-errors','enable-logging']
        options.add_experimental_option("excludeSwitches", exp_opt)
        prefs ={"profile.default_content_setting_values.notifications":2,"intl.accept_languages":["es-ES","es"], "credentials_enable_service":False}
        options.add_experimental_option("prefs", prefs)


        s = Service(ruta)
        driver = webdriver.Chrome(service=s, options=options)
        driver.set_window_position(0,0)

        return driver
    
    def search_coursera(self, minimo):
        print('Buscando cursos')
        url = "https://www.coursera.org/courses"
        self.driver.get(url)
        courses={'url_courses':[], 'name_courses':[], 'habilidades_courses':[], 'valoracion_courses':[],'reseñas_courses':[], 'durabilidad_courses':[]}
        while len(courses['url_courses']) < minimo:
            cont=0
            for n in range(2):
                cont+=1450
                self.driver.execute_script(f"window.scrollTo(0,{cont});")
                time.sleep(3)
            elementos = self.driver.find_elements(By.CSS_SELECTOR, "div.css-1j8ushu")

            for elemento in elementos:
                try:
                    course= elemento.find_element(By.CSS_SELECTOR, "a").get_attribute('href')
                    name_course= elemento.find_element(By.CSS_SELECTOR, "h2").text
                    habilidades_course= elemento.find_element(By.CSS_SELECTOR, "p").text
                    valoracion_course= elemento.find_element(By.CSS_SELECTOR, 'p.cds-33.css-11uuo4b.cds-35').text
                    data_course= elemento.find_element(By.CSS_SELECTOR, 'p.cds-33.css-dmxkm1.cds-35').text
                    courses['url_courses'].append(course)
                    courses['name_courses'].append(name_course)
                    courses['habilidades_courses'].append(habilidades_course)
                    courses['valoracion_courses'].append(valoracion_course) 
                    courses['reseñas_courses'].append(data_course)
                    print(name_course)
                    print(course)
                    print(habilidades_course)
                    print(f'{valoracion_course} {data_course}')

                except:
                    print('error al encontrar los datos')
        cont=0
        #while len(courses['durabilidad_courses']) < minimo:
        #   cont+=1
        #  elementos = driver.find_elements(By.CSS_SELECTOR, "p.cds-33.css-dmxkm1.cds-35")
        # for elemento in elementos:
            #    if cont >= 25:
            #       if cont%2==0:
            #          try:
            #             data_course= elemento.text
                #            courses['durabilidad_courses'].append(data_course)
                #           print(data_course)
                #      except:
                #         print('error al encontrar la durabilidad')
    #
    #               else: pass
    #          else: pass

                    
        elemento = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Próxima página']")))
        elemento.click()
        return courses  