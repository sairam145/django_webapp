# from django.db import models
#
# # Create your models here.
# class Blog(models.Model):
#     sno = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=200)
#     meta = models.CharField(max_length=300)
#     content = models.TextField()
#     thumbnail_img = models.ImageField(null=True, blank=True, upload_to="images/")
#     thumbnail_url = models.URLField(blank=True, null=True)
#     category = models.CharField(max_length=255, default="uncategorized")
#     slug = models.CharField(max_length=100)
#     time = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return self.title

from django.db import models

class Project(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()  # Changed from meta to description for clarity
    thumbnail_img = models.ImageField(null=True, blank=True, upload_to="images/")
    thumbnail_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=255, default="uncategorized")  # Consider using a ManyToManyField for categories if needed
    slug = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # Changed from DateField to DateTimeField for more precision

    def __str__(self):
        return self.title
