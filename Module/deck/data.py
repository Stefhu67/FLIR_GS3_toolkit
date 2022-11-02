import yaml, sys
import numpy as np
import os.path

class Deck():
    def __init__(self, inputhpath):
        if not os.path.exists(inputhpath):
            print("File " + inputhpath)
            sys.exit(1)
        else:
            with open(inputhpath,'r') as f:
                ## Container of the tags parsed from the yaml file
                self.doc = yaml.load(f, Loader=yaml.BaseLoader)
                self.Camera_parameters = self.doc['Camera_parameters']
                self.gain = self.Camera_parameters['gain']
                self.exposure_time = self.Camera_parameters['exposure_time']
                self.black_level = self.Camera_parameters['black_level']
                self.gamma = self.Camera_parameters['gamma']
                self.sharpness = self.Camera_parameters['sharpness']

                self.Experience_parameters = self.doc['Experience_parameters']
                self.framerate = self.Experience_parameters['framerate']
                self.test_name = self.Experience_parameters['test_name']