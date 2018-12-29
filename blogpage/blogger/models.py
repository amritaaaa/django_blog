from django.db import models

# Create your models here.
class blog_article(models.Model):
    author=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    title=models.CharField(max_length=100)
    content=models.TextField()
    image=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
class register(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=20,default="")
    def __str__(self):
        return  self.name


