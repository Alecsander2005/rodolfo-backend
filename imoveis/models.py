from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField


class Imovel(models.Model):

    TIPO_VAGA_CHOICES = [
        ('Fixa', 'Fixa'),
        ('Rotativa', 'Rotativa'),
    ]

    FINALIDADE_CHOICES = [
        ('venda', 'Venda'),
        ('aluguel', 'Aluguel'),
        ('locacao', 'Locação'),
        ('arrendar', 'Arrendar'),
    ]

    CIDADE_CHOICES = [
        ('João Pessoa', 'João Pessoa'),
        ('Cabedelo', 'Cabedelo'),
        ('Conde', 'Conde'),

    ]

    STATUS_CHOICES = [
        ('pronto', 'Pronto'),
        ('construcao', 'Em Construção'),
        ('lancamento', 'Lançamento'),
        ('na_planta', 'Na Planta'),
    ]

    TIPO_CHOICES = [
        ('casa', 'Casa'),
        ('apartamento', 'Apartamento'),
        ('terreno', 'Terreno'),
        ('comercial', 'Comercial'),
        ('cobertura', 'Cobertura'),
        ('flat', 'Flat'),
        ('condominio fechado', 'Condomínio Fechado'),
    ]

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    cidade = models.CharField(max_length=100, choices=CIDADE_CHOICES)
    bairro = models.CharField(max_length=100)

    quartos = models.PositiveIntegerField()
    banheiros = models.PositiveBigIntegerField()
    vagas_garagem = models.PositiveIntegerField(
        default=0,
    )

    tipo_vaga = models.CharField(
        max_length=10,
        choices=TIPO_VAGA_CHOICES,
        blank=True,
        null=True
    )

    metragem = models.DecimalField(max_digits=10, decimal_places=2)

    finalidade = models.CharField(max_length=20, choices=FINALIDADE_CHOICES)
    tipo = models.CharField(max_length=30, choices=TIPO_CHOICES)

    criado_em = models.DateTimeField(auto_now_add=True)

    def link_whatsapp(self):
        try:
            numero = settings.WHATSAPP_NUMBER

            if not numero:
                return None

            mensagem = (
                f"Olá, tenho interesse no imóvel "
                f"'{self.titulo}' listado no seu site."
            )

            return f"https://wa.me/{numero}?text={mensagem}"

        except AttributeError:
            return None

    def __str__(self):
        return self.titulo


class Imagem(models.Model):

    imovel = models.ForeignKey(
        Imovel,
        related_name='imagens',
        on_delete=models.CASCADE
    )

    imagem = CloudinaryField('image')

    def __str__(self):
        return f"Imagem do imóvel: {self.imovel.titulo}"