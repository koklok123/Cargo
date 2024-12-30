from django.shortcuts import render, redirect
from . models import Osnov, News, Questions, Contact
from django.views import View
from django.views.generic import DetailView, ListView
from apps.telegram.views import get_text
from . forms import ReviewForm
from django.http import HttpResponseNotFound
# Create your views here.


def love(request):
    return render(request, 'animations/love.html')

def new_year(request):
    return render(request, 'animations/new-year.html')

def custum_404_view(request, exception):
    return render(request, 'animations/404.html', status=404)

def custum_500_view(request, *args, **argv):
    return render(request, '500.html', status=500)

class OsnovView(View):
    template_name = 'index.html'

    def get(seld, request):
        osnov = Osnov.objects.all()
        questions = Questions.objects.all()
        context = {
            'osnov_list': osnov,
            'questions_list': questions,
        }
        return render(request, OsnovView.template_name, context)
    
class NewsDetailView(DetailView):
    model = News
    tem = 'single.html'
    template_name = tem

    def news(request):
        news = News.objects.all()
        return render(request, NewsDetailView.tem, {'news_list': news})
    
class NewsListView(ListView):
    model = News
    tem = 'news-list.html'
    template_name = tem

    def news_list(request):
        news = News.objects.all()
        return render(request, NewsListView.tem, {'news_list': news})
    

class AddComment(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        news = News.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.news = news
            form.save()
        return redirect(news.get_absolute_url())
        

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        Contact.objects.create(name=name, email=email, message=message)
        
        get_text(f"""
                 Новое сообщение:
                 Имя: {name}
                 Email: {email}
                 Сообщение: {message}
        """)
        
        return redirect('index')
    
    return render(request, "contact.html", {'contact_form': True})