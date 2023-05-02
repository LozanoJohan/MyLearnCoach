from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('C:/Users/Jimer/Downloads/chromedriver_win32')

# Replace 'url' with the actual URL of the web page
url = 'https://sia.unal.edu.co/Catalogo/facespublico/public/servicioPublico.jsf?taskflowId=task-flow-AC_CatalogoAsignaturas'
driver.get(url)

# Wait for the element to become present
nivel_de_estudio_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(((By.ID, 'pt1:r1:0:soc1::content'))))

# Wait for the options to be loaded
WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#pt1\\:r1\\:0\\:soc1\\:\\:content > option")))

# Create the Select object and select the option by value
nivel_de_estudio = Select(nivel_de_estudio_element)
nivel_de_estudio.select_by_value('0')

# Wait for the element to become present again
facultad_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(((By.ID, 'pt1:r1:0:soc2::content'))))

# Wait for the options to be loaded
WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#pt1\\:r1\\:0\\:soc2\\:\\:content > option")))

# Create the Select object and select the option by value
facultad = Select(facultad_element)
facultad.select_by_value('0')

# Wait for the element to become present
plan_de_estudios_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(((By.ID, 'pt1:r1:0:soc3::content'))))

# Wait for the options to be loaded
WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#pt1\\:r1\\:0\\:soc3\\:\\:content > option")))
                                                                                         
# Create the Select object and select the option by value
plan_de_estudios = Select(plan_de_estudios_element)
plan_de_estudios.select_by_value('0')

# Wait for the element to become present
button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'af_button_link')))

# Click the button
button.click()

# Continue with scraping the data from the new page that loads

# Find all <a> elements on the page and click them
#wait 5 seconds for the page to load

driver.implicitly_wait(30)
body = driver.find_element(By.TAG_NAME, 'body')
print(body.text)

# links = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'a')))
# links[0].click()
