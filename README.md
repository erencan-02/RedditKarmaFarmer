# RedditKarmaFarmer

RedditKarmaFarmer is a bot for farming karma points on Reddit.
The bot gains Karma by commenting randomly on submissions.

![alt text](https://i.imgur.com/9PemMZI.png)

## Installation

Use the git clone command to install RedditKarmaFarmer.

```bash
git clone https://github.com/erencan-02/RedditKarmaFarmer.git
```

## Usage

```python
import KarmaFarmer

#Create the options you want
#categories: top,new,hot,rising
subreddits = {
    "PewdiepieSubmissions": ("new", 500),
    "memes": ("new", 500),
    SUBREDDIT: (CATEGORY, AMOUNT_OF_COMMENTS)
}

#Make a new user
user = KarmaFarmer.User("reddit_USERNAME", "reddit_PASSWORD")

#Comment list that the bot can use
comments = ["random comments", "a", "b", "c"]

#You need a webdriver in order to run selenium
options = webdriver.ChromeOptions()
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-infobars")
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(chrome_options=options)

#Initiate the bot and run it
bot = KarmaFarmer.Bot(driver, user, comments, subreddits)
bot.run()

```

## Note
The Webdriver (in this case Chromedriver) has to be in the root directory.

## License
[MIT](https://choosealicense.com/licenses/mit/)

