from django.test import TestCase
from django.urls import reverse

from blog.models import Article
from blog.views import ArticlesListView


def create_articles(number=1):
    articles = [
        Article(
            title=f'title{n}',
            content=f'content{n}') for n in range(number)]
    Article.objects.bulk_create(articles)


class ArticlesListViewTest(TestCase):
    def test_max_items(self):
        '''The list view returns exactly `max_items` objects in queryset'''

        view = ArticlesListView()
        view.max_items = 10

        create_articles(view.max_items)
        self.assertEqual(view.max_items, len(view.get_queryset()))
