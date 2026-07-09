from django.db import models

from django.conf import settings
from django.db import models


class Produto(models.Model):
    """
    Model único que substitui Tempero, Alho, Cebola, Pimenta,
    Pimenta_Agranel, chas, mel e PreTreino. A diferenciação
    agora é feita pelo campo `categoria`.
    """

    class Categoria(models.TextChoices):
        TEMPERO = "tempero", "Tempero"
        ALHO = "alho", "Alho"
        CEBOLA = "cebola", "Cebola"
        PIMENTA = "pimenta", "Pimenta"
        PIMENTA_GRANEL = "pimenta_granel", "Pimenta a Granel"
        CHA = "cha", "Chá"
        MEL = "mel", "Mel"
        PRE_TREINO = "pre_treino", "Pré-Treino"

    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=Categoria.choices)
    preco_medida = models.DecimalField(max_digits=8, decimal_places=2)
    preco_atacado_meio_kilo = models.DecimalField(max_digits=8, decimal_places=2)
    preco_atacado_kilo = models.DecimalField(max_digits=8, decimal_places=2)
    preco_bruto = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade = models.IntegerField(default=0)
    validade = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["categoria", "nome"]

    def __str__(self):
        return f"{self.nome} ({self.get_categoria_display()})"


class Movimentacao(models.Model):
    class Tipo(models.TextChoices):
        ENTRADA = "entrada", "Entrada"
        SAIDA = "saida", "Saída"

    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE, related_name="movimentacoes"
    )
    tipo = models.CharField(max_length=10, choices=Tipo.choices)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)
    responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    observacao = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["-data"]

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.produto.nome} ({self.quantidade})"

    def save(self, *args, **kwargs):
        """Ao criar uma movimentação nova, ajusta a quantidade do produto automaticamente."""
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            if self.tipo == self.Tipo.ENTRADA:
                self.produto.quantidade += self.quantidade
            else:
                self.produto.quantidade = max(0, self.produto.quantidade - self.quantidade)
            self.produto.save(update_fields=["quantidade"])

