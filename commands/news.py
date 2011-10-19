import feedparser
import random
import urllib


class News:
    """
    Takes given user search terms, searches Google News for them via RSS feeds, and returns a topic link and top news result.
    Requires the Universal Feed Parser python plugin: http://code.google.com/p/feedparser/
    """
    
    rss = "http://news.google.com/news?ned=us&topic=h&output=rss"
    rss_front = "http://news.google.com/news?q="
    rss_back = "&output=rss"
    title = u"No news found (?)"
    url = u" "
    subcommands = ['random', 'latest', 'list']
    
    def __init__(self, bot):
        self.bot = bot
        bot.register_command('news', self.news)
        
    def news(self, data):
        search = data['message'].split(" ", 1)
        if search[0] in self.subcommands:
            search_type = search[0]
            if len(search) < 2:
                search_item = ""
            else:
                search_item = search[1]   
        else:  
            search_type = 'latest'
            search_item = data['message']
            
        if search_item == "": 
            self.bot.say("No news topic given, showing popular news:", data['channel'])
            feed = feedparser.parse(self.rss)
        else:
            q_string = urllib.quote(search_item)
            news_url = self.rss_front + q_string + self.rss_back
            feed = feedparser.parse(news_url)
            
        if search_type == 'random':
            News.random_news(self, data, feed)
        elif search_type == 'list': 
            News.list_feed(self, data, feed)
        else:
            News.latest_news(self, data, feed)
        
    def random_news(self, data, news):
        number = random.randint(0, len(news['entries']) - 1)
        News.parse_feed(self, data, news, number)
    
    def latest_news(self, data, news): 
        News.parse_feed(self, data, news, 0)
        
    def parse_feed(self, data, news, index):
        try:
            self.title = news['entries'][index].title.encode('utf-8')
        except:
            self.bot.say("error: unreadable rss url!!")
        self.url = news['entries'][index].link.encode('utf-8')
        url_parsed = self.url.partition('&url=')
        self.bot.say(self.title + ", " + url_parsed[2], data['channel'])
        
    def list_feed(self, data, news):
        loop = 0
        try:
            self.title = news['entries'][0].title.encode('utf-8')
        except:
            self.bot.say("error: unreadable rss url!!")
        while loop < 3:
            self.title = news['entries'][loop].title.encode('utf-8')
            self.url = news['entries'][loop].link.encode('utf-8')
            url_parsed = self.url.partition('&url=')
            self.bot.say(self.title + ", " + url_parsed[2], data['channel'])
            loop = loop + 1