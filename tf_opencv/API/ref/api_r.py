import responder
import peewee
import cv2

db = peewee.SqliteDatabase("data.db")

class Images(peewee.Model):
    imagePath = peewee.TextField()
    imageRevPath = peewee.TextField()
    imageWidth = peewee.IntegerField()
    imageHeigh = peewee.IntegerField()

    class Meta:
        database = db

api = responder.API()

@api.route('/getImage/{imagePath}')
def get_image(res, resp, *, imagePath):
    try:
        image = Images.get(Images.imagePath == imagePath)
        result = {
            "result": True,
            "data": {
                "imagePath": image.imagePath,
                "imageWidth": image.imageWidth,
                "imageHeight": image.imageHeigh,
                "imageRevPath": image.imageRevPath

            }
        }    
    
    # run_sr_generator

    except Images.DoesNotExist:
        result = {
            "result": False
        }


    resp.media = result

if __name__ == '__main__':
    api.run(address="0.0.0.0", port=8888)
