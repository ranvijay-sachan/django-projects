from django.shortcuts import render_to_response
from article.models import Article
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def articles(request):
    language = 'en-us'
    session_language = 'en-us'
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    return render_to_response('article/articles.html', {'articles': Article.objects.all(), 'language':language, 'session_language': session_language })

def article(request, article_id=1):
    return render_to_response('article/article.html', {'article': Article.objects.get(id=article_id) })

def language(request, language = 'en-us'):
    response = HttpResponse("setting language to %s" % language)
    response.set_cookie('lang',language)
    request.session['lang'] = language
    return response
