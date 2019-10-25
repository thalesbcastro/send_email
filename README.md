# Envio de e-mail com Django

Com pouquíssimas linhas de código, algumas configuraçes no settings, um modelo e uma view são suficientes para criar um envio de e-mail simples no Django.

## 1º passo:
Antes de tudo deve-se configurar o servidor SMTP no settings.py:

```
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'provedor_email@gmail.com.br'
EMAIL_HOST_PASSWORD = 'senha_provedor'
EMAIL_USE_TLS = True

```

## Criar um modelo no models.py

Neste exemplo, foi criado uma aplicação de nome email_app. Dentro dela, no arquivo models.py, a classe User:

```

class User(models.Model):
    first_name = models.CharField('Nome', max_length=15)
    last_name = models.CharField('Sobrenome', max_length=15)
    age = models.IntegerField('Idade')

    def __str__(self):
        return self.first_name + ' tem ' + str(self.age) + ' anos!'

```
Dentro deste model, a função save() envia um e-mail toda vez que os campos são preenchidos e salvos. Dentro dela, o método super() foi sobrescrito e se inseriu o seguinte trecho de código: 

```
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

```

Para que se possa enviar a mensagem em HTML, a variável html_email foi criada, utilizando-se do método render_to_string, bem como o plain_text para que, caso a plataforma não renderize o html, seja enviada em forma de texto.   

