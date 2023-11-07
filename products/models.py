from django.db import models 
from django.contrib.auth import get_user_model

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name="categories", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()

class Tag(models.Model):
    category = models.ForeignKey(Category, related_name="tags", on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, related_name="tags", on_delete=models.CASCADE,blank=True,null=True )
    title = models.CharField(max_length=255)
    slug = models.SlugField()

class BodyCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

class Animation(models.Model):
    name = models.CharField(max_length=255)
    file30 = models.FileField(upload_to="animations/file/%y%m%d")
    file60 = models.FileField(upload_to="animations/file/%y%m%d")
    tag = models.ForeignKey(Tag, related_name="animations", on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    preview = models.FileField(upload_to="animations/preview/%y%m%d")
    owner = models.ForeignKey(get_user_model(), related_name="my_owner_animations", on_delete=models.PROTECT, blank=True, null=True)
    downloads = models.IntegerField(default=0)
    body_category = models.ForeignKey(BodyCategory, related_name="animations", on_delete=models.CASCADE)

#learn
    def save(self, *args, **kwargs):
        if self.owner:
            self.owner.is_staff=True
            self.owner.save()
        return super().save(*args, **kwargs)

