from django.views.generic import ListView, CreateView

from blog.models import Article


class ArticlesListView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    model = Article
    ordering = '-publication_date'
    max_items = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.max_items:
            queryset = queryset[:self.max_items]
        return queryset


class CreateArticleView(CreateView):
    template_name = 'blog/publish.html'
    success_url = '/blog/'
    model = Article
    fields = ['title', 'content', 'featured_image']
