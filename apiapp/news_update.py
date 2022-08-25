from apscheduler.schedulers.background  import BackgroundScheduler
from apiapp.views import NewsViewset

def startjob():
    scheduler = BackgroundScheduler()
    story = NewsViewset()
    scheduler.add_job(story.get_data, "interval", minutes=5, id="story_001", replace_existing=True)
    scheduler.start()