from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import base64
from PIL import Image
from io import BytesIO


url = 'https://worldspinner.com/heraldry/device_editor/'
chrome_options = Options()
chrome_options.add_argument("--headless")  # no window
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

f = open("blasons_png.txt", 'a')
i = 11638
while i <= 15000:
    i = i+1
    while True:
        try:
            img_b64 = WebDriverWait(driver, 20).until(
                lambda driver: driver.find_element_by_css_selector('img.device-preview').get_attribute('ng-src'))[22:]
            break
        except:
            pass
    nom = driver.find_element_by_css_selector('em.ng-binding').get_attribute('innerHTML')[1:-1]

    im = Image.open(BytesIO(base64.b64decode(img_b64)))
    im.save("images/"+str(i)+".png", 'PNG')
    f.write(str(i) + ';' + nom + '\n')
    print(nom)
    print(str(i) + "\n")

    while True:
        driver.find_element_by_class_name('brass-button-small').click()
        #  wait end of js function trigged by the click
        try:
            WebDriverWait(driver, 20).until(
                lambda driver: driver.find_element_by_css_selector('em.ng-binding').get_attribute('innerHTML')[1:-1] != nom)
            break
        except:
            pass

