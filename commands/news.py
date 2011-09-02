import feedparser
import random
import urllib


class News:
    """
    Takes given user search terms, searches Google News for them via RSS feeds, and returns a topic link and top news result.
    """
    
    rss = "http://news.google.com/news?ned=us&topic=h&output=rss"
    rss_front = "http://news.google.com/news?q="
    rss_back = "&output=rss"
    title = u"No news found (?)"
    url = u" "
    
    def __init__(self, bot):
        self.bot = bot
        bot.register_command('news', self.news)
        
    def news(self, data):
        if data['message'] == "": 
            self.bot.say("No news topic given, showing random headline:", data['channel'])
            News.random_news(self, data)
        else:
            News.news_search(self, data)
            
            
    def random_news(self, data):
        news = feedparser.parse(self.rss)
        number = random.randint(0, len(news['entries']) - 1)
        News.parse_feed(self, data, news, number)
    
    def news_search(self, data):
        q_string = urllib.quote(data['message'])
        news_url = self.rss_front + q_string + self.rss_back
        news = feedparser.parse(news_url)
        News.parse_feed(self, data, news, 1)
        
    def parse_feed(self, data, news, index):
        try:
            self.title = news['entries'][index].title.encode('utf-8')
        except:
            self.bot.say("unreadable rss url!")
        self.url = news['entries'][index].link.encode('utf-8')
        url_parsed = self.url.partition('&url=')
        self.bot.say(self.title + ", " + url_parsed[2], data['channel'])