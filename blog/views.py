from typing import Any
from django.http import HttpResponse , Http404
from django.shortcuts import render
from blog.data import posts

# Create your views here.
def blog(req):
    context = {
        #'text': 'Estamos no blog',
        'title':'Blog - ',
        'posts': posts,
        }
    return render(req, 'blog/index.html',context)

def post(req:HttpResponse, post_id:Any):
    found_post: dict[str, Any] | None = None
    
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    if found_post is None:
        raise Http404('Post nao encontrado!')
        
    context = {
        #'text': 'Estamos no blog',
        'title':'Blog - ',
        'post': found_post,
        }
    return render(req, 'blog/post.html',context)

def exemple(req):
    context = {
        'text': 'Estamos no exemplo',
        'title':'Exemple - ',
        }
    return render(
        req,
        'blog/exemple.html',
        context,
        )