from django.urls import path
from .views import homePage, blogPage, postPage, search, updatePost, deletePost, createPost, frenchVersion

urlpatterns = [
    path('', homePage, name='home'),
    path('blog/', blogPage, name='blog'),
    path('post/<slug>/', postPage, name='post'),
    path('search-results/', search, name='search'),
    path('create-post/', createPost, name='create-post'),
    path('update-post/<slug>/', updatePost, name='update-post'),
    path('delete-post/<slug>/', deletePost, name='delete-post'),
    path('french-version/', frenchVersion, name='french_version'),
]
