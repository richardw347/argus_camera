import cv2
from argus_camera import ArgusCamera


def main():
    camera = ArgusCamera(
        stream_resolution=(1640, 1232),
        video_converter_resolution=(820, 616),
        edge_enhance_mode=2,
        edge_enhance_strength=1.0)
    cv2.namedWindow("Argus Camera", cv2.WINDOW_AUTOSIZE)
    cv2.moveWindow("Argus Camera", 10, 10)
    while True:
        image = camera.read()
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imshow("Argus Camera", image)
        k = cv2.waitKey(1)
        if k & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
