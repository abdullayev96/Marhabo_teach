from django.shortcuts import render
from django.views import View
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Article, Category
from django.shortcuts import get_object_or_404



class HomePageView(View):
    def get(self, request):
        articles = Article.objects.all()
        return render(request, "home.html", {'articles': articles})


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'category', 'summary', 'body', 'photo', 'video', 'author')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'summary', 'body', 'photo', 'video')
    template_name = 'article_edit.html'

    # def test_func(self):
    #     obj = self.get_object()
    #     return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


#############

class ArticleCategoryView(View):
    def get(self, request, category_name, beat_id):
        # category = Category.objects.get(name= category_name)
        category = get_object_or_404(Category, name=category_name, pk=beat_id)
        articles = Article.objects.filter(category=category)
        return render(request, 'category.html', {'articles': articles, "category": category})


class ArticleCategoryDetail(DetailView):
    model = Article
    template_name = ('article_category.html')


def for_all_pages(request):
    categories = Category.objects.all()
    return {"categories": categories}

