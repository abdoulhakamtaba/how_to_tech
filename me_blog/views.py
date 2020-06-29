from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import BlogPost, ImageThing, Tags, Category, Author, PostView, SignUp
from .forms import CommemtForm, BlogPostForm
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q

def search(request):
    queryset = BlogPost.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) | 
            Q(overview__icontains=query)
        ).distinct()
    '''
    if request.method == 'POST':
        email=request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        return redirect('blogPage')
    '''
    context = {
        'queryset':queryset
    }
    return render(request, 'search_result.html', context)

# Create your views here.
def homePage(request):
    #featured post
    featured = BlogPost.objects.filter(featured=True)
    #latest post
    latest_post = BlogPost.objects.order_by('-postdate')[0:3]
    img = ImageThing.objects.all()

    if request.method == 'POST':
        emaill = request.POST['email']
        new_signup = SignUp()
        new_signup.email=emaill
        new_signup.save()
        return redirect('home')

    context={
        'blogObjects':featured,
        'latest_post':latest_post,
        'img':img,
    }

    return render(request, 'index.html', context)


#categories and number
def get_category_count():
    queryset = BlogPost.objects.values('category__title').annotate(Count('category__title'))

    return queryset


def blogPage(request):
    all_posts = BlogPost.objects.all()
    paginator = Paginator(all_posts, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset= paginator.page(paginator.num_pages)


    latest_post = BlogPost.objects.order_by('-postdate')[0:3]
    tags = Tags.objects.all()

    #categories and number
    categories_and_numb = get_category_count()

    print(categories_and_numb)        


    context = {
        'queryset':paginated_queryset,
        'latest_post': latest_post,
        'tags':tags,
        'page_request_var':page_request_var,
        'categories_and_numb':categories_and_numb,
    }

    return render(request, 'blog.html', context)

def postPage(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    latest_post = BlogPost.objects.order_by('-postdate')[0:3]
    categories_and_numb = get_category_count()
    tags = Tags.objects.all()

    PostView.objects.get_or_create(post=post)

    form = CommemtForm(request.POST or None)
    if request.method == 'POST':
        form.instance.post = post
        form.save()
        return redirect('post', slug=slug)

    context = {
        'post':post,
        'latest_post': latest_post,
        'categories_and_numb':categories_and_numb,
        'tags':tags,
        'form':form,
    }

    return render(request, 'post.html', context)

def get_author(user):
    qs = Author.objects.get(user=user)
    if qs:
        return qs
    return None

def createPost(request):
    title = 'Create'
    form = BlogPostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = author
            form.save()
            return redirect('blog')

    context = {
        'title':title,
        'form':form,
    }

    return render(request, 'post_create.html', context)

def updatePost(request, slug):
    title = 'Update'
    post =  get_object_or_404(BlogPost, slug=slug)
    form = BlogPostForm(request.POST or None, request.FILES or None, instance=post)
    author = get_author(request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = author
            form.save()
            return redirect('post', slug=slug)

    context = {
        'title':title,
        'form':form,
    }

    return render(request, 'post_create.html', context)

def deletePost(request, slug):
    post =  get_object_or_404(BlogPost, slug=slug)
    post.delete()
    return redirect(reverse('blog'))

def frenchVersion(request):
    return render(request, 'french.html')