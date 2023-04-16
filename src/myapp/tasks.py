from __future__ import absolute_import, unicode_literals
import logging

from django.conf import settings
from mydjango.celery import app

logger = logging.getLogger("celery")


@app.task
def show_hello_world():
    logger.info("-"*25)
    logger.info("Aplication from celery")
    logger.info("-"*25)
