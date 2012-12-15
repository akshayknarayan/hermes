import feedparser
import urllib.request
import re

class post(object):
    def __init__(self, contents, title, author, time, link):
        self.contents = contents
        self.title = title
        self.author = author
        self.time = time
        self.link = link
    def printout(self):
        print(self.title)
        print(str(self.author) + " " + str(self.time))
        print(str(self.contents))
        print(self.link)
        
class feed(object):
    def __init__(self, url_str):
        self.url = url_str
        self.feed = self.get_data()
        self.posts = []
        self.get_posts()
        self.title = self.feed.feed.title
    def get_data(self):
        u = urllib.request.urlopen(self.url)
        fp = open('feed.xml', 'wb')
        fp.write(u.read())
        fp.close()
        return feedparser.parse('feed.xml')
    def re_format(self, text):
        text = re.sub('\n','', text)
        text = re.sub('</p>','\n', text)
        text = re.sub('<(.*?)>','',text)
        text = re.sub('&mdash;', "--", text)
        text = re.sub('&amp;', '&', text)
        text = re.sub('&hellip;', '...', text)
        text = re.sub('&nbsp;', ' ', text)
        return text.strip()
    def get_posts(self):
        if self.feed.bozo == 1:
            return None
        for entry in self.feed.entries:
            title = entry.title
            author = entry.author
            time = entry.published
            content = self.re_format(entry.content[0].value)
            link = entry.link
            self.posts.append(post(content, title, author, time, link))
    def printout(self):
        print(self.title)
        print(self.url)
        for post in self.posts:
            post.printout()
            print()

#fd_verge = feed('http://www.theverge.com/rss/index.xml')
#fd_verge.printout()