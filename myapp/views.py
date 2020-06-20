from django.contrib import messages
#from django.contrib.redirects.models import Redirect
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from myapp.models import Category, Image


# Create your views here.
def homepage(request):
    cats=Category.objects.all()
    image=Image.objects.all()
    data={'cats':cats,'image':image}
    return render(request,'homepage.html',data)

def show_category_page(request,cid):
    cats=Category.objects.all()
    category=Category.objects.get(pk=cid)
    image=Image.objects.filter(cat=category)
    data = {'cats':cats, 'image': image}
    return render(request,'homepage.html', data)

def Search(request):
    search_element=request.GET['search']
    match = Image.objects.filter(Q(title__icontains=search_element))
    if match:
        # data = Image.objects.get(title=match)
        return render(request, 'search.html', {'data': match})
    else:
        message="no record found"
        return render(request,'search.html',{'message':message})








