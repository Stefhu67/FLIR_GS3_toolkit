from Module import *
import argparse
import cv2
import  time

deck = Deck('./deck.yaml')
Yaml_parameters = deck.doc

# Retrieve singleton reference to system object
system = PySpin.System.GetInstance()
# Retrieve list of cameras from the system
cam_list = system.GetCameras()
cam = cam_list.GetSize()
cameras = []
print('Number of cameras detected: %d' % cam)
print("1 : Display cameras")
print("2 : Capture images")
code = input("Choose the option : ")

#______________________________________
# Display cameras
if code == "1":

    initialize(cam, cam_list, system, cameras, deck.gain, deck.exposure_time, deck.black_level, deck.gamma, deck.sharpness).acquisition_display()

    display(cam, cameras).cv_display()

#_________________________________________________
# Capture frames

if code == "2":
    initialize(cam, cam_list, system, cameras, deck.gain, deck.exposure_time, deck.black_level, deck.gamma, deck.sharpness).acquisition_capture()

    count_frame = 0
    try:
        while True:
            capture(cam_list, count_frame).capture_frame()
            time.sleep(1/float(deck.framerate))
            count_frame += 1
    except KeyboardInterrupt:
        pass
    # Sort Images
    sort_file(deck.test_name).sort_frames()

#_________________________________________________
# End Acquisition
for cam in cam_list:
    cam.EndAcquisition()
    cam.TriggerMode.SetValue(PySpin.TriggerMode_Off)
    print("reset trigger mode")
    cam.DeInit()
    del cam
del cameras
del cam_list

system.ReleaseInstance()
del system

#_________________________________________________

input('Done! Press Enter to exit...')

