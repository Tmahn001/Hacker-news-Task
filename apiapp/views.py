from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView, TemplateView
import json
import requests
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .serializers import NewsSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



from .models import NewsID, News, Comment
from itertools import islice
from celery import Celery
from celery.schedules import crontab
from celery import shared_task


# Create your views here.
class NewsViewset(viewsets.ModelViewSet):
    def get_data(request):
        headers = {'content-type': 'application/json'}
        url = f'https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty'
        response = requests.get(url)
        data = response.json()
        all_posts = {}
        print("synching")

        top_100 = islice(data, 20)
        for item in top_100:
            url = f'https://hacker-news.firebaseio.com/v0/item/{item}.json?print=pretty'
            response = requests.get(url)
            data = response.json()
            item = [data]
            for post in item:
                if "url" in post:
                    news_data = News(
                        title=post['title'],
                        category=post['type'],
                        post_url=post['url'],
                        hackernews_id=post['id'],
                        author=post['by'],
                        time=post['time'],
                        path = 'hackernews'

                    )

                else:
                    news_data = News(
                        title=post['title'],
                        category=post['type'],
                        hackernews_id=post['id'],
                        author=post['by'],
                        time=post['time'],
                        path = 'hackernews'

                    )
                if 'kids' in data:
                    print(data['kids'])
                    for item in data['kids']:
                        url = f'https://hacker-news.firebaseio.com/v0/item/{item}.json?print=pretty'
                        response = requests.get(url)
                        comment = response.json()
                        comment_data = Comment(
                            author_id = comment.get('parent'),
                            text = comment.get('text'),
                            by = comment.get('by'),
                            time = comment.get('time'),

                        )
                        comment_data.save()



                news_data.save()

@shared_task()
def run_task():
    NewsViewset.get_data(request=requests)





def home(request):
    all_posts = News.objects.all().order_by('-time')
    comments = Comment.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(all_posts, 20)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context ={
        "posts": posts,
        "comments": comments

    }

    return render(request, 'news_api/home.html', context)

def story(request):
    all_posts = News.objects.all().order_by('-time')
    filter_posts = News.objects.filter(category='story').all().order_by('-time')
    page = request.GET.get('page', 1)

    paginator = Paginator(filter_posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'news_api/story.html', {"posts": posts})



def userPost(request):
    items = News.objects.filter(path='user').all().order_by('-time')
    context = {
        'items': items
    }
    return render(request, 'news_api/deletable.html', context)

class PostEdit(UpdateView):
    model = News
    template_name = 'news_api/update_item.html'
    fields = ['title', 'post_url', 'category']




def detail_view(request, id):
    context = {}

    # add the dictionary during initialization
    context["news"] = News.objects.get( hackernews_id = id )
    context["comments"] = Comment.objects.all()

    return render(request, 'news_api/post_detail.html', context)


class PostDelete(DeleteView):
    model = News
    template_name = 'news_api/delete_item.html'

class CreatePost(CreateView):
    model = News
    template_name = 'news_api/add.html'
    fields = ['title', 'hackernews_id', 'category', 'post_url', 'author']

def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            posts = News.objects.filter(title__icontains=query)
            return render(request, 'news_api/search.html', {'posts': posts})
        else:
            print("no info")
            return request(request, 'search.html', {})

class ErrorView(TemplateView):
    template_name = 'news_api/error.html'
    model = News


def run(request):
    url = f'https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty'
    response = requests.get(url)
    data = response.json()
    all_posts = {}
    print("synching")

    top_10 = islice(data, 2)
    for item in top_10:
        url = f'https://hacker-news.firebaseio.com/v0/item/{item}.json?print=pretty'
        response = requests.get(url)
        data = response.json()
        item = [data]
        for post in item:
            id = [post['kid']]
            print(len(id))
    return render(request)


















class NewsIdView(APIView):
  permission_classes = [AllowAny]

# get a list of all news ids from hacker news
  def get(self, request, format=None):

    NEWS_URL = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'

    headers = {'user-agent': 'quickcheck/0.0.1'}
    response = requests.get(NEWS_URL, headers=headers)

    result = response.text.split(',')[1:len(response.text.split(','))-2]  # to trim the last element
    last = response.text.split(',')[-1]  #got this from API " 499287535 ] /n" --> reshaped to that below
    result.insert(len(result), last.strip().split()[0]) # "499287535"

    res = [int(id.strip()) for id in result] # list comprehension to strip each element of the data

    return Response(res, status=status.HTTP_200_OK)


class NewsItemView(APIView):
    permission_classes = [AllowAny]

    def get_data_from_API(self):
        """
            This helps to return
            formatted data fetched from endpoint provided
            using request.
        """
        # latest = HackerNewsID.objects.all()[len(HackerNewsID.objects.all())-1].hackernews # getting latest id from db
        result = []
        half = 0
        total = len(NewsID.objects.all()) # getting the total ids from the db

        #slicing into half based on even or odd total
        if total % 2 == 0:
            half = len(NewsID.objects.all()) / 2
        else:
            half = (len(NewsID.objects.all()) / 2) + 1

        ids = NewsID.objects.all()[:half] #slicing the queryset to get last half

        for id in ids:
            NEWS_URL = f'https://hacker-news.firebaseio.com/v0/item/{str(id)}.json?print=pretty'
            headers = {'user-agent': 'quickcheck/0.0.1'}
            response = requests.get(NEWS_URL, headers=headers)
            data = json.loads(response.text)
            result.append(data)

        return result


#GET the latest hackernews streamed
    def get(self, request, format=None):
        return Response(self.get_data_from_API(),status=status.HTTP_201_CREATED)




