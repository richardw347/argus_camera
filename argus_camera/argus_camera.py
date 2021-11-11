import numpy as np
from .cpp import *
from past.builtins import long

class ArgusCamera:
    """
    Argus Camera Python wrapper
    """

    def __init__(
            self, 
            device_id=0, 
            stream_resolution = (1280, 720), 
            video_converter_resolution = (640, 480),
            frame_duration_range = (int(1e9//30), int(1e9//30)),
            exposure_time_range = (long(0), long(999999999)),
            source_clip_rect = (0.0, 0.0, 1.0, 1.0),
            gain_range = (0., 300.),
            ae_regions = None,
            sensor_mode=0,
            denoise_mode=0,
            denoise_strength=0.0,
            edge_enhance_mode=0,
            edge_enhance_strength=0.0,
            isp_digital_gain_range = (0., 300.),
            ae_antibanding_mode=0,
            awb_lock=True,
            awb_mode=0,
            wb_gains = (0, 0, 0, 0)):

        self.device_id = device_id

        self.video_converter_resolution = video_converter_resolution

        self.config = DEFAULT_DEVKIT_CONFIG()
        self.config.setDeviceId(device_id)
        self.config.setStreamResolution(stream_resolution)
        self.config.setVideoConverterResolution(video_converter_resolution)
        self.config.setFrameDurationRange(frame_duration_range)
        self.config.setSourceClipRect(source_clip_rect)
        self.config.setSensorMode(sensor_mode)
        self.channels = 4

        #   Addition Exposure and AE
        self.config.setExposureTimeRange(exposure_time_range)
        self.config.setExposureCompensation(0)
        self.config.setGainRange(gain_range)
        self.config.setAeLock(True)
        self.config.setAwbLock(awb_lock)
        self.config.setAwbMode(awb_mode)
        self.config.setIspDigitalGainRange(isp_digital_gain_range)
        self.config.setAeAntibandingMode(ae_antibanding_mode)
        self.config.setWbGains(wb_gains)

        # Set denoise and edge enhancement
        self.config.setDenoiseMode(denoise_mode)
        self.config.setDenoiseStrength(denoise_strength)
        self.config.setEdgeEnhanceMode(edge_enhance_mode)
        self.config.setEdgeEnhanceStrength(edge_enhance_strength)

        if ae_regions is not None:
            aeRegion_arr = np.asarray(ae_regions, dtype=np.float32)
            aer_shape = aeRegion_arr.shape
            if not (len(aer_shape) == 2 and aer_shape[0] and aer_shape[1] == 5):
                raise ValueError("ae_regions value error")
            self.config.setAeRegions(aeRegion_arr.tolist())

        self.camera = IArgusCamera_createArgusCamera(self.config)
        
        self.read_error_code = -1
        
        # ret = IArgusCamera_createArgusCamera(self.config)
        
        # if (isinstance(ret, (tuple, list))) :
        #     self.camera, self.camera_error_code = ret
        # elif isinstance(ret, int) :
        #     self.camera = None
        #     self.camera_error_code = ret
        # else:
        #     raise NotImplementedError
        print(type(self.camera))

        
    # def isOpened(self) -> bool:
        """
        Return the initialization status of the camera.

        RETURN
        ------
        bool
            If true, the camera successfully initialized.
        """
        # return not self.camera_error_code

    def read(self):
        image = np.empty(list(self.video_converter_resolution)[::-1] + [self.channels], np.uint8)
        self.camera.read(image.ctypes.data)
        return image[:,:,:3]
