from django.shortcuts import render
from django.views import View

from kunuz_app.models import News, Category


# Create your views here.
class HomePageView(View):
    def get(self, request):
        categories = Category.objects.all()
        news_list = News.objects.all()
        context = {'news_list': news_list, 'categories': categories}
        return render(request, 'index.html', context)


class UzbNewsView(View):
    def get(self, request):
        news_list = News.objects.all().filter(category__id=1)
        context = {'news_list': news_list}
        return render(request, 'index.html', context)

class JahonNewsView(View):
    def get(self, request):
        news_list = News.objects.all().filter(category__id=2)
        context = {'news_list': news_list}
        return render(request, 'index.html', context)


class DetailView(View):
    def get(self, request, id):
        news = News.objects.get(id=id)
        context = {'news': news}
        return render(request, 'detail.html', context)
        print(news.image)


