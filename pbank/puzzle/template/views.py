from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', locals())


def login_user(request):
    # if request.method == "POST":
    #     username = request.POST.get("username", None)
    #     psd = request.POST.get("psd", None)
    #     is_auth = authenticate(request, username=username, psd=psd)
    #     if is_auth:
    #         login(request, is_auth)
    #         return redirect("login/")
    #     else:
    #         error = "f'invalid {username} and {psd} password"
    return render(request, "login.html", locals())


def logout_view(request):
    return redirect(request, "logout.html", locals())
