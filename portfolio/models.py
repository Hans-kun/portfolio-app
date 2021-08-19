from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('portfolio:post_list_by_category', args=[self.slug])


class Customer(models.Model): 
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True)
    occupation = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='static/images')
    description = models.TextField()
    resume = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title



class Post(models.Model):
    category = models.ForeignKey(Category, related_name='post',
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    tags = TaggableManager()
    created = models.DateTimeField(auto_now_add=True)
    pdf = models.FileField(upload_to='pdfs/', null = True, blank=True)

    def datepublished(self):
        return self.created.strftime('%B %d %Y')
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:post_detail', args=[self.id])
    

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.post.title
    