# pages/views.py
from django.views.generic import ListView
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.views.generic import TemplateView
#from django.views.generic.edit import CreateView # new
from django.shortcuts import render
from .forms import PostForm

from .models import Post

# class HomePageView(ListView):
#     model = Post
#     template_name = 'home.html'
#     context_object_name = 'all_posts_list' # new
#
#
# class PostCreateView(View):
#     def post(self, request):
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = PostForm()
#         return render(request, 'add.html', {'form': form})
#
#     def get(self, request):
#         form = PostForm()
#         return render(request, 'add.html', {'form': form})
#
def list_and_create_view(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
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
      'home.html', {'page': page,'objects': objects,'form': form})
