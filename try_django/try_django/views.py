from django import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    my_title = "Hello Home page..."
    context = {"title": "my title"}
    if request.user.is_authenticated:
        context = {"title": my_title, "my_list": [1, 2, 3, 4, 5]}
    return render(request, "home.html", context)


def about_page(request):
    return render(request, "about.html", {"title": "About Us"})


def contact_page(request):
    return render(request, "home_page.html", {"title": "Contact Us"})


def example_page(request):
    context = {"title": "Example"}
    template_name = "home_page.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    # render(request, "home_page.html", {"title": "Contact Us"})
    return HttpResponse(rendered_item)
