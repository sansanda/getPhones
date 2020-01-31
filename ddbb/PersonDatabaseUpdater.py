from bs4 import BeautifulSoup
import requests
from time import sleep

import urllib.request
import re
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

URL = "https://intranet.imb-cnm.csic.es/intranet/"
USER = 'dsanchez'
PASSWORD = 'mtx.23'

def doLogin(driver, url, user, password):

    driver.get(url)

    login_user = driver.find_element_by_id('login_user')
    login_password = driver.find_element_by_id('login_password')
    login_btn = driver.find_element_by_id('login_btn')
    login_user.send_keys(user)
    login_password.send_keys(password)
    login_btn.click()

    # volvemos a pedir la pagina, esta vez ya logeados
    driver.get(url)
    # print(driver.page_source)

def getWebVisiblePersons_Records(driver):

    personal_list = driver.find_element_by_id('theList')
    visible_personal_list_records = list()

    matchedPersons = \
        personal_list.find_elements_by_xpath("//td[@class='collapsing' and contains(@onclick,'personal.showRecord')]")

    for person in matchedPersons:
        t = str(person.get_attribute('onclick'))
        n = re.findall(r"'(.*?)'", t, re.DOTALL)
        visible_personal_list_records.append(n)

    return visible_personal_list_records


doLogin(driver,URL,USER,PASSWORD)

#go to personal list page
lateral_menu_telefons_item = driver.find_element_by_id('div_12')
telefons_link = lateral_menu_telefons_item.find_element_by_tag_name('a')
telefons_link.click()

#ahora estamos en la página con la tabla de telefonos
#El cnm guarda todas la fichas (records) de los empleados aunque estos esten dados de baja (ya no trabajen en el cnm)
#Esto nos obliga a extraer solo las fichas que se muestran en la web (que no son todas)

visiblePersons_Records = getWebVisiblePersons_Records(driver)

# validIndexes = list()
#
#
# for index in range(1,1500):
#     try:
#         driver.execute_script("personal.showRecord('{}')".format(index))
#         sleep(5)
#         driver.execute_script("personal.list()")
#         validIndexes.append(index)
#     except UnexpectedAlertPresentException:
#         print('Usuario {} NOOOOOOOOO VALIDO'.format(index))
#         continue
#
# print('Lista de Usuarios:')
# print(validIndexes)
# print('Numero total de personas: ',len(validIndexes))


#ahora estamos en la página con la tabla de telefonos
#personal_list = driver.find_element_by_id('theList')
#matchedPersons = personal_list.find_elements_by_xpath("//td[contains(text(), '{}') and @class='collapsing']".format('David'))
# nameOf_matchedPersons = list()
#
# for person in matchedPersons:
#     nameOf_matchedPersons.append(person.text)

#now we have all the names of the persons that match the serach criteria (in this example, name contains David)

# time = 2
# for name in nameOf_matchedPersons:
#     matchedPerson = personal_list.find_element_by_xpath(
#         "//td[contains(text(), '{}') and @class='collapsing']".format(name))
#     matchedPerson.click()
#     sleep(time)
#     personDetails = driver.find_element_by_id('requestsList')
#     sleep(time)
#     tornarAlLlistatBtn = personDetails.find_element_by_xpath("//div[contains(text(), '{}')]".format('Tornar al llistat'))
#     sleep(time)
#     tornarAlLlistatBtn.click()
#     sleep(time)
#     personal_list = driver.find_element_by_id('theList')

# for name in nameOf_matchedPersons:
#     matchedPerson = personal_list.find_element_by_xpath(
#         "//td[contains(text(), '{}') and @class='collapsing']".format(name))
#     sleep(0.5)
#     matchedPerson.click()
#     sleep(2)
#     img = driver.find_element_by_xpath("//*[@id='requestsList']/div/div[2]/div/img")
#     src = img.get_attribute('src')
#     # download the image
#     urllib.request.urlretrieve(src, "captcha.png")
#     sleep(0.5)
#     tornarAlLlistatBtn = driver.find_element_by_xpath("//div[contains(text(), '{}')]".format('Tornar al llistat'))
#     tornarAlLlistatBtn.click()
#     sleep(2)
#     personal_list = driver.find_element_by_id('theList')
#     sleep(0.5)

# rows = driver.find_elements_by_tag_name('tr')
# for row in rows:
#     cols = row.find_elements_by_tag_name('td')
#     for col in cols:
#         print(col.text)



# # defining a params dict for the parameters to be sent to the API
# payload =  {'login':'dsanchez', 'password': 'mtx.23'}
#
# # sending get request and saving the response as response object
# r = requests.post(url=URL, data=payload)
#
# print(r.content)
#
# soup = BeautifulSoup(r.content, 'html.parser')

