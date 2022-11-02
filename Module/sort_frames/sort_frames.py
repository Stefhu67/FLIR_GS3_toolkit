import os
import glob
import re

class sort_file:
    def __init__(self, test_name):
        self.test_name = test_name
    
    def sort_frames(self):
        frames = glob.glob('*.tif')
        frames.sort()
        n_test = 0

        if not os.path.exists(self.test_name + str(n_test).zfill(2)):
            os.makedirs(self.test_name + str(n_test).zfill(2))
            for each_frame in frames:
                os.rename(each_frame, self.test_name + str(n_test).zfill(2) + '/' + each_frame)
            n_test += 1
        else:
            while os.path.exists(self.test_name + str(n_test).zfill(2)) == True:
                n_test +=1
            os.makedirs(self.test_name + str(n_test).zfill(2))
            for each_frame in frames:
                os.rename(each_frame, self.test_name + str(n_test).zfill(2) + '/' + each_frame)
            n_test += 1
