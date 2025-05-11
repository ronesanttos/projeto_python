from django.shortcuts import render
# Create your views here.
def blog(req):
    context = {
        'text': 'Estamos no blog',
        'title':'Blog - '}
    return render(req, 'blog/index.html',context)

def exemple(req):
    context = {
        'text': 'Estamos no exemplo',
        'title':'Exemple - '}
    return render(
        req,
        'blog/exemple.html',
        context,
        )