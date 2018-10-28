from django.shortcuts import render, render_to_response, get_object_or_404
from .models import Article

# Create your views here.
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {}
    context['article_obj'] = article
    return render_to_response("article_detail.html", context)

def article_list(request):
    articles = Article.objects.filter(is_deleted=False)
    context = {}
    context['articles'] = articles
    return render_to_response("article_list.html", context)
