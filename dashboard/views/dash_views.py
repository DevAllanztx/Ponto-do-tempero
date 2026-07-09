from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        usuario = request.POST.get("usuario", "")
        senha = request.POST.get("senha", "")
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect("home")
        return render(request, "login_ponto_tempero.html", {
            "error": "Usuário ou senha incorretos.",
            "usuario": usuario,
        })

    return render(request, "login_ponto_tempero.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def home(request):
    return render(request, "index.html")


@login_required(login_url="login")
def placeholder(request, titulo):
    return render(request, "placeholder.html", {"titulo": titulo})

