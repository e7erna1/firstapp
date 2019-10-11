from django.http.response import HttpResponse
from django.template import loader

from article.models import Article, Comments


def articles(request):
    template = loader.get_template('articles.html')
    context = {'articles': Article.objects.all()}
    return HttpResponse(template.render(context, request))


def article(request, article_id=1):
    template = loader.get_template('article.html')
    context = {'article': Article.objects.get(id=article_id),
               'comments': Comments.objects.filter(
                   comments_article_id=article_id)}
    return HttpResponse(template.render(context, request))
