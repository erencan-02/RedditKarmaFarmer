from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random


class Bot:
    def __init__(self, driver, user, comments, options):
        self.driver = driver
        self.user = user
        self.comments = comments
        self.commented_posts = []
        self.options = options

    def login(self):
        self.driver.get("https://www.reddit.com")
        self.driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[2]/div/div[1]/a[1]').click()

        #Selenium fails to recognize xpaths of web elements
        #Login data: user.u_name | user.u_pwd
        _continue = input("Please log in. Note: No further interaction needed. Press any key to continue...")

    def write_comment(self, submission):
        self.driver.get(submission)
        time.sleep(4)

        #Writes comment into the comment section 
        #Note: html element is not an input (span)
        comment_box = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div/span/br')
        random_comment = random.choice(self.comments)
        comment_box.send_keys(random_comment)

        #Submit comment
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/div/div/div[3]/div[1]/button').click()
        time.sleep(5)

    def run(self):
        self.login()
        scraper = Scraper(self.driver, self.options)
        submissions = scraper.get_submissions()

        #Write comment for each submission
        for _submission in submissions:
            try:
                self.write_comment(_submission)
            except:
                continue


class User:
    def __init__(self, u_name, u_pwd):
        self.u_name = str(u_name)
        self.u_pwd = str(u_pwd)


class Scraper:
    def __init__(self, driver, subreddit_options):
        self.driver = driver
        self.subreddit_options = subreddit_options
        self.scraped_post_links = []

    def get_submissions(self):
        for sub_reddit in self.subreddit_options:
            self.driver.get("https://reddit.com/r/{}/{}/".format(sub_reddit, self.subreddit_options[sub_reddit][0]))
            time.sleep(4)

            #Scroll until the whole page is loaded
            while len(self.driver.find_elements_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[5]/div')) < self.subreddit_options[sub_reddit][1] + 50:
                self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                time.sleep(2)
            
            #Get links of submissions and store them
            scraped = []
            i = 1
            while len(scraped) < self.subreddit_options[sub_reddit][1]:
                try:
                    scraped += [self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[5]/div[{}]/div/div/div[2]/div[1]/div[1]/div[1]/a'.format(i)).get_attribute('href')]
                    print('Added {}'.format(scraped[-1]))
                except:
                    print('Error: Could not scrape post. Scraping continues...')
                    i += 1
                    continue
                i += 1
            self.scraped_post_links += scraped
            
        return self.scraped_post_links                        


subreddits = {
    "PewdiepieSubmissions": ("new", 500),
    "memes": ("new", 500),
    "meme": ("new", 300)
}

#Disables browser notifications
options = webdriver.ChromeOptions()
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-infobars")
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(chrome_options=options)

user = User("USERNAME", "PASSWORD")
comments = ["random comments", "a", "b", "c"]
bot = Bot(driver, user, comments, subreddits)
bot.run()
