This repository is about a [Twitter bot](https://twitter.com/Berlinhouse1).
It will search rental appartments (Mietwohnung) in Berlin (district Charlottenburg, or somewhere else). Then automatically post on Twitter the average, min, and max of found results.

References:
* Search on Immobilienscout24:
  * https://github.com/balzer82/immoscraper, using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  * https://github.com/asmaier/ImmoSpider, using [Scrapy](https://scrapy.org/doc/)
* Host server for bot:
  * [Heroku via Github](https://github.com/tranvohuy/simple_twitter_bot_Heroku_via_Github)
  * [Heroku via HerokuCLI](https://github.com/tranvohuy/simple_twitter_bot)
* Twitter
  * [Twitter API](https://developer.twitter.com/en/docs.html)
  * [Tweepy](http://docs.tweepy.org/en/v3.5.0/getting_started.html), a python library to work with Twitter
