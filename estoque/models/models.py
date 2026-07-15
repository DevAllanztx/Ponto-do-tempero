from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class Produto(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="produtos"
    )
    nome = models.CharField(max_length=100)
    preco_medida = models.DecimalField("Preco por Medida", max_digits=8, decimal_places=2)
    preco_atacado_meio_kilo = models.DecimalField("Preco Atacado (500g)", max_digits=8, decimal_places=2)
    preco_atacado_kilo = models.DecimalField("Preco Atacado (1kg)", max_digits=8, decimal_places=2)
    preco_bruto = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=0)
    validade = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.nome
