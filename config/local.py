from datetime import timedelta

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/flask_example'
# SQLALCHEMY_ECHO = True
CELERY_BROKER_URL = 'sqla+postgresql://localhost/flask_example'
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERYBEAT_SCHEDULE = {
    'example_task': {
        'task': 'tasks.example_task',
        'schedule': timedelta(seconds=10),
        'args': ()
    },
}

ERROR_404_HELP = False
