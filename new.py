# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import unittest, time, re
wd = webdriver.Firefox()


class TestAddGroup:
    def set_up(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(90)


    def test_add_group(self):
        wd.get("http://localhost/addressbook/addressbook/")
        wd.find_element(by=By.NAME, value="user").click()
        wd.find_element(by=By.NAME, value="user").clear()
        wd.find_element(by=By.NAME, value="user").send_keys("admin")
        wd.find_element(by=By.NAME, value="pass").clear()
        wd.find_element(by=By.NAME, value="pass").send_keys("secret")
        wd.find_element(by=By.XPATH, value="//input[@value='Login']").click()
        wd.find_element(by=By.LINK_TEXT, value ="groups").click()
        wd.find_element(by=By.NAME, value="new").click()
        wd.find_element(by=By.NAME, value="group_name").click()
        wd.find_element(by=By.NAME, value="group_name").clear()
        wd.find_element(by=By.NAME, value="group_name").send_keys("hihoi")
        wd.find_element(by=By.NAME, value="group_header").click()
        wd.find_element(by=By.NAME, value="group_header").clear()
        wd.find_element(by=By.NAME, value="group_header").send_keys("guigiu")
        wd.find_element(by=By.NAME, value="group_footer").click()
        wd.find_element(by=By.NAME, value="group_footer").clear()
        wd.find_element(by=By.NAME, value="group_footer").send_keys("gyugiu")
        wd.find_element(by=By.NAME, value="submit").click()
        wd.find_element(by=By.LINK_TEXT, value="group page").click()
        wd.find_element(by=By.LINK_TEXT, value="Logout").click()

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
