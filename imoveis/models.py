from django.db import models
from django.conf import settings

class Imovel(models.Model):


    FINALIDADE_CHOICES = [
        ('venda', 'Venda'),
        ('aluguel', 'Aluguel'),
        ('locacao', 'Locação'),
        ('arrendar', 'Arrendar'),
    ]

    CIDADE_CHOICES = [
        ('João Pessoa', 'João Pessoa'),
        ('Mediaçoes', 'Mediações'),
        ]
    

    STATUS_CHOICES = [
        ('pronto', 'Pronto'),
        ('construcao', 'Em Construção'),
        ('lancamento', 'Lançamento'),
        ('na_planta', 'Na Planta'),
    ]

    TIPO_CHOICES = [
        ('casa', 'casa'),
        ('apartamento', 'apartamento'),
        ('terreno', 'terreno'),
        ('comercial', 'comercial'),
        ('cobertura', 'cobertura'),
        ('flat', 'flat'),
        ('condominio fechado', 'condominio fechado'),
        ]

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    cidade = models.CharField(max_length=100, choices=CIDADE_CHOICES)
    bairro = models.CharField(max_length=100)

    quartos = models.IntegerField()
    banheiros = models.IntegerField()
    vagas_garagem = models.IntegerField()
    metragem = models.DecimalField(max_digits=10, decimal_places=2)
    finalidade = models.CharField(max_length=20, choices=FINALIDADE_CHOICES)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    imagem_principal = models.ImageField(upload_to='imoveis/', blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    def link_whatsapp(self):
        try:
            numero = settings.WHATSAPP_NUMBER
            if not numero:
                return None
            mensagem = f"Olá, tenho interesse no imóvel '{self.titulo}' listado no seu site. Poderia me fornecer mais informações?"
            return f"https://wa.me/{numero}?text={mensagem}"
        except AttributeError:
            return None
    
    def __str__(self):
        return self.titulo
    
class Imagem(models.Model):
    imovel = models.ForeignKey(Imovel, related_name='imagens', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='imoveis/')

    def __str__(self):
        return f"Imagem do imóvel: {self.imovel.titulo}"
    
