from bs4 import BeautifulSoup
from django.conf import settings
import requests
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


class FeedsCrawler():
    """
    
    Crawler class for news
    this class get the link and pars news list with their relative details

    """

    def __init__(self):
        self.req = None
        self.output_list = []
        self.local_time = 'Etc/GMT'

    @staticmethod
    def get_link():
        try:
            req = requests.get(settings.FEEDS_BASE_URL, timeout=settings.DEFAULT_NETWORK_TIMEOUT)
        except:
            req = None
        return req
    
    @staticmethod
    def parse_news_list(req):
        news_list = []
        news = req.json()
        for count, new in enumerate(news['items'][:settings.NUMBER_OF_NEWS_TO_CRAWL]):
            content_html = new['content_html']
            content = BeautifulSoup(content_html, 'html.parser')
            p_tag = content.find('p')
            content = p_tag
            url = new['url']
            title = new['title']
            summary = new['summary']
            date_published = new['date_published']
            author = new['author']['name']
            image = new['image']
            news_list.append({str(count):
                                    {'title': title, 'url': url,
                                    'summary': summary, "date_published": date_published,
                                    "author": author, "content": content, 'image': image
                                }
                            })
        return news_list

    @staticmethod
    def crawl_links():
        req = FeedsCrawler.get_link()
        news_list = FeedsCrawler.parse_news_list(req)
        return news_list