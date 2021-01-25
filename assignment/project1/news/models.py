from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField('TITLE', max_length=100)
    slug = models.SlugField('SLUG', unique=True)
    author = models.CharField('AUTHOR', max_length=50)
    description = models.CharField('DESCRIPTION', max_length=200, blank=True)
    date = models.DateTimeField('DATE')

    def __str__(self):
        return self.title, self.description, self.author, self.date

    class Meta:
        ordering = ('-date',)