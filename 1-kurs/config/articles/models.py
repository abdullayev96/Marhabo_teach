from django.db import models
from django.contrib.auth import get_user_model
from django.db import models




class Category(models.Model):
    objects = models.CASCADE
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Article(models.Model):
    objects = None
    title =models.CharField( max_length=150)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)
    summary = models.CharField(max_length=100, blank=True)
    body = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    video = models.FileField(upload_to='video/', blank=True)
    date = models.DateTimeField( auto_now_add=True)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)
    #     self.id = None

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={"beat_id":self.pk})

##
#