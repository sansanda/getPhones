from bs4 import BeautifulSoup
import requests
from time import sleep

import urllib.request
import re
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException


class CNMEmployeesCaller():

    def __init__(self):
        pass

    def doLogin(self, driver, url, user, password):

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

    def goToPersonalListPage(self, driver):
        # go to personal list page
        # punto de partida https://intranet.imb-cnm.csic.es/
        lateral_menu_telefons_item = driver.find_element_by_id('div_12')
        telefons_link = lateral_menu_telefons_item.find_element_by_tag_name('a')
        telefons_link.click()

    def getWebVisiblePersons_Records(self, driver):

        #Punto de partida es la página https://intranet.imb-cnm.csic.es/intranet/personal/list.php
        visible_personal_list_records = list()

        matchedPersons = \
            driver.find_elements_by_xpath("//td[@class='collapsing' and contains(@onclick,'personal.showRecord')]")

        for person in matchedPersons:
            t = str(person.get_attribute('onclick'))
            n = re.findall(r"'(.*?)'", t, re.DOTALL)
            visible_personal_list_records.append(n[0])

        return visible_personal_list_records


    def getRecordData(self, driver, recordNumber):

        #Punto de partida es la página https://intranet.imb-cnm.csic.es/intranet/personal/list.php
        name,department,group,ubication,phone,mail,photo = "","","","","","",""

        try:

            driver.execute_script("personal.showRecord('{}')".format(recordNumber))
            sleep(6)
            #requestList = driver.find_element_by_xpath("//div[@id='requestsList']")
            #card = requestList.find_element_by_xpath("//div[@class='card']")
            name = driver.find_element_by_xpath("//div[@class='ui dividing header']").text
            #cardDescription = card.find_element_by_xpath("//div[@class='description']")
            cardDescriptionItems = driver.find_elements_by_xpath("//div[@class='item']")

            l = str(cardDescriptionItems[0].text).split('\n')
            if len(l) == 2: department = l[1]
            l = str(cardDescriptionItems[1].text).split('\n')
            if len(l) == 2: group = l[1]
            l = str(cardDescriptionItems[2].text).split('\n')
            if len(l) == 2: ubication = l[1]
            l = str(cardDescriptionItems[3].text).split('\n')
            if len(l) == 2: phone = l[1]
            l = str(cardDescriptionItems[4].text).split('\n')
            if len(l) == 2: mail = l[1]

            driver.execute_script("personal.list()")
            sleep(6)

        except UnexpectedAlertPresentException:
            print('Usuario {} NOOOOOOOOO VALIDO'.format(recordNumber))

        return (name,department,group,ubication,phone,mail,photo)


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

