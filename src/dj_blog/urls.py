"""dj_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, get_object_or_404

from posts.models import Post


def render_post(request, slug):
    # FIXME ограничить выборку
    # TODO переместить view в приложение posts
    post = get_object_or_404(Post, slug=slug)

    return render(request, template_name='post.html', context={
        'article_html': post.html,
        'title': post.title,
    })


urlpatterns = [
    path('', render, kwargs={
        'template_name': 'index.html',
    }),
    path('post/<slug:slug>/', render_post, name='post'),
    path('category/', render, kwargs={
        'template_name': 'category.html',
    }),
    path('admin/', admin.site.urls),
]
