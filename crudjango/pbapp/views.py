# pages/views.py
from django.views.generic import ListView
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.views.generic import TemplateView
#from django.views.generic.edit import CreateView # new
from django.shortcuts import render
from .forms import PostForm
from crud.models import Member

from .models import Post

def list_and_create_view(request, id):
    member = Member.objects.get(id=id)
    key2select = Post.objects.filter(myowner=member)
    form = PostForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.myowner = member
        post.save()
        form = PostForm()

    # notice this comes after saving the form to pick up new objects
    objects = Post.objects.all()
    paginator = Paginator(objects, 3)# 3 posts in each page
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer deliver the first page
        objects = paginator.page(1)
    except EmptyPage:
        #If page is out of range deliver last page of results
        objects = paginator.page(paginator.num_pages)
    return render(request,
      'home.html', {'page': page,'key2select': key2select,'objects': objects,'form': form})
