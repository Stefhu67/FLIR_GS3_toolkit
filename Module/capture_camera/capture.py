import os
import PySpin
import sys

NUM_IMAGES = 1

class capture:
    def __init__(self, cam_list, count_frame):
        self.cam_list = cam_list
        self.count_frame = count_frame
    
    def capture_frame(self):
        for n in range(NUM_IMAGES):
            for i, cam in enumerate(self.cam_list):

                # Retrieve device serial number for filename
                node_device_serial_number = PySpin.CStringPtr(cam.GetTLDeviceNodeMap().GetNode('DeviceSerialNumber'))

                if PySpin.IsAvailable(node_device_serial_number) and PySpin.IsReadable(node_device_serial_number):
                    device_serial_number = node_device_serial_number.GetValue()
                print('Camera %d serial number set to %s...' % (i, device_serial_number))

                # Retrieve next received image and ensure image completion
                image_result = cam.GetNextImage()
                # Convert image to mono 8
                image_converted = image_result.Convert(PySpin.PixelFormat_Mono8, PySpin.HQ_LINEAR)
                # Save image
                filename = str(self.count_frame).zfill(4)+ '_' + str(i)+'.tif'
                image_converted.Save(filename)
                print('Image saved at %s' % filename)
                # Release image
                image_result.Release()
                print()
