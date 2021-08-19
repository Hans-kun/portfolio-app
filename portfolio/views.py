from urllib.parse  import quote_plus
from django.shortcuts import render, get_object_or_404
from .models import Category, Customer, WorkExperience, Post, PostImage
from wsgiref.util import FileWrapper
from django.http import HttpResponse, FileResponse
import mimetypes
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
	

# Create your views here.


def index(request, category_slug=None, tag_slug=None):
    category = None
    categories = Category.objects.all()
    posts = Post.objects.all()
    tag = None
    paginator = Paginator(posts, 30) #30 post in  each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)


    context = {'category': category, 'categories':categories, 'posts':posts, 'page': page,}
    return render (request, "index.html", context)


def post_detail(request, id):
    get_post_cat = get_object_or_404(Post, id=id)
    post_cat = get_post_cat.category

    post_category = Post.objects.filter(category=post_cat).order_by('-created')
    post_category = [i for i in post_category if not i.id == id][:3]
    post = get_object_or_404(Post, id=id)
    share_string = quote_plus(post.description)
    print(share_string)
    
    photos = PostImage.objects.filter(post=post)
    context = {'post_category': post_category, 'post': post, 'photos':photos, 'share_string':share_string}
    return render(request, 'detail.html', context)


def about(request):
    customer = Customer.objects.all()
    workexp = WorkExperience.objects.all()
    context = {'customer': customer, 'workexp': workexp}
    return render(request, 'text.html', context)




# def download_pdf(request):
#     filepath = open('C:\\Users\\User\\portfolio app2\\portfolioApp\\conda-cheatsheet.pdf', 'rb')
#     response = FileResponse(filepath)
#     response['Content-Type'] = 'application/pdf'
#     response['Content-Disposition'] = 'attachment:filename=conda-cheatsheet.pdf'
#     return response


# def tagged(request, tag_slug=None):
#     post = get_object_or_404(Post, id=id)
#     tags = post.tags.all()
#     if tag_slug:
#         tag= get_object_or_404(Tag, slug=tag_slug)
#         post = post.filter(tags__in=[tag])
#     context = {'tags': tags}
#     return render(request, 'detail.html', context)
