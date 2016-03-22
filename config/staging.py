import os
from datetime import timedelta

DEBUG = True
SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERYBEAT_SCHEDULE = {
    'example_task': {
        'task': 'tasks.example_task',
        'schedule': timedelta(minutes=2),
        'args': ()
    },
}

ERROR_404_HELP = False
