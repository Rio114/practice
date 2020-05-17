import urllib.request
import json
import argparse

URL = 'http://localhost:8888/getImage/'
DATA_DIR = 'data/'

def get_image(image_file):
    url = URL + image_file
    try:
        with urllib.request.urlopen(url) as response:
            body = json.loads(response.read())
            result = body['result']
            output = body['output']

            print(result)
            print(output)

    except urllib.error.URLError as e:
        print(e.reason)

def main():
        # parse path
    parser = argparse.ArgumentParser()
    parser.add_argument("image_file", help="only for .jpg files")
    args = parser.parse_args()
    image_file = args.image_file
    
    get_image(image_file)

if __name__ == '__main__':
    main()