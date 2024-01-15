from django.shortcuts import render
from django.views.generic import TemplateView

from posts.models import Post


class HomeView(TemplateView):
    template_name = "posts/index.html"

def home(request):
    context = dict()
    context['posts'] = Post.objects.all()
    return render(request, "posts/index.html", context)
