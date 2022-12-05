import os
import requests
from celery import shared_task
from celery.utils.log import get_task_logger
from .feeds_crawler import FeedsCrawler
from .models import News
from common.exceptions import ParseError


logger = get_task_logger(__name__)


def download_image(image_url, image_path):
    if image_url:
        if os.path.exists(image_path):
            os.remove(image_path)
        try:
            news_image_file = requests.get(image_url, allow_redirects=True, timeout=20)
            file_object = open(image_path, 'wb')
            file_object.write(news_image_file.content)
            file_object.close()
        except OSError:
            image_path = ''
    else:
        image_path = ''
    return image_path



@shared_task(queue="news")
def crawl_news():
    news_image_folder = './static/media/cel/img/news/'
    os.makedirs(news_image_folder, exist_ok=True)

    try:
        news_list_dict = FeedsCrawler.crawl_links()
        for count, items in enumerate(news_list_dict):
                item = items.get(str(count))
                news_row, _ = News.objects.get_or_create(title=item['title'])
                image_name = 'image_{}.jpg'.format(news_row.id)
                image_path = news_image_folder + image_name

                #### download image
                image_path = download_image(item['image'], image_path)
                image = image_path.replace('./static/media/', '')
                if not News.objects.filter(title=item['title']).exists():
                    News.objects.create(url=item['url'],
                                            title=item['title'],
                                            content=str(item['content']),
                                            summary=item['summary'],
                                            image=image_path,
                                            date_published=item['date_published'],
                                            author=item['author'])
    except:
        raise ParseError


