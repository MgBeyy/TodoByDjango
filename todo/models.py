from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50, verbose_name="Başlık")
    completed = models.BooleanField(verbose_name="Durum")

    def __str__(self):
        return self.title