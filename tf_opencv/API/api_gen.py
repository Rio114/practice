import responder

from asyncio import sleep
from datetime import datetime

from generate_sr_image import SrImage

SRC_DIR = 'data/'

api = responder.API()

@api.route('/getImage/{image_file}')
async def get_image(res, resp, *, image_file):
    output_file = await generate(image_file)

    result = {
            "input": image_file,
            "output": output_file
            }

    if output_file != False:
        result['result'] = True
    else:
        result['result'] = False

    resp.media = result

async def generate(image_file):
    obj = SrImage(SRC_DIR)
    return obj.generate(image_file)

if __name__ == '__main__':
    api.run(address="0.0.0.0", port=8888)