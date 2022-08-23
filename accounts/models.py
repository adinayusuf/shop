from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,
                                verbose_name='User', related_name='profile')
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True, verbose_name='Avatar')
    about_user = models.CharField(max_length=200, null=True, blank=True, verbose_name='About user')
    git = models.URLField(null=True, blank=True, verbose_name='GIT')

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
