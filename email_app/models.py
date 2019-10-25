# coding=utf-8
import smtplib
from builtins import super
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.db import models
from django.urls import reverse

'''
    Criando o modelo para o teste de envio de e-mail
'''


class User(models.Model):
    first_name = models.CharField('Nome', max_length=15)
    last_name = models.CharField('Sobrenome', max_length=15)
    age = models.IntegerField('Idade')

    def __str__(self):
        return self.first_name + ' tem ' + str(self.age) + ' anos!'

    '''
        Toda vez que usuario for salvo, manda um e-mail
    '''

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        data = {'name': self.first_name,
                'age': self.age}
        plain_text = render_to_string('email/mensagem.txt', data)
        html_email = render_to_string('email/mensagem.html', data)
        try:
            send_mail(
                'Envio com Django',
                plain_text,
                'thalescast@gmail.com',
                ['thalescast@gmail.com'],
                html_message=html_email,
                fail_silently=True,
            )
        except smtplib.SMTPException:
            print('E-mail não enviado. Ocorreu algum problema!!')
