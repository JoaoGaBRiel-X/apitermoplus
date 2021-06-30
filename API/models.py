from django.db import models

VEICULO_CHOICES = (
        ('P', 'Pequeno'),
        ('M', 'Medio'),
        ('G', 'Grande'),
        ('C', 'Carreta'),
        ('B', 'Bi-trem'),
        ('A', 'Cavalo')
    )

class Cliente(models.Model):
    STATUS_CHOICES = (
        ('a', 'Ativo'),
        ('i', 'Inativo')
    )
    nome = models.CharField(max_length=30)
    cadastro = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='i')

class Veiculos(models.Model):
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15)
    cor = models.CharField(max_length=10)
    tipo = models.CharField(max_length=1, choices=VEICULO_CHOICES, null=False, blank=False)
    placa = models.CharField(max_length=7)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    cadastro = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

class Entrada(models.Model):
    ENTRADA_CHOICES = (
        ('M', 'Mensalista'),
        ('A', 'Avulso'),
        ('E', 'Especial')
    )
    tipo_entrada = models.CharField(max_length=1, choices=ENTRADA_CHOICES, null=False, blank=False)
    tipo_veiculo = models.CharField(max_length=1, choices=VEICULO_CHOICES, null=False, blank=False)
    placa = models.CharField(max_length=7)
    data = models.DateTimeField()


