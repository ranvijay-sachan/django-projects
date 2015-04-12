from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
# site request forzory to ebeded spacial token

"""Cross Site Request Forgery protection?

The CSRF middleware and template tag provides easy-to-use protection against Cross Site Request Forgeries.
This type of attack occurs when a malicious Web site contains a link,
a form button or some javascript that is intended to perform some action on your Web site,
using the credentials of a logged-in user who visits the malicious site in their browser.
A related type of attack, ?login CSRF?, where an attacking site tricks a user?s browser
into logging into a site with someone else?s credentials, is also covered.

The first defense against CSRF attacks is to ensure
that GET requests (and other ?safe? methods, as defined by 9.1.1 Safe Methods, HTTP 1.1, RFC 2616) are side-effect free.
Requests via ?unsafe? methods, such as POST, PUT and DELETE, can then be protected by following the steps below.

How to use it?

To take advantage of CSRF protection in your views, follow these steps:

The CSRF middleware is activated by default in the MIDDLEWARE_CLASSES setting. If you override that setting,
remember that 'django.middleware.csrf.CsrfViewMiddleware' should come before any view middleware that assume that CSRF attacks have been dealt with.

If you disabled it, which is not recommended, you can use csrf_protect() on particular views you want to protect (see below).

In any template that uses a POST form, use the csrf_token tag inside the <form> element if the form is for an internal URL, e.g.:

<form action="." method="post">{% csrf_token %}
This should not be done for POST forms that target external URLs, since that would cause the CSRF token to be leaked, leading to a vulnerability.

In the corresponding view functions, ensure that the 'django.template.context_processors.csrf' context processor is being used. Usually, this can be done in one of two ways:

Use RequestContext, which always uses 'django.template.context_processors.csrf' (no matter what template context processors are configured in the TEMPLATES setting).
If you are using generic views or contrib apps, you are covered already, since these apps use RequestContext throughout.

Manually import and use the processor to generate the CSRF token and add it to the template context. e.g.:"""

from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('article/login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('article/loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('article/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('article/logout.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    args = {}
    args.update(csrf(request))

    args['form'] = UserCreationForm()

    return render_to_response('article/register.html', args)

def register_success(request):
    return render_to_response('article/register_success.html')

