from django.shortcuts import render
from django.http import HttpResponse
from blog.article.models import Article
from django.http import Http404


# Create your views here.


def index(request):
    post_list = Article.objects.all()
    print(post_list[0].id)
    return render(request, 'article/index.html', {'post_list': post_list})


def detail(request, article_id):
    try:
        post = Article.objects.get(id=str(article_id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'article/post_article.html', {'post': post})
