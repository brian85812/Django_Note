from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True)

    def __str__(self):
        return self.title
