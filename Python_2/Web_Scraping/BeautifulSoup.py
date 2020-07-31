import requests
from bs4 import BeautifulSoup

url = 'http://www.blog.pythonlibrary.org/'


def get_articles():
    """
    Get the articles from the front page of the blog
    """
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.findAll('h1')

    articles = {i.a['href']: i.text.strip()
                for i in pages if i.a}

    for article in articles:
        s = '{title}: {url}'.format(title=articles[article].encode('utf-8'), url=article)
        print(s)

    return articles


if __name__ == '__main__':
    articles = get_articles()


import requests

from bs4 import BeautifulSoup

url = 'https://twitter.com/mousevspython'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
tweets = soup.findAll('li', 'js-stream-item')
for item in range(len(soup.find_all('p', 'TweetTextSize'))):
    tweet_text = tweets[item].get_text().encode('utf-8')
    print(tweet_text)
    dt = tweets[item].find('a', 'tweet-timestamp')
    print('This was tweeted on ' + str(dt))