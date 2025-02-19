from django.urls import path
from .views import post_list
from .views import details_posts
from .views import post_create
from .views import home
from .views import blog
urlpatterns = [
             path('form/',post_create,name='post_create'),
             path('posts/', post_list, name='post_list'),
             path('posts/<int:id>', details_posts, name='details_posts'),
             path('home/', home, name='index'),
             path('blog/', blog, name='about'),
]