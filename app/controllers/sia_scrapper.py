from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SiaScrapper:
    def __init__(self): 
        self.driver = webdriver.Chrome('C:/Users/Jimer/Downloads/chromedriver_win32')

        # URL of the public SIA courses
        url = 'https://sia.unal.edu.co/Catalogo/facespublico/public/servicioPublico.jsf?taskflowId=task-flow-AC_CatalogoAsignaturas'
        self.driver.get(url)

    def scrap(self):
        # Esto por el momento está bug :(

        # Wait for the element to become present
        nivel_de_estudio_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(((By.ID, 'pt1:r1:0:soc1::content'))))

        # Wait for the options to be loaded
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#pt1\\:r1\\:0\\:soc1\\:\\:content > option")))

        # Create the Select object and select the option by value
        nivel_de_estudio = Select(nivel_de_estudio_element)
        nivel_de_estudio.select_by_value('0')

        # Wait for the element to become present again
        facultad_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(((By.ID, 'pt1:r1:0:soc2::content'))))

        # Wait for the options to be loaded
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#pt1\\:r1\\:0\\:soc2\\:\\:content > option")))

        # Create the Select object and select the option by value
        facultad = Select(facultad_element)
        facultad.select_by_value('0')

        # Wait for the element to become present
        plan_de_estudios_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(((By.ID, 'pt1:r1:0:soc3::content'))))
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for the options to be loaded
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#pt1\\:r1\\:0\\:soc3\\:\\:content > option")))
                                                                                                
        # Create the Select object and select the option by value
        plan_de_estudios = Select(plan_de_estudios_element)
        plan_de_estudios.select_by_value('0')

        # Wait for the element to become present
        time.sleep(3)
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'af_button_link')))

        # Click the button
        button.click()

        # Continue with scraping the data from the new page that loads

        # Find all <a> elements on the page and click them
        #wait 5 seconds for the page to load
        time.sleep(5)

        self.driver.implicitly_wait(30)
        body = self.driver.find_element(By.TAG_NAME, 'body')
        print(body.text)

        links = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'a')))
        links[0].click()

        return '' # Aun no funciona :(
