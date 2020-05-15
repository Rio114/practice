import cv2

def register_image(path):
    img = cv2.imread(path)
    shape = img.shape
    h = shape[0]
    w = shape[1]
    c = shape[2]

    return h, w, c
