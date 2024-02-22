from django.shortcuts import render

from .models import Post, Author, Category

def posts(request):
    category_name = request.GET.get('category_name')
    
    print(category_name)
    
    posts = Post.objects.all()
    categories = Category.objects.all()
    
    if category_name is not None:
        posts = posts.filter(category__name=category_name)
    
    return render(request, 'app/posts.html', context={'posts': posts, 'categories': categories})

def post_detail(request, pk):
    
    post = Post.objects.filter(pk = pk).first()
    
    return render(request, 'app/post.html', context = {'post': post})
    