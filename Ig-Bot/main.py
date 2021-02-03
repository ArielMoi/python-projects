from selenium import webdriver
import os
import time

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome('chromedriver.exe')
        self.base_url = 'https://www.instagram.com'
        self.login()


    def login(self):
        self.driver.get('{}/accounts/login/#'.format(self.base_url))
        time.sleep(1)
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)

        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button/div').click()

        time.sleep(2.5)
    #    self.driver.get(self.base_url)

    def nav_user(self, user):
    #    time.sleep(2)
        self.driver.get('{}/{}'.format(self.base_url, user))


    def follow_user(self, user):
        self.nav_user(user)

        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]
        follow_button.click()

if __name__ == '__main__':

    ig_bot = InstagramBot('temp', 'temp')
    print(ig_bot.username)
  #  ig_bot.nav_user('garyvee')
    ig_bot.follow_user('garyvee')