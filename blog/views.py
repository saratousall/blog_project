from django.shortcuts import render
from django.shortcuts import render ,get_object_or_404,  redirect 
from .models import Post
from .forms import PostForm

def post_list(request):
  posts = Post.objects.all().order_by('-created_at')
  
  return render(request, 'blog/post_list.html', {'posts': posts})


def details_posts(request, id):
   post=get_object_or_404(Post,id=id)
   print("#==="*40)
   print(post)
   print("#==="*40)
   return render(request, 'blog/posts_detail.html', {'post':post})
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Redirige vers la liste des posts après l'ajout
    else:
        form = PostForm()
    
        return render(request, 'blog/form.html', {'form': form})
def home(request):
     return render(request, 'blog/index.html')
    

def blog(request):
    return render(request, 'blog/blog.html')
        
# Create your views here.
