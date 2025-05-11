from django.shortcuts import render

# Create your views here.
def home(req):
    
    context = {
        'text':'Estamos na home',
        'title':'Home - '
               }
    
    return render(
        req,
        'home/index.html',
         context,
        )