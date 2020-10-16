import cv2
from argus_camera import ArgusCamera

def main():
    top = 250
    left = 650
    bottom = 850
    right = 950

    #camera = ArgusCamera()
    camera = ArgusCamera(stream_resolution=(1640, 1232),
                        video_converter_resolution=(1640, 1232),
                        #source_clip_rect=(0.25, 0.25, 0.75, 0.75),
                        ae_regions=[[top,left,bottom,right,0.8]])
    cv2.namedWindow("Argus Camera", cv2.WINDOW_AUTOSIZE)
    cv2.moveWindow("Argus Camera", 10,10)
    while True:
        image = camera.read()
        bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.rectangle(bgr,(left,top),(right,bottom),(255,0,255),3)
        cv2.imshow("Argus Camera", bgr)
        k = cv2.waitKey(1)
        if k & 0xFF == 27:
            cv2.destroyAllWindows()
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
