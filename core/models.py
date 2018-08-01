from django.db import models

# Create your models here.

class Endereco(models.Model):
    logradouro = models.CharField('Logradouro', max_length=150)
    numero = models.CharField('Número', max_length=10)
    bairro = models.CharField('Bairro', max_length=20)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.logradouro

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ['logradouro']