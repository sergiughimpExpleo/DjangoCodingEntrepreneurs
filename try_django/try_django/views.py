from django import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    my_title = "Hello there..."
    context = {"title": my_title}
    template_name = "title.txt"
    template_obj = get_template(template_name)
    rendered_string = template_obj.render(context)
    # doc = "<h1>{title}</h1>".format(title=my_title)
    # django_rendered_doc = "<h1>{{title}}</h1>".format(title=my_title)
    return render(request, "home_page.html", {"title": rendered_string})


def about_page(request):
    return render(request, "home_page.html", {"title": "About Us"})


def contact_page(request):
    return render(request, "home_page.html", {"title": "Contact Us"})


def exemple_page(request):
    context = {"title": "Example"}
    template_name = "home_page.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    # render(request, "home_page.html", {"title": "Contact Us"})
    return HttpResponse(rendered_item)
