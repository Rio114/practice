import peewee

db = peewee.SqliteDatabase("data.db")

class Images(peewee.Model):
    imagePath = peewee.TextField()
    imageRevPath = peewee.TextField()
    imageWidth = peewee.IntegerField()
    imageHeigh = peewee.IntegerField()

    class Meta:
        database = db

Images.create_table()
Images.create(imagePath='image.jpg',
imageRevPath='image_rev.jpg',
imageWidth=1920,
imageHeigh=1080,
)