import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Article


class ArticleModelTests(TestCase):

    def test_was_published_recently_with_future_article(self):
        """
        was_published_recently() returns False for articles whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_article = Article(publish_date = time)
        self.assertIs(future_article.was_published_recently(), False)