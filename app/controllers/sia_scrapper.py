import json
import logging
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException

import time

class SiaScrapper:
    def __init__(self): 
        self.driver = webdriver.Chrome('C:/Users/Jimer/Downloads/chromedriver_win32')
        self.wait = WebDriverWait(self.driver, 10)
        self.all_courses = {'SIACourses': []}

        # URL of the public SIA courses
        url = 'https://sia.unal.edu.co/Catalogo/facespublico/public/servicioPublico.jsf?taskflowId=task-flow-AC_CatalogoAsignaturas'
        self.driver.get(url)

    def scrap(self):
        # Esto por el momento está bug :(
        try:
            # Wait for the element to become present
            nivel_de_estudio_element = self.wait.until(EC.element_to_be_clickable(((By.ID, 'pt1:r1:0:soc1::content'))))

            # Wait for the options to be loaded
            self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#pt1\\:r1\\:0\\:soc1\\:\\:content > option")))

            # Create the Select object and select the option by value
            nivel_de_estudio = Select(nivel_de_estudio_element)
            nivel_de_estudio.select_by_value('0')

            # Wait for the element to become present again
            facultad_element = self.wait.until(EC.element_to_be_clickable(((By.ID, 'pt1:r1:0:soc2::content'))))

            # Wait for the options to be loaded
            self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#pt1\\:r1\\:0\\:soc2\\:\\:content > option")))

            # Create the Select object and select the option by value
            facultad = Select(facultad_element)
            facultad.select_by_value('0')

            # Wait for the element to become present
            plan_de_estudios_element = self.wait.until(EC.element_to_be_clickable(((By.ID, 'pt1:r1:0:soc3::content'))))

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait for the options to be loaded
            self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#pt1\\:r1\\:0\\:soc3\\:\\:content > option")))
                                                                                                    
            # Create the Select object and select the option by value
            plan_de_estudios = Select(plan_de_estudios_element)
            plan_de_estudios.select_by_value('0')
        
        except:
            self.scrap()

        # Wait for the element to become present
        time.sleep(1)
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'af_button_link')))

        # Click the button
        button.click()

        time.sleep(1)

        self.driver.implicitly_wait(30)

        links = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'af_commandLink')))

        for i in range(len(links) - 2):
            desired_link = links[i]
            print('Links: ', len(links), 'Iterción: ', i)
            
            try:
                code = desired_link.text
                desired_link.click()
            except:
                # Re-locate the element
                links = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'af_commandLink')))
                desired_link = links[i]

                code = desired_link.text
                print(code)

                desired_link.click()  # hay un error aca

            time.sleep(1)

            name_element = self.wait.until(EC.presence_of_element_located((By.XPATH, '(//h2)[1]')))
            name = " ".join(name_element.text.split()[:-1])
        
            type_element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.row.detass-tipologia.af_panelGroupLayout')))
            type = " ".join(type_element.text.split()[1:])
            
            credits_element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.row.detass-creditos.af_panelGroupLayout')))
            credits = credits_element.text.split(':')[1] 

            groups = []

            try:
                groups_elements = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'af_showDetailHeader_title-text0')))
                professors_elements = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'strong')))
                horarios_aulas_elements = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.salto margin-l.af_panelGroupLayout')))
                
                for i in range(len(groups_elements)):
                    group = groups_elements[i].text
                    professor = professors_elements[i].text
                    horario_aula = horarios_aulas_elements[i].text
                    
                    groups.append({
                        'group': group,
                        'professor': professor,
                        'horario_aula': horario_aula
                        })
            except:
                print('Error al obtener los grupos')
                
            print(name, code, type, credits + '\n---------------------')

            volver_btn = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'af_button_link')))
            volver_btn.click()

            time.sleep(1)

            # Convert name, code, type, credits to json format
            course = {
                'name': name,
                'code': code,
                'type': type,
                'credits': credits,
                'groups': groups
            }            

            self.all_courses['SIACourses'].append(course)
            print(self.all_courses)

            json_route = 'D:/Users/Usuario/Documents/GitHub/MyLearnCoach/app/data/courses_data.json'

            with open(json_route, 'r') as f:
                data = json.load(f)
                for _course in data['SIACourses']:
                    for key, _course_data in _course.items():
                        #print('probando.... ',type(key), type(code), key, code)
                        print(str(key) == code)
                        if str(key) == code:
                            _course_data = course
                            break
                else: 
                    data['SIACourses'].append({code: course})

            with open(json_route, 'w') as f:
                json.dump(data, f, indent = 4)
                f.close()
    
        return self.all_courses # Aun no funciona :(