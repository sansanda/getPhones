from bs4 import BeautifulSoup
import requests
from time import sleep

import urllib.request
import re
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException


class CNMEmployeesDataMiner():

    def __init__(self, url, user, password, employeesDataFilePath, employeesDataFileName, employeesImagesFolder):
        self.url = url
        self.user = user
        self.password = password
        self.employeesFilePath = employeesDataFilePath
        self.employeesFileName = employeesDataFileName
        self.employeesImagesFolder = employeesImagesFolder

    def doLogin(self, driver):

        driver.get(self.url)

        login_user = driver.find_element_by_id('login_user')
        login_password = driver.find_element_by_id('login_password')
        login_btn = driver.find_element_by_id('login_btn')
        login_user.send_keys(self.user)
        login_password.send_keys(self.password)
        login_btn.click()

        # volvemos a pedir la pagina, esta vez ya logeados
        driver.get(self.url)
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
            sleep(5)
            #requestList = driver.find_element_by_xpath("//div[@id='requestsList']")
            #card = requestList.find_element_by_xpath("//div[@class='card']")
            name = driver.find_element_by_xpath("//div[@class='ui dividing header']").text
            #cardDescription = card.find_element_by_xpath("//div[@class='description']")
            cardDescriptionItems = driver.find_elements_by_xpath("//div[@class='item']")

            image_element = driver.find_element_by_xpath("//*[@id='requestsList']/div/div[2]/div/img")
            image = image_element.get_attribute('src')
            urllib.request.urlretrieve(image, self.employeesFilePath+self.employeesImagesFolder + name + ".png")

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
            sleep(5)

        except UnexpectedAlertPresentException:
            print('Usuario {} NOOOOOOOOO VALIDO'.format(recordNumber))

        return (name,department,group,ubication,phone,mail,photo)
