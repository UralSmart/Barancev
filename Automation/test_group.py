# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabili

class TestLicreategrouplo():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_licreategrouplo(self):
    self.driver.get("http://localhost/addressbook/")
    self.driver.set_window_size(1226, 1020)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
    self.driver.find_element(By.LINK_TEXT, "Группы").click()
    self.driver.find_element(By.NAME, "new").click()
    self.driver.find_element(By.NAME, "group_name").click()
    self.driver.find_element(By.NAME, "group_name").send_keys("fghfhfgh")
    self.driver.find_element(By.NAME, "group_header").click()
    self.driver.find_element(By.NAME, "group_header").send_keys("fhgfhfghfg")
    self.driver.find_element(By.NAME, "group_footer").click()
    self.driver.find_element(By.NAME, "group_footer").send_keys("hfhthfht")
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.LINK_TEXT, "group page").click()
    self.driver.find_element(By.LINK_TEXT, "Выйти").click()
  
