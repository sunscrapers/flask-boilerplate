from app import create_celery_app

celery = create_celery_app()


def run_celery():
    celery.worker_main(['', '-B'])


@celery.task()
def example_task():
    print('Hello celery!')
