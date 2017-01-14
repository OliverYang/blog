from django.shortcuts import render
from django.http import HttpResponse
from blog.article.models import Article


# Create your views here.


def index(request):
    post_list = Article.objects.all()
    return render(request, 'article/index.html', {'post_list': post_list})
