from django.db import models
from datetime import datetime
from django.db.models.fields import DateTimeField
from django.urls import reverse

# Create your models here.
class UCDateTimeField(DateTimeField):

    def pre_save(self, model_instance, add):
        if self.auto_now or (self.auto_now_add and add):
            value = datetime.datetime.now()
            setattr(model_instance, self.attname, value)
            return value
        else:
            value = getattr(model_instance, self.attname)
            if not isinstance(value, datetime):
                # assume that the value is a timestamp if it is not a datetime
                value = datetime.fromtimestamp(int(value))
                # an exception might be better than an assumption
                setattr(model_instance, self.attname, value)
            return super(UCDateTimeField, self).pre_save(model_instance, add)


class News(models.Model):
    title = models.CharField(max_length=200, blank = True, null = True)
    hackernews_id = models.BigIntegerField(unique=True, primary_key=True)
    time = UCDateTimeField(default=datetime.now)
    category = models.CharField(max_length=50, blank = True, null = True)
    post_url = models.CharField(max_length=200, blank = True, null = True, default='http://stoplight.io/prism/')
    author = models.CharField(max_length=50, blank = True, null = True)
    path = models.CharField(max_length=50, blank = True, null = True, default='user')

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.hackernews_id)])

class Comment(models.Model):
    author_id = models.BigIntegerField(blank=True, null=True, default=153636)
    text = models.TextField(blank=True, null=True)
    by = models.CharField(max_length=200, blank = True, null = True)
    time = UCDateTimeField(default=datetime.now)





#ignore this model, this method did not work
class NewsID(models.Model):
    hackernews = models.BigIntegerField(unique=True, primary_key=True)
    time = models.DateTimeField(default=datetime.now())

    def save(self, *args, **kwargs):
        self.id = self.hackernews
        super(NewsID, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.hackernews)