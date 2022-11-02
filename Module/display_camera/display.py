import cv2
import PySpin
import numpy as np

cam_resolution = (1280, 1024)

class display:
    def __init__(self, cam, cameras):
        self.cam = cam
        self.cameras = cameras
    
    def cv_display(self):
        while True:
            key = cv2.waitKey(1)
            if key == 32: # space
                cv2.destroyAllWindows()
                break
    
            for j, self.cam in enumerate(self.cameras):
                try:
                    self.cam.TriggerSoftware()
                    i = self.cam.GetNextImage()

                    # retrieve id cams
                    node_device_serial_number = PySpin.CStringPtr(self.cam.GetTLDeviceNodeMap().GetNode('DeviceSerialNumber'))
                    device_serial_number = node_device_serial_number.GetValue()
                    #print('Camera %d serial number set to %s...' % (j, device_serial_number))
                    #print(i.GetWidth(), i.GetHeight(), i.GetBitsPerPixel())

                    if i.IsIncomplete():
                        pass
                    else:
                        cam_id = self.cam.GetUniqueID()
                        image_converted = i.Convert(PySpin.PixelFormat_BGR8, PySpin.DIRECTIONAL_FILTER)
                        image_data = image_converted.GetData()
                        cvi = np.frombuffer(image_data, dtype=np.uint8)
                        cvi = cvi.reshape((i.GetHeight(),i.GetWidth(),3))
                        res = cv2.resize(cvi, cam_resolution)
                        line = cv2.line(res, (int(cam_resolution[0]/2), 0), (int(cam_resolution[0]/2),int(cam_resolution[1])), (0, 0, 255), 2)
                        line = cv2.line(res, (0, int(cam_resolution[1]/2)), (int(cam_resolution[0]),int(cam_resolution[1]/2)), (0, 0, 255), 2)
                        cv2.imshow("cam {}".format(device_serial_number),line)

                    i.Release()
                    del i

                except PySpin.SpinnakerException as ex:
                    print("Error: {}".format(ex))