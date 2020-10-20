import cv2
import numpy as np

from argus_camera import ArgusCamera


def shift_ae_region(ae_region: np.ndarray, mode_resolution: tuple = (3280, 2464)):
    """
    In-place
    """
    offset = 10
    w = ae_region[2] - ae_region[0]
    h = ae_region[3] - ae_region[1]
    ae_region[0] += offset
    ae_region[2] += offset
    if ae_region[2] >= mode_resolution[0]:
        ae_region[0] -= mode_resolution[0] - w
        ae_region[2] -= mode_resolution[0] - w
        ae_region[1] += h
        ae_region[3] += h
    if ae_region[3] >= mode_resolution[1]:
        ae_region[1] -= mode_resolution[1] - h
        ae_region[3] -= mode_resolution[1] - h


def main():
    # ae_regions = list of list of xmin, xmax, ymin, ymax, weight
    ae_region = np.array([0, 0, 400, 400, 1.0], dtype=np.float32)
    camera = ArgusCamera(
        stream_resolution=(1640, 1232),
        video_converter_resolution=(820, 616),
        ae_regions=[ae_region.tolist()])
    cv2.namedWindow("Argus Camera", cv2.WINDOW_AUTOSIZE)
    cv2.moveWindow("Argus Camera", 10, 10)
    # IMX-219 native resolution (mode = 0): 3280x2464
    while True:
        r = camera.setAeRegions([ae_region.tolist()])
        # print(r)
        # print(camera.getAeRegions())
        image = camera.read()

        bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        b = (ae_region[:4]/4).astype(np.int32)
        cv2.rectangle(bgr, (b[0], b[1]), (b[2], b[3]), (255, 0, 255), 3)
        cv2.imshow("Argus Camera", bgr)
        k = cv2.waitKey(1)
        if k & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            print("Exiting...")
            break
        shift_ae_region(ae_region)


if __name__ == "__main__":
    main()
