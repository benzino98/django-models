
from django.db import models


class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Post"
        title = models.CharField(max_length=200)
        text = models.TextField(blank=True)
        author = models.ForeignKey(get_user_model())
        created_date = models.DateTimeField()
        plublished_date = models.DateTimeField()
