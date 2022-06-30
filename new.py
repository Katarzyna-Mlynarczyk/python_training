# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import unittest, time, re
wd = webdriver.Firefox()


class Test_Add_Group(unittest.TestCase):
    def set_up(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(90)

    def test_add_group(self):
        self.open_home_page(wd)
        self.login(wd)
        self.open_groups_page(wd)
        self.create_group(wd)
        self.return_to_groups_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element(by=By.LINK_TEXT, value="Logout").click()

    def return_to_groups_page(self, wd):
        wd.find_element(by=By.LINK_TEXT, value="group page").click()

    def create_group(self, wd):
        # init group creation
        wd.find_element(by=By.NAME, value="new").click()
        # fill group form
        wd.find_element(by=By.NAME, value="group_name").click()
        wd.find_element(by=By.NAME, value="group_name").clear()
        wd.find_element(by=By.NAME, value="group_name").send_keys("hihoi")
        wd.find_element(by=By.NAME, value="group_header").click()
        wd.find_element(by=By.NAME, value="group_header").clear()
        wd.find_element(by=By.NAME, value="group_header").send_keys("guigiu")
        wd.find_element(by=By.NAME, value="group_footer").click()
        wd.find_element(by=By.NAME, value="group_footer").clear()
        wd.find_element(by=By.NAME, value="group_footer").send_keys("gyugiu")
        # submit group creation
        wd.find_element(by=By.NAME, value="submit").click()

    def open_groups_page(self, wd):
        wd.find_element(by=By.LINK_TEXT, value="groups").click()

    def login(self, wd):
        wd.find_element(by=By.NAME, value="user").click()
        wd.find_element(by=By.NAME, value="user").clear()
        wd.find_element(by=By.NAME, value="user").send_keys("admin")
        wd.find_element(by=By.NAME, value="pass").clear()
        wd.find_element(by=By.NAME, value="pass").send_keys("secret")
        wd.find_element(by=By.XPATH, value="//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tear_Down(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
