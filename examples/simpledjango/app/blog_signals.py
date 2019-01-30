# coding: utf-8

from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from .models import Blog
from utils.reds_cli import search_cli


@receiver(post_save, sender=Blog)
def save_blog_log(sender, instance, **kwargs):
    search_cli.index(instance.title + instance.txt, instance.id)
