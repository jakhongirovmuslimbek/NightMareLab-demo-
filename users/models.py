from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ImageSpecField
from imagekit.processors import Transpose

class UserProfile(AbstractUser):
    USER_TYPE = ()
    image = models.FileField(upload_to="users/%y/%m/%d/", blank=True, null=True)
    thumbnail_image = ImageSpecField(
        source = 'image',
        processors = [Transpose(),],
        format = 'JPEG',
        options = {'quality':60}
    )
    middle_name = models.CharField(max_length=255, blank=True, null=True)

    @property
    def type_user(self):
        type = ""
        if self.is_superuser:
            type = "admin"
        elif self.is_staff:
            type = "seller"
        else:
            type = "user"
        return type

#learn
    @property
    def owner_animations(self):
        if len(self.my_owner_animations.all()):
            return self.my_owner_animations.all()
        return None

    @property
    def user_animations(self):
        if len(self.my_animations.all()):
            return self.my_animations.all()
        return None
