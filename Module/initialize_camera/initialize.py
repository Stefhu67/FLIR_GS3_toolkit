import PySpin

class initialize:
    def __init__(self, cam, cam_list, system, cameras, gain, exposure_time, black_level, gamma, sharpness):
        self.cam = cam
        self.cam_list = cam_list
        self.system = system
        self.cameras = cameras
        self.gain = gain
        self.exposure_time = exposure_time
        self.black_level = black_level
        self.gamma = gamma
        self.sharpness = sharpness

    def set_trigger_mode_software(self):
        self.cam.TriggerMode.SetValue(PySpin.TriggerMode_Off)
        self.cam.TriggerSource.SetValue(PySpin.TriggerSource_Software)
        self.cam.TriggerMode.SetValue(PySpin.TriggerMode_On)
        print("set trigger mode software")

    def reset_trigger_mode_software(self):
        self.cam.TriggerMode.SetValue(PySpin.TriggerMode_Off)
        print("reset trigger mode")
    
    def set_parameters(self):
        self.cam.GainAuto.SetValue(PySpin.GainAuto_Off)
        self.cam.Gain.SetValue(float(self.gain))
        self.cam.ExposureAuto.SetValue(PySpin.ExposureAuto_Off)
        self.cam.ExposureTime.SetValue(min(self.cam.ExposureTime.GetMax(), float(self.exposure_time)))
        self.cam.BlackLevel.SetValue(float(self.black_level))
        self.cam.Gamma.SetValue(float(self.gamma))
    
    def acquisition_display(self):
        if self.cam_list.GetSize() == 0:
            print('Not enough cameras!')
            input('Done! Press Enter to exit...')
            self.system.ReleaseInstance()
            del self.system
            sys.exit()

        for i in range(self.cam_list.GetSize()):
            self.cam = self.cam_list.GetByIndex(i)
            print("camera {} serial: {}".format(i, self.cam.GetUniqueID()))
            self.cam.Init()
            self.cam.AcquisitionMode.SetValue(PySpin.AcquisitionMode_Continuous)
            self.set_trigger_mode_software()
            self.set_parameters()
            self.cam.BeginAcquisition()
            self.cameras.append(self.cam)
            print("begin acquisition")

    def acquisition_capture(self):
        if self.cam_list.GetSize() == 0:
            self.cam_list.Clear()
            system.ReleaseInstance()
            print('Not enough cameras!')
            input('Done! Press Enter to exit...')

        for i, cam in enumerate(self.cam_list):
            # Set acquisition mode to continuous
            cam.Init()
            node_acquisition_mode = PySpin.CEnumerationPtr(cam.GetNodeMap().GetNode('AcquisitionMode'))
            node_acquisition_mode_continuous = node_acquisition_mode.GetEntryByName('Continuous')
            acquisition_mode_continuous = node_acquisition_mode_continuous.GetValue()
            node_acquisition_mode.SetIntValue(acquisition_mode_continuous)
            cam.BeginAcquisition()
            print('Camera %d started acquiring images...' % i)