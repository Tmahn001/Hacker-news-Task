from django.urls import path

from .views import NewsIdView, NewsItemView, home, story, userPost,\
    PostEdit, PostDelete, PostDetailView, CreatePost, searchBar, ErrorView

urlpatterns = [


    path('all-items', NewsIdView.as_view(), name='index'),
    path('hackernews/', NewsItemView.as_view(), name='news-item'),
    path('', home, name='home'),
    path('story/', story, name='story'),
    path('user/', userPost, name='user-items'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('news/add', CreatePost.as_view(), name='add_post'),
    path('search/', searchBar, name='search'),
    path('error', ErrorView.as_view(), name='edit_error')





]