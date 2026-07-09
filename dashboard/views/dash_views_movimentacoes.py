
    # Adicione esta função ao seu dashboard/views/dash_views.py
    # (ajuste o import do model conforme o app onde você colocar Produto/Movimentacao)
    
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
    
from estoque.models import Movimentacao, Produto
    

@login_required
def movimentacoes(request):
    if request.method == "POST":
        produto_id = request.POST.get("produto")
        tipo = request.POST.get("tipo")
        quantidade = request.POST.get("quantidade")
        observacao = request.POST.get("observacao", "")
        try:
            produto = Produto.objects.get(pk=produto_id)
            quantidade = int(quantidade)

            if tipo == Movimentacao.Tipo.SAIDA and quantidade > produto.quantidade:
                messages.error(
                    request,
                    f"Estoque insuficiente. {produto.nome} tem apenas {produto.quantidade} unidade(s).",
                )
            else:
                Movimentacao.objects.create(
                    produto=produto,
                    tipo=tipo,
                    quantidade=quantidade,
                    responsavel=request.user,
                    observacao=observacao,
                )
                messages.success(request, "Movimentação registrada com sucesso.")
        except (Produto.DoesNotExist, ValueError, TypeError):
            messages.error(request, "Não foi possível registrar a movimentação. Confira os dados.")

        return redirect("movimentacoes")
 
    lista_movimentacoes = Movimentacao.objects.select_related("produto", "responsavel").all()[:100]
    produtos = Produto.objects.all().order_by("nome")
 
    contexto = {
        "movimentacoes": lista_movimentacoes,
        "produtos": produtos,
        "total_entradas": Movimentacao.objects.filter(tipo=Movimentacao.Tipo.ENTRADA).count(),
        "total_saidas": Movimentacao.objects.filter(tipo=Movimentacao.Tipo.SAIDA).count(),
    }
    return render(request, "movimentacoes.html", contexto)
 
