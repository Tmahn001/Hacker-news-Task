from apscheduler.schedulers.background  import BackgroundScheduler
from celery import Celery
from datetime import timedelta


import json
import requests
from .models import NewsID, News, Comment
from itertools import islice
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status, viewsets
from celery.schedules import crontab
from celery import shared_task


#def startjob():
    #scheduler = BackgroundScheduler()
    #story = NewsViewset()
    #scheduler.add_job(story.get_data, "interval", minutes=1, id="story_001", replace_existing=True)
    #scheduler.start()

