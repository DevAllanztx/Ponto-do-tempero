from django.urls import path

from dashboard import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("home/", views.home, name="home"),
    path("logout/", views.logout_view, name="logout"),
    path("post/<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
]

