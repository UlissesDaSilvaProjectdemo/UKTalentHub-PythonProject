from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementsList():

    def testListOfElements(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        radioButtonsList = driver.find_elements(
            By.XPATH, "//input[contains(@type,'radio') and contains(@name,'cars')]")
        size = len(radioButtonsList)
        print("Size of the list: " + str(size))

        for radioButton in radioButtonsList:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(2)

    def testUnOrderlist(self):

        baseUrl = "https://www.bbc.co.uk/sport"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        skillsSection = self.driver.find_element_by_xpath("//*[@id='sp-nav-flyout'']/div[1]/ul[1]")
        skillsList = skillsSection.find_elements_by_tag_name("li")
        for skill in skillsList:
            skill.find_elemdnt_by_xpath("//*[@id='sp-nav-flyout']/div[1]/ul[1]/li[5]").click()

ff = WorkingWithElementsList()
ff.testListOfElements()