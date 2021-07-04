from django.db import models

VEICULO_CHOICES = (
    ('P', 'Pequeno'),
    ('M', 'Medio'),
    ('G', 'Grande'),
    ('C', 'Carreta'),
    ('B', 'Bi-trem'),
    ('A', 'Cavalo')
)

PATIO_CHOICES = (
    ('N', 'Nulo'),
    ('P', 'Patio'),
    ('L', 'Livre'),
    ('B', 'Bloqueado'),
    ('E', 'Espera')
)

ENTRADA_CHOICES = (
    ('M', 'Mensalista'),
    ('A', 'Avulso'),
    ('E', 'Especial')
)

STATUS_CHOICES = (
    ('A', 'Ativo'),
    ('I', 'Inativo')
)

class Cliente(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='i')
    cadastro = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)


class Veiculos(models.Model):
    modelo = models.CharField(max_length=15, null=True, blank=True)
    cor = models.CharField(max_length=10, null=True, blank=True)
    tipo = models.CharField(max_length=1, choices=VEICULO_CHOICES, null=False, blank=False)
    placa = models.CharField(max_length=7, null=False, blank=False)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    cadastro = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)


class Entrada(models.Model):
    tipo_entrada = models.CharField(max_length=1, choices=ENTRADA_CHOICES, null=False, blank=False)
    tipo_veiculo = models.CharField(max_length=1, choices=VEICULO_CHOICES, null=False, blank=False)
    placa = models.CharField(max_length=7)
    data = models.DateTimeField()
    status_patio = models.CharField(max_length=1, choices=PATIO_CHOICES, default='P', null=False, blank=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A', null=False, blank=False)
