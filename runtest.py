import cv2
from argus_camera import ArgusCamera

def main():

    camera = ArgusCamera()
    cv2.namedWindow("Argus Camera", cv2.WINDOW_AUTOSIZE)
    cv2.moveWindow("Argus Camera", 50,50)
    while True:
        image = camera.read()
        
        bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imshow("Argus Camera", bgr)
        k = cv2.waitKey(1)
        if k & 0xFF == 27:
            cv2.destroyAllWindows()
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
