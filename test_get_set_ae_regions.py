import cv2
from argus_camera import ArgusCamera


def main():
    left = 650
    top = 250
    right = 950
    bottom = 550

    camera = ArgusCamera(
        stream_resolution=(1640, 1232),
        video_converter_resolution=(820, 616),
        ae_regions=[[left, top, right, bottom, 1.0]])
    cv2.namedWindow("Argus Camera", cv2.WINDOW_AUTOSIZE)
    cv2.moveWindow("Argus Camera", 10, 10)
    # IMX-219 native resolution (mode = 0): 3280x2464
    left = int(left/4)
    top = int(top/4)
    right = int(right/4)
    bottom = int(bottom/4)
    while True:
        image = camera.read()
        print(camera.getAeRegions())
        bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.rectangle(bgr, (left, top), (right, bottom), (255, 0, 255), 3)
        cv2.imshow("Argus Camera", bgr)
        k = cv2.waitKey(1)
        if k & 0xFF == 27:
            cv2.destroyAllWindows()
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
