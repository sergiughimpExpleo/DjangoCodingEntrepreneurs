from django.db.models import query
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import BlogPost
# Create your views here.

# CRUD
# GET -> Retrieve / List
# POST -> Create / Update / Delete
# CRUD = Create Retrieve Update Delete


def blog_post_list_view(request):
    # list out objects
    # could be search
    qs = BlogPost.objects.filter(title__icontains='hello')
    template_name = 'blog_post_list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)


def blog_post_create_view(request):
    # create objects
    # use a form
    template_name = 'blog_post_create.html'
    context = {'form': None}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    # 1 object -> detail view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail2.html'
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_update.html'
    context = {"object": obj, 'form': None}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_delete.html'
    context = {"object": obj}
    return render(request, template_name, context)
