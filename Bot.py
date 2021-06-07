from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(6)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(6)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + hashtag + '&src=typed_query')
        time.sleep(6)
        for i in range(1, 3):
            bot.execute_script(
                'window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
            tweets = bot.find_elements_by_css_selector(
                '.css-4rbku5.css-18t94o4.css-901oao.r-1re7ezh.r-1loqt21.r-1q142lx.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-3s2u2q.r-qvutc0')
            links = [elem.get_attribute('href') for elem in tweets]
            for link in links:
                bot.get(link)
                try:
                    bot.find_element_by_xpath(
'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[4]/div/div/section/div/div/div[6]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div[3]/div/div/div[1]/svg').click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(60)

yo = TwitterBot('gaffox', '159ropox')
yo.login()
yo.like_tweet('crypto')
