#pragma once

#include <cstdint>
#include <vector>
#include <memory>

#define WIDTH_IDX 0
#define HEIGHT_IDX 1
#define ONE_SECOND_NANOS 1000000000
#define EXPOSURE_DEFAULT_LOW 0 
#define EXPOSURE_DEFAULT_HIGH 9999999999999

class ArgusCameraConfig
{
public:

  void setDeviceId(uint32_t deviceId) { mDeviceId = deviceId; };
  uint32_t getDeviceId() { return mDeviceId; };

  void setSourceClipRect(std::vector<float> sourceClipRect) { mSourceClipRect = sourceClipRect; };
  std::vector<float> getSourceClipRect() { return mSourceClipRect; };

  void setStreamResolution(std::vector<uint32_t> streamResolution) { mStreamResolution = streamResolution; };
  std::vector<uint32_t> getStreamResolution() { return mStreamResolution; };

  void setVideoConverterResolution(std::vector<uint32_t> videoConverterResolution) { mVideoConverterResolution = videoConverterResolution; };
  std::vector<uint32_t> getVideoConverterResolution() { return mVideoConverterResolution; };

  void setFrameDurationRange(std::vector<uint64_t> frameDurationRange) { mFrameDurationRange = frameDurationRange; };
  std::vector<uint64_t> getFrameDurationRange() { return mFrameDurationRange; };

  void setSensorMode(uint32_t sensorMode) { mSensorMode = sensorMode; };
  uint32_t getSensorMode() { return mSensorMode; };

  void setExposureTimeRange(std::vector<uint64_t> exposureTimeRange) { mExposureTimeRange = exposureTimeRange; };
  std::vector<uint64_t> getExposureTimeRange() { return mExposureTimeRange; };

  void setExposureCompensation(float ExposureCompensation) { mExposureCompensation = ExposureCompensation; };
  float getExposureCompensation() { return mExposureCompensation; };

  void setAeRegions(std::vector<std::vector<float> > AeRegions) { mAeRegions = AeRegions; };
  std::vector<std::vector<float> > getAeRegions() { return mAeRegions; };

  void setWbGains(std::vector<float> gains) { mWbGains = gains; };
  std::vector<float> getWbGains() { return mWbGains; };

  void setAwbMode(uint32_t mode) { mAwbMode = mode; };
  uint32_t getAwbMode() { return mAwbMode; }

  void setAwbLock(bool AwbLock) { mAwbLock = AwbLock; };
  bool getAwbLock() { return mAwbLock; };

  void setAeLock(bool AeLock) { mAeLock = AeLock; };
  bool getAeLock() { return mAeLock; };

  void setGainRange(std::vector<float> gainRange) { mGainRange = gainRange; };
  std::vector<float> getGainRange() { return mGainRange; };

  void setDenoiseMode(uint32_t denoiseMode) { mDenoiseMode = denoiseMode; };
  uint32_t getDenoiseMode() { return mDenoiseMode; };

  void setDenoiseStrength(float denoiseStrength) { mDenoiseStrength = denoiseStrength; };
  float getDenoiseStrength() { return mDenoiseStrength; };

  void setEdgeEnhanceMode(uint32_t edgeEnhanceMode) { mEdgeEnhanceMode = edgeEnhanceMode; };
  uint32_t getEdgeEnhanceMode() { return mEdgeEnhanceMode; };

  void setEdgeEnhanceStrength(float edgeEnhanceStrength) { mEdgeEnhanceStrength = edgeEnhanceStrength; };
  float getEdgeEnhanceStrength() { return mEdgeEnhanceStrength; };

  void setIspDigitalGainRange(std::vector<float> ispDigitalGainRange) { mIspDigitalGainRange = ispDigitalGainRange; };
  std::vector<float> getIspDigitalGainRange() { return mIspDigitalGainRange; };

  void setAeAntibandingMode(uint32_t aeAntibandingMode) { mAeAntibandingMode = aeAntibandingMode; };
  uint32_t getAeAntibandingMode() { return mAeAntibandingMode; };

  bool mAwbLock;
  bool mAeLock;
  uint32_t mDeviceId;
  uint32_t mSensorMode;
  uint32_t mAwbMode;
  std::vector<float> mWbGains;
  float mExposureCompensation;
  std::vector<uint32_t> mStreamResolution;
  std::vector<uint32_t> mVideoConverterResolution;
  std::vector<uint64_t> mExposureTimeRange;
  std::vector<uint64_t> mFrameDurationRange;
  std::vector<float> mGainRange;
  std::vector<float> mSourceClipRect;
  std::vector<std::vector<float>> mAeRegions;
  uint32_t mDenoiseMode;
  float mDenoiseStrength;
  uint32_t mEdgeEnhanceMode;
  float mEdgeEnhanceStrength;
  std::vector<float> mIspDigitalGainRange;
  uint32_t mAeAntibandingMode;

  std::vector<uint32_t> getOutputShape() {
    return { mVideoConverterResolution[HEIGHT_IDX], mVideoConverterResolution[WIDTH_IDX], getNumChannels() };
  };

  size_t getOutputSizeBytes();
  uint32_t getNumChannels();
};

ArgusCameraConfig DEFAULT_DEVKIT_CONFIG()
{
    ArgusCameraConfig c;
    c.mAwbLock = false;
    c.mAeLock = false;
    c.mDeviceId = 0;
    c.mExposureCompensation = 0.;
    c.mSensorMode = 0;
    c.mGainRange = {0.0, 300.0};
    c.mSourceClipRect = { 0.0, 0.0, 1.0, 1.0 };
    c.mStreamResolution = { 640, 480 };
    c.mVideoConverterResolution = { 640, 480 };
    c.mFrameDurationRange = { ONE_SECOND_NANOS / 30, ONE_SECOND_NANOS / 30 }; // 30fps
    c.mExposureTimeRange = { EXPOSURE_DEFAULT_LOW,EXPOSURE_DEFAULT_HIGH };
    c.mDenoiseMode = 0;
    c.mDenoiseStrength = 0.0;
    c.mEdgeEnhanceMode = 0;
    c.mEdgeEnhanceStrength = 0.0;
    c.mIspDigitalGainRange = {0.0, 300.0};
    c.mAeAntibandingMode = 0;
    c.mAwbMode = 0;
    return c;
}

class IArgusCamera
{
public:
  static IArgusCamera *createArgusCamera(const ArgusCameraConfig &config, int *info=nullptr);
  virtual ~IArgusCamera() {};
  virtual int read(uint8_t *data) = 0;
};

