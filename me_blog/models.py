from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.shortcuts import reverse

# Create your models here.

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Tags(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    content= models.TextField(max_length=200)
    post = models.ForeignKey('BlogPost', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PostView(models.Model):
    post = models.ForeignKey('BlogPost', related_name='views', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.title[:20]}...'


class BlogPost(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    postdate = models.DateTimeField(auto_now_add=True)
    overview = models.TextField()
    content = RichTextField()
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tags)
    image = models.ImageField(upload_to='images/')
    featured = models.BooleanField()
    slug = models.CharField(max_length=100)
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    

    def get_absolute_url(self):
        return reverse('post', kwargs={
            'slug': self.slug
        })

    def overview_short(self):
        return self.overview[:150]

    def __str__(self):
        return self.title

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')
    
    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()

class ImageThing(models.Model):
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.image.url





class SignUp(models.Model):
    email = models.EmailField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email