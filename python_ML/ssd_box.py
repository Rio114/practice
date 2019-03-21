import numpy as np

def Center2Corner(rects): 
    """
    Center:[cx, cy, w, h] 
    -> Coerner:[left_upper_x, left_upper_y, right_lower_x, right_lower_y]
    """
    left_upper_x = rects[:,0] - rects[:,2]/2
    left_upper_y = rects[:,1] - rects[:,3]/2
    right_lower_x = rects[:,0] + rects[:,2]/2
    right_lower_y = rects[:,1] + rects[:,3]/2
    return np.vstack([left_upper_x, left_upper_y, right_lower_x, right_lower_y]).T

def Edge2Center(rects): 
    """
    Edge:[left_upper_x, left_upper_y, w, h] 
    -> Center:[cx, cy, w, h]
    """
    cx = rects[:,0] + rects[:,2]/2
    cy = rects[:,1] + rects[:,3]/2
    return np.vstack([cx, cy, rects[:,2], rects[:,3]]).T

def generate_feature_map(imgage_size, feat_size): 
    """
    Arguments
        image_size : shape(width, height)
        feat_size : shape(m,n)
    
    Return
        feature_maps : shape(m, n, map_dim)
        map_dim: Center:[cx, cy, w, h]

    """
    im_w = imgage_size[0]
    im_h = imgage_size[1]
    w = im_w / feat_size[0]
    h = im_h / feat_size[1]
    feat_map = np.ones([feat_size[0], feat_size[1], 4])
    for i in range(feat_size[0]):
        for j in range(feat_size[1]):
            feat_c_x = w / 2 + 1 + i * w
            feat_c_y = h / 2 + 1 + j * h
            feat_map[i,j,:] = np.array((feat_c_x, feat_c_y, feat_w, feat_h))
    return feat_map.astype(np.int32)

def generate_scales(smin, smax, num_map):
    """
    smin: 0-1
    smax: 0-1 > smin
    num_map: int > 1
    """
    return smin + (smax - smin) / (num_map - 1) * np.array([k for k in range(num_map+1)])

def generate_default_boxes(imgage_size, feat_map, feat_aspect, scale): #scale = (sk[i], sk[i+1])
    length = imgage_size[0]

    def_boxes = []

    for feat in feat_map:
        for j, ar in enumerate(feat_aspects[i]):
            if ar == 1:
                sk1 = [(scale[0] * scale[1]) ** 0.5, scale[0]]
                for sk in sk1:
                    w = int(length * sk * ar **0.5)
                    h = int(length * sk * (1/ar) ** 0.5)
                    def_boxes.append([feat[0],feat[1], w, h])
            else:
                    w = int(length * scale[0] * ar **0.5)
                    h = int(length * scale[0] * (1/ar) ** 0.5)
                    def_boxes.append([feat[0],feat[1], w, h])
    return np.array(def_boxes) 

def normalize(target, ref): # ref might be default box
    cx = (target[0] - ref[0]) / ref[2]
    cy = (target[1] - ref[1]) / ref[3]
    w = np.log(target[2]/ref[2])
    h = np.log(target[3]/ref[3])
    return np.array([cx, cy, w,h])

def smoothL1(target, ref):
    diffs = target - ref
    for m in range(4):
        if np.abs(diffs[m]) > 1:
            diffs[m] = np.abs(diffs[m])  -  0.5
        else:
            diffs[m] = 0.5 *np.abs(diffs[m]) ** 2
    return diffs.sum()

def box_area(box): #box = [cx, cy, w, h]
    return box[2] * box[3]

def boxes_area(boxes):
    """
    boxes = np.array(n, 4) 
    center:[cx, cy, w, h]
    """
    return boxes[:, 2] * boxes[:, 3]

def intersection(tar_box, ref_box):# todo: when indexes are out of range
    ref_area = cvtToPos(ref_box) # pos = (xmin, ymin, xmax, ymax)
    tar_area = cvtToPos(tar_box)
    
    x_min_max = np.maximum(ref_area[0], tar_area[0])
    x_max_min = np.minimum(ref_area[2], tar_area[2])
    
    intersection_x = np.maximum(0, x_max_min - x_min_max)
    
    y_min_max = np.maximum(ref_area[1], tar_area[1])
    y_max_min = np.minimum(ref_area[3], tar_area[3])
    
    intersection_y = np.maximum(0, y_max_min - y_min_max)
    
    pixels = intersection_x * intersection_y

    return pixels

def iou(tar_box, ref_box):
    return intersection(tar_box, ref_box)/(box_area(tar_box) + box_area(ref_box))