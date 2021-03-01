from django.db.models import query
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import BlogPost
# Create your views here.


# GET -> 1 object
# filter -> [] object


def blog_post_detail_page(request, slug):
    template_name = 'blog_post_detail_page.html'
    print("DJANGO SAYS", request.method, request.path, request.user)
    # queryset = BlogPost.objects.filter(slug=slug)
    # if queryset.count() == 0:
    #     raise Http404
    # else:
    #     obj = queryset.first()
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj}
    return render(request, template_name, context)

    # try:
    #    obj = BlogPost.objects.get(slug=slug)
    # except BlogPost.DoesNotExist:
    #     raise Http404
    # except ValueError:
    #     raise Http404
    # query -> database -> data -> django renders it


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
    template_name = 'blog_post_detail.html'
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
