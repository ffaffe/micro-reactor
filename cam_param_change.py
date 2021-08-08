from time import sleep, time
import picamera

# For help see --> https://picamera.readthedocs.io/en/release-1.10/quickstart.html #

with picamera.PiCamera() as camera:
    camera.sharpness = 100
    camera.contrast = 0
    camera.brightness = 40
    camera.saturation = 50
    camera.ISO = 100                    # light sensitivity adjustement, possible values = 100,200,320,400,500,640,800 #
    camera.video_stabilization = True
    camera.exposure_compensation = 0
    camera.exposure_mode = 'auto'
    camera.meter_mode = 'average'
    camera.awb_mode = 'off'             # suposedly corrects for Noir cam daylight issues --> this is a LIE!!! Available options = auto, sunlight, cloudy, shade, tungsten, fluorescent, incandescent, flash, horizon and off (off allows adjust awb_gains) #
    camera.awb_gains = (1.1, 1.3)       # manual correction of false colour captures caused by Noir functionality (red:blue ratio), values = 0.1-->8.0 #
    camera.image_effect = 'none'
    camera.color_effects = None
    #camera.rotation = 0
    camera.hflip = True
    camera.vflip = True
    #camera.crop = (0.0, 0.0, 1.0, 1.0)

    camera.start_preview()
    sleep(5)
    camera.stop_preview()
