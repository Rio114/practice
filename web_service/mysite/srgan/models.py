from django.db import models
from django.core.validators import FileExtensionValidator
from datetime import datetime

class FileNameModel(models.Model):
    file_name = models.CharField(max_length = 50)
    upload_time = models.DateTimeField(default = datetime.now)
    
# class ImageData(models.Model):
#     # id
#     name = models.CharField(max_length=200)
#     #ファイルフィールドを設定する
#     image = models.FileField(upload_to='upload/%Y/%m/%d/',
#                              verbose_name='アップロード画像',
#                              validators=[FileExtensionValidator(['jpg','png','gif', ])],
#                              )
    # uploader = models.CharField(max_length=200)
    # uploadDate = models.DateField()
    # updateDate = models.DateField()
    # deleteFlg = models.BooleanField()


    # image data
    # original_name = models.CharField(max_length=200)
    # hashed_name = models.CharField(max_length=200)
    # image = models.ImageField(
    #     upload_to='images/',
    #     validators=[FileExtensionValidator(['jpg'])],
    # )

    # image = models.ImageField(
    #     upload_to='images/',
    #     verbose_name='添付画像',
    #     height_field='url_height',
    #     width_field='url_width',
    #     validators=[FileExtensionValidator(['jpg'])],
    # )

    # height = models.IntegerField(
    #     editable=False,
    # )
    # width = models.IntegerField(
    #     editable=False,
    # )


    # # upload info
    # client_ip = models.CharField(max_length=200)
    # upload_dttm = models.DateTimeField(auto_now=True)

    # # already generated sr-image?
    # generated = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.hashed_name

