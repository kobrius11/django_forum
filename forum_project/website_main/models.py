from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext as _

from datetime import datetime

user = get_user_model()

# Create your models here.
class TimeModule(models.Model):
    date_created = models.TimeField(
        _("time created"),
        name="time_created",  
        editable=False,
        default=datetime.now,
    )
    date_edited = models.TimeField(
        _("time edited"),
        name="time_edited",  
        editable=True,
        default=datetime.now,
    )

    class Meta:
        abstract = True


class Post(TimeModule):
    title = models.CharField(verbose_name=_("title"), name="title", max_length=500, editable=True, default="please provide post title")
    content = models.CharField(verbose_name=_("content"), name="content", max_length=5000, editable=True)
    author = models.ForeignKey(user, on_delete=models.CASCADE, related_name="posts")
    
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return "{}, date_created".format(self.author)

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})


class Comment(TimeModule):
    content = models.CharField(verbose_name=_("content"), name="content", max_length=5000, editable=True)
    author = models.ForeignKey(user, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return "{}, {}".format(self.author, self.date_created)

    def get_absolute_url(self):
        return reverse("Comments_detail", kwargs={"pk": self.pk})