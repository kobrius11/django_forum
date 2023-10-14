from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.
class UserProfile(models.Model):
    owner = models.ForeignKey(get_user_model(), verbose_name=_("owner"), on_delete=models.CASCADE)
    picture = models.ImageField(
        _("profile picture"), 
        upload_to=None, 
        height_field=None, 
        width_field=None, 
        max_length=None, 
        null= True, 
        blank=True
    )
    

    class Meta:
        verbose_name = _("user profile")
        verbose_name_plural = _("user profiles")

    def __str__(self):
        return "{}, profile".format(self.owner.get_username())

    def get_absolute_url(self):
        return reverse("userprofile_detail", kwargs={"pk": self.pk})

    
