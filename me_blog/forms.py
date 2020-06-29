from django import forms
from .models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):

    class Meta:
        model=BlogPost
        fields = ('title', 'overview', 'content', 'category', 'tag', 'image', 'featured', 'slug', 'previous_post', 'next_post')

class CommemtForm(forms.ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows':4,
        'name':"message",
        'placeholder':"Message*",
        'class':"form-control"
    }))

    email_address = forms.CharField(widget=forms.TextInput(attrs={
        'name' : "username",
        'id':"useremail",
        'placeholder':"Email Address",
        'class':"form-control"
    }))

    name = forms.CharField(widget=forms.TextInput(attrs={
        'name' : "username",
        'id':"username",
        'placeholder':"Name",
        'class':"form-control"
    }))

    class Meta:
        model = Comment
        fields = ('name', 'email_address', 'content',)