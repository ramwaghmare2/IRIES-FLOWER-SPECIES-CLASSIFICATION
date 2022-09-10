import pickle 
import json 
import numpy as np
import config

class IrisSpecies:
    def __init__(self,SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):
        self.SepalLengthCm= SepalLengthCm
        self.SepalWidthCm =SepalWidthCm
        self.PetalLengthCm =PetalLengthCm
        self.PetalWidthCm =PetalWidthCm
        
    def get_data(self):
        with open(config.MODEL_PATH,'rb') as f :
            self.model = pickle.load(f)
    
        with open(config.PROJECT_PATH,'r') as f :
            self.project_data= json.load(f)
            
    def get_result(self):
        self.get_data()
        test_array = np.zeros(len(self.project_data['columns']))
        test_array[0] = self.SepalLengthCm
        test_array[1]=  self.SepalWidthCm
        test_array[2]= self.PetalLengthCm
        test_array[3]= self.PetalWidthCm
        
        result = self.model.predict([test_array])
        return result[0]