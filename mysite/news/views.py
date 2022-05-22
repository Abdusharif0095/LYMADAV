from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.generic import ListView
from .models import *
from .forms import *
from django.core.paginator import Paginator


class HomeNews(ListView):
    model = News
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список новостей'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


def register(request):

    if request.method == 'POST':
        form1 = RegisterForm(request.POST, request.FILES)
        if form1.is_valid():
            print(form1.cleaned_data)
            User.objects.create(position_id=Position.objects.filter(name='автор').first(), fullname=form1.cleaned_data['fullname'], email=form1.cleaned_data['email'], password=form1.cleaned_data['password'], birthday=form1.cleaned_data['birthday'], about=form1.cleaned_data['about'])
            # position_id = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Должность')
            # fullname = models.CharField(max_length=50, verbose_name='ФИО')
            # email = models.CharField(max_length=50, verbose_name='Эл. Почта')
            # password = models.CharField(max_length=30, verbose_name='Пароль')
            # birthday = models.DateField(verbose_name='День Рождения')
            # photo = models.ImageField(upload_to='photos/user/', blank=True, verbose_name='Фото')
            # about = models.TextField(blank=True, verbose_name='О пользователе')
            # status = models.BooleanField(default=False, verbose_name='Регистрирован')
            return redirect('home')
        else:
            print(form1.errors)
    form = SearchForm()
    form1 = RegisterForm()
    context = {
        'form': form,
        'form1': form1,
    }
    return render(request, 'news/register.html', context)


def login(request):
    return render(request, 'news/login.html')


def index(request):
    form = SearchForm()
    news = News.objects.filter(is_published=True).order_by('-created_at')
    paginator = Paginator(news, 3)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    context = {
        'news': news,
        'title': 'Список новостей',
        'form': form,
        'page_obj': page_objects,
        'page_num': page_num,
        'prev': str(int(page_num) - (int(page_num) > 1)),
        'next': str(int(page_num) + (int(page_num) < (len(news) + 3) // 3)),
        'max_page': str((len(news) + 3) // 3),
    }
    return render(request, 'news/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id_id=category_id, is_published=True)
    category = Category.objects.filter(pk=category_id)

    paginator = Paginator(news, 3)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)

    form = SearchForm()

    context = {
        'title': 'Список новостей',
        'news': news,
        'category': category,
        'page_obj': page_objects,
        'page_num': page_num,
        'prev': str(int(page_num) - (int(page_num) > 1)),
        'next': str(int(page_num) + (int(page_num) < (len(news) + 3) // 3)),
        'max_page': str((len(news) + 3) // 3),
        'form': form,
    }

    return render(request, 'news/category.html', context)


def view_news(request, news_id):
    form1 = SearchForm()
    news_item = get_object_or_404(News, pk=news_id)
    comments = reversed(Comment.objects.filter(news_id_id=news_id, is_published=True))

    if request.POST:
        form1 = CommentForm(request.POST)
        cur = News.objects.filter(id=news_id).first()
        if form1.is_valid():
            Comment.objects.create(news_id=cur, writer=form1.cleaned_data['writer'], content=form1.cleaned_data['content'])
            return redirect('view_news', news_id)
    else:
        form1 = CommentForm()
        form = SearchForm()
        return render(request, 'news/view_news.html', {"news_item": news_item, 'comments': comments, 'form1': form1, 'form': form})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form1 = NewsForm()
        form = SearchForm()
    return render(request, 'news/add_news.html', {'form': form, 'form1': form1})


def search_list(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            ans = ""
            newss = []
            news = News.objects.all()
            for item in news:
                if form.cleaned_data['search_title'].lower() in item.title.lower():
                    newss.append(item)

            form = SearchForm()

            if len(newss) == 0:
                search_ans = "Нет новостей с такими заголовками!"
            else:
                search_ans = "Ответ на ваш запрос!"

            paginator = Paginator(newss, 3)
            page_num = request.GET.get('page', 1)
            page_objects = paginator.get_page(page_num)
            context = {
                'news': newss,
                'title': 'Список новостей',
                'form': form,
                'page_obj': page_objects,
                'search_ans': search_ans,
                'page_num': page_num,
                'prev': str(int(page_num) - (int(page_num) > 1)),
                'next': str(int(page_num) + (int(page_num) < (len(news) + 3) // 3)),
                'max_page': str((len(news) + 3) // 3),
            }

            return render(request, 'news/index.html', context)

    else:

        form = SearchForm()
        news = News.objects.all()
        paginator = Paginator(news, 3)
        page_num = request.GET.get('page', 1)
        page_objects = paginator.get_page(page_num)
        context = {
            'news': news,
            'title': 'Список новостей',
            'form': form,
            'page_obj': page_objects,
            'page_num': page_num,
            'prev': str(int(page_num) - (int(page_num) > 1)),
            'next': str(int(page_num) + (int(page_num) < (len(news) + 3) // 3)),
            'max_page': str((len(news) + 3) // 3),
        }

        return render(request, 'news/index.html', context)


def test(request):
    objects = ['john1', 'paul2', 'george3', 'ringo4', 'john5', 'paul6', 'george7', 'ringo8', 'john1', 'paul2', 'george3', 'ringo4', 'john5', 'paul6', 'george7', 'ringo8', 'john1', 'paul2', 'george3', 'ringo4', 'john5', 'paul6', 'george7', 'ringo8', 'john1', 'paul2', 'george3', 'ringo4', 'john5', 'paul6', 'george7', 'ringo8', 'john1', 'paul2', 'george3', 'ringo4', 'john5', 'paul6', 'george7', 'ringo8']
    paginator = Paginator(objects, 1)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'news/test.html', {'page_obj': page_objects})
