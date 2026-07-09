from django.views import generic
from django.shortcuts import render


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

