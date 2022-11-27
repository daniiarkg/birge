from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.contrib.auth.models import User

statuschoices = [
    ('cur', 'Сбор подписей'),
    ('viw', 'На рассмотрении'),
    ('res', 'Готов ответ'),
]


class Petition(models.Model):
    def __str__(self):
        return self.title

    def save(self):
        self.date = now()
        super(Petition, self).save()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=60, null=True)
    text = models.TextField(null=True)
    date = models.DateField(null=True, blank=True)
    votes = models.IntegerField(default=0)
    status = models.CharField(
        max_length=3, choices=statuschoices, default='cur')


class Comment(models.Model):
    def __str__(self):
        return self.petition.id + self.id

    def save(self):
        self.time = now()
        super(Petition, self).save()
    petition = models.ForeignKey(
        Petition,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    text = models.TextField(null=True)
    time = models.DateTimeField(null=True)


class Citizen(models.Model):
    def __str__(self):
        return self.user.username
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pin = models.CharField(max_length=14, null=True)
