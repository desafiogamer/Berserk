from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Comment(models.Model):
    STATUS = (
        ('Lido', 'Lido'),
        ('Não lido', 'Não lido')
    )

    name = models.CharField(max_length=50, blank=False)
    comment = models.TextField()
    status = models.CharField(choices=STATUS, max_length=10, default='Não lido')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

