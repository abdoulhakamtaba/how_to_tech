from django.contrib import admin
from .models import Author, Category, Comment, BlogPost, ImageThing, Tags, PostView, SignUp

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(ImageThing)
admin.site.register(Tags)
admin.site.register(PostView)
admin.site.register(SignUp)