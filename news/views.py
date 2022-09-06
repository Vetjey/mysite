from django.shortcuts import render, get_object_or_404
from .models import News, Category

def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, template_name='news/index.html', context = context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    #category_id указываем как в БД
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category
    }
    return render(request, template_name='news/category.html', context=context)

def view_news(request, pk):
    new = get_object_or_404(News, pk=pk)
    context = {
        'new': new
    }
    return render(request, template_name='news/view_new.html', context=context)