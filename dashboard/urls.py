from django.urls import path

from dashboard import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("home/", views.home, name="home"),
    path("logout/", views.logout_view, name="logout"),
    # Placeholders das seções do menu (ainda sem tela própria).
    path("produtos/", views.placeholder, {"titulo": "Produtos"}, name="produtos"),
    path("movimentacoes/", views.placeholder, {"titulo": "Movimentações"}, name="movimentacoes"),
    path("relatorios/", views.placeholder, {"titulo": "Relatórios"}, name="relatorios"),
    path("contatos/", views.placeholder, {"titulo": "Contatos"}, name="contatos"),
    
]

