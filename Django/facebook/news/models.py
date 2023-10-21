from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save


class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    description = models.TextField(default='')
    counter = models.PositiveIntegerField(default=0)


class Posts(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)


def ___str___(self):
    return self.title


@receiver(pre_save, sender=News)
def my_handler(sender, instance, **kwargs):
    counter = News.objects.count()
    if counter >= 75:
        News.object.order.by('created_at')[0].delete()
    print('До сохранения')


# -----------------------------------------------------------------
# def my_handler_without_decorator(sender, instance, **kwargs):
#     print('До сохранения')
#
#
# pre_save.connect(receiver=my_handler_without_decorator, sender=News)
# @receiver(post_save, sender=News)
# def my_handler_1(sender, instance, **kwargs):
#     print('После сохранения')


MAX_RECORDS = {
    'category1': 5,
    'category2': 10,
    'category3': 15
}

DEFAULT_MAX_RECORDS = 5


@receiver(pre_save, sender=Posts)
def check_max_records(sender, instance, **kwargs):
    max_records = MAX_RECORDS.get(instance.category, DEFAULT_MAX_RECORDS)

    if Posts.objects.filter(category=instance.category).count() >= max_records:
        oldest_record = Posts.objects.filter(category=instance.category).order_by('created_date').first()
        oldest_record.delete()
