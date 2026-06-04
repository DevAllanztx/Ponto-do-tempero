from django.http import HttpResponse
from django.views import generic


class EstoqueView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Estoque funcionando')