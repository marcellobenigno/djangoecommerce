from django.db import models


class Contact(models.Model):
    name = models.CharField('nome', max_length=100)
    email = models.EmailField('e-mail', max_length=50)
    message = models.TextField('mensagem')

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'
        ordering = ['name', ]

    def __str__(self):
        return self.name
