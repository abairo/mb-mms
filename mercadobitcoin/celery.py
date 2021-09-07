import os
from celery.schedules import crontab
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mercadobitcoin.settings')
app = Celery('mercadobitcoin')

app.conf.beat_schedule = {
    'import-yesterday-every-day': {
        'task': 'apps.mms.tasks.import_yesterday',
        'schedule': crontab(hour=0, minute=1),
    },
    'check-missing-days-every-4-hour': {
        'task': 'apps.mms.tasks.import_yesterday',
        'schedule': crontab(minute='*/60'),
    },
}


# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


from celery.signals import task_failure
@task_failure.connect()
def celery_task_failure_email(**kwargs):
    from django.core.mail import mail_admins
    import socket
    subject = "[Django][{queue_name}@{host}] Error: Task {sender.name} ({task_id}): {exception}".format(
        queue_name="celery",
        host=socket.gethostname(),
        **kwargs
    )
    message = """Task {sender.name} with id {task_id} raised exception:
{exception!r}Task was called with args: {args} kwargs: {kwargs}.The contents of the full traceback was:{einfo}
    """.format(
        **kwargs
    )

    mail_admins(subject, message)
