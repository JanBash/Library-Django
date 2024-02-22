from django.db import models

class Author(models.Model):
    username = models.CharField(max_length=50)
    age = models.IntegerField()
    
    def __str__(self):
        return f'{self.username} | {self.pk}'

class Category(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return f'{self.name} | {self.pk}'

class Post(models.Model):
    title = models.CharField(max_length = 150)
    content = models.TextField(default = '')
    category = models.ForeignKey(Category, verbose_name = ("categories"), on_delete=models.PROTECT)
    author = models.ForeignKey(Author, verbose_name = ("authors"), on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f'{self.title} | {self.pk}'