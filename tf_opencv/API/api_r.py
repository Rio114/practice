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

# @api.route('/sendImage', methods=['POST'])
# def send_image():
#     imagePath = request.data.decode()
#     height, width, channel = check_image(imagePath)

#     rev_path = imagePath.split('.')[0] + '_rev.jpg'
#     result = {
#         "result": True,
#         "data": {
#             "imagePath": imagePath,
#             "imageWidth": width,
#             "imageHeight": height,
#             "imageRevPath": rev_path
#         }
#     }

#     Images.create(imagePath=imagePath,
#             imageWidth=width,
#             imageHeigh=height,
#             imageRevPath=rev_path)

#     return make_response(jsonify(result))

# def check_image(req):
#     path = req
#     print(path)
#     img = cv2.imread(path)
#     shape = img.shape
#     h = shape[0]
#     w = shape[1]
#     c = shape[2]
#     return h, w, c

if __name__ == '__main__':
    api.run(address="0.0.0.0", port=8888)
