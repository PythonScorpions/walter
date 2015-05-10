__author__ = 'Scorpion_Python'
from django.shortcuts import render, get_object_or_404,redirect,render_to_response
from django.http import HttpResponseRedirect, HttpResponse, QueryDict
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required

# custom login_required decorator for class based view
def custom_login_required(f):
    def wrap(request, *args, **kwargs):
        # this will check whether admin user or merchant is logged in , if not it will redirect to login page
        if request.user.is_authenticated() and request.user.is_superuser == False:
            pass
        else:
            return render(request, "userapp/login.html", locals())
        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap

def admin_login_required(f):
    def wrap(request, *args, **kwargs):
        # this will check whether admin user or merchant is logged in , if not it will redirect to login page
        if request.user.is_authenticated() and request.user.is_superuser == True:
             return render(request, 'userapp/login.html', locals())
        else:
            return render(request, "userapp/login.html", locals())
        # return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap

class index_view(View):
    template1 = "userapp/login.html"
    template2 = "userapp/login.html"

    @method_decorator(custom_login_required)
    def get(self, request):
        active = "index"
        flag="home"
        return render(request, self.template1, locals())

    @method_decorator(custom_login_required)
    def post(self, request):
        flag="home"
        active = "index"
        return render(request, self.template2, locals())
