from django.db import models

# Create your models here.

class TiposDeVeiculos(models.Model):
    tipo=models.CharField("Tipo de Veiculos" , max_length=20)


    def __str__(self):
        return "{}".format(self.tipo)

    class Meta:
        ordering=('tipo',)
        verbose_name ='tipo de veiculo'
        verbose_name_plural='Tipo de veiculos'




class MarcaDoVeiculo(models.Model):
    marca=models.CharField('Marca do veiculo', max_length=20, help_text='Ex. Nissan, Honda, fiat')

    def __str__(self):
        return "{}".format(self.marca)

    class Meta:
        ordering=('marca',)
        verbose_name='Marca do Veiculo'
        verbose_name_plural='Marca Dos Veiculos'


class Veiculos(models.Model):
    tipo= models.ForeignKey(TiposDeVeiculos)
    marca=models.ForeignKey(MarcaDoVeiculo)

    modelo=models.CharField('Modelo', max_length=50)
    placa=models.CharField('Placa', max_length=8)
    cor=models.CharField('Cor', max_length=10)


    def __str__(self):
        return "{} - {}".format(self.placa, self.modelo)


    class Meta:
        ordering=('tipo','marca','modelo')
        verbose_name='Veiculo'
        verbose_name_plural='Veiculos'
