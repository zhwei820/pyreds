from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(
        '文章标题',
        max_length=300,
    )
    txt = models.TextField(
        '文章内容'
    )
    num_read = models.IntegerField(
        '阅读量',
        default=0,
        db_index=True,
        blank=True,
    )
    num_like = models.IntegerField(
        '点赞量',
        default=0,
        db_index=True,
        blank=True,
    )
    create_time = models.DateTimeField(
        'create_time',
        auto_now_add=True,
        db_index=True,
    )
    update_time = models.DateTimeField(
        'update_time',
        auto_now=True,
        db_index=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章信息'
        verbose_name_plural = verbose_name
