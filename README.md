# RedditKarmaFarmer

RedditKarmaFarmer is a bot for farming karma points on Reddit.

## Installation

Use the git clone command to install ReditKarmaFarmer.

```bash
git clone https://github.com/erencan-02/RedditKarmaFarmer.git
```

## Usage

```python
import KarmaFarmer

#Create the options you want
subreddits = {
    "PewdiepieSubmissions": ("new", 500),
    "memes": ("new", 500),
    "meme": ("new", 300)
}

#Make a new user
user = User("reddit_USERNAME", "reddit_PASSWORD")

#Comment list that the bot can use
comments = ["random comments", "a", "b", "c"]

#Initiate the bot and run it
bot = Bot(driver, user, comments, subreddits)
bot.run()

```

## License
[MIT](https://choosealicense.com/licenses/mit/)

