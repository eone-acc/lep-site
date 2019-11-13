from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    pub_date = models.DateField(auto_now_add=True)
    text = models.TextField(blank=True, null=True)
    workoff_date = models.DateField(blank=True, null=True)
    light_count = models.CharField(max_length=25, blank=True, null=True)

    def get_absolute_url(self):
        return ('projects/'+self.slug)


    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.post.title
