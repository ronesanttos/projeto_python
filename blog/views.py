from django.shortcuts import render
from blog.data import posts

# Create your views here.
def blog(req):
    context = {
        'text': 'Estamos no blog',
        'title':'Blog - ',
        'posts': posts,
        }
    return render(req, 'blog/index.html',context)

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