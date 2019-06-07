from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField('date published')
    body = models.TextField()
    hashtags = models.ManyToManyField('Hashtag',blank=True) # 다대다 ManyToManyField
    image = models.ImageField(upload_to='images/',blank=True)

class Comment(models.Model):
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    comment_text = models.CharField(max_length=200)

class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
