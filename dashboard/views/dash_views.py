from django.views import generic
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
            "error": "Usuário ou senha inválidos.",
            "usuario": usuario,
        })

    return render(request, "login_ponto_tempero.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def home(request):
    return render(request, "index.html")


class PostView(generic.ListView):
    # Mantém sua listagem (se existir Post model)
    try:
        from dashboard.models import Post

        queryset = Post.objects.filter(status=1).order_by("-created_on")
        template_name = "dashboard/post_list.html"
    except Exception:
        queryset = []
        template_name = "index.html"


class PostDetailView(generic.DetailView):
    try:
        from dashboard.models import Post

        model = Post
        template_name = "dashboard/index.html"
    except Exception:
        model = None
        template_name = "index.html"

