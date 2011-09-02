import feedparser


class Woot:
    """
    Returns the current item on sale at Woot.com, according to the woot rss.
    """
    
    rss = "http://www.woot.com/blog/rss.aspx"
    sale = u"No woots? Something's wrong."
    sale_date = "None"
    wootoff_status = ". "

    def __init__(self, bot):
        self.bot = bot
        bot.register_command('woot', self.woot)
	
    def woot(self, data):
        self.bot.say('The current sale at www.woot.com is ' + self.get_woot() + self.wootoff_status, data['channel'])

    def get_woot(self):
        woot = feedparser.parse(self.rss)
        first_found = False
        for item in woot['entries']:
            if item.category == 'Woot':
                if first_found == False:
                    self.sale = item.title.encode('utf-8')
                    first_found = True
                    self.sale_date = item.updated[0:2]
                else:
                    if self.sale_date == item.updated[0:2]:
                        self.wootoff_status = ". Woot-Off Detected!"
                    else:
                        self.wootoff_status = ". "
                    break
        return self.sale

    def check_woot(self):
        check_sale = self.get_woot()
        if check_sale != self.sale:
            self.sale = check_sale
            self.bot.say('The current sale at www.woot.com is ' + self.sale, data['channel'])
        else:
            pass
