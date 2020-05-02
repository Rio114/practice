import argparse
import cv2

def main():
    # parse path
    parser = argparse.ArgumentParser()
    parser.add_argument("video_path", help="hogehogehoge")
    args = parser.parse_args()
    path = args.video_path

    output_path = path.split('.')[0] + '_r.mp4'

    # read video
    cap = cv2.VideoCapture(path) # 引数がファイルパス
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 動画の画面横幅
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 動画の画面縦幅
    fcnt = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # 総フレーム数
    fps = cap.get(cv2.CAP_PROP_FPS) #
     
    print('file path:', path)
    print('width:',  width)
    print('height:',  height)
    print('frame_count:',  fcnt)
    print('frame_rate:',  fps)

    # Set output video infomation.
    fourcc = cv2.VideoWriter_fourcc('D', 'I','V','3')
    vw = cv2.VideoWriter(output_path, fourcc, fps, (width, height), True)

    # Make the output video.
    print('Making a video...')

    while(cap.isOpened()):
        ret, img = cap.read()
        if ret == True:
            vw.write(img)  # Add frame
        else:
            break

    # Post processing.
    cap.release()
    cv2.destroyAllWindows()

    print('output path:', output_path)

        
if __name__ ==  "__main__":
    main()
