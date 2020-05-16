from django.db import models

class ImageData(models.Model):
    # image data
    original_name = models.CharField(max_length=200)
    hashed_name = models.CharField(max_length=200)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    channel = models.IntegerField(default=0)

    # upload info
    client_ip = models.CharField(max_length=200)
    upload_dttm = models.DateTimeField(auto_now=True)

    # already generated sr-image?
    generated = models.BooleanField(default=False)

    def __str__(self):
        return self.hashed_name

