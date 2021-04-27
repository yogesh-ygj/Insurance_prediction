import pickle
import json
import numpy as np
file_path = 'Model/knn_model.pickle'
model = pickle.load(open(file_path,'rb'))

class insurance_knn_model():

    def predict_charges(self, age,gender,bmi,children,smoker, region):
        with open("Model/columns1.json", "r") as f:
            data_columns = json.load(f)['data_coumns']
            locations_list = data_columns

        region = region.lower()
        location_index= locations_list.index (region)
        z=np.zeros(len(locations_list))
        z[0]= age
        
        if gender == 'male': 
            z[1] = 1
        else:
            z[1] = 0
            
        z[2] = bmi
        z[3] = children
        
        if smoker == 'yes': 
            z[4] = 1
        else:
            z[4] = 0 
        z[location_index]= 1
        
        return model.predict([z])[0]

if __name__ == "__main__":
    ir = insurance_knn_model()
    charges  = ir.predict_charges( 30,'male',39,0,'yes', 'r_southwest')
    print("The Predicted charges are :",round(charges,2))