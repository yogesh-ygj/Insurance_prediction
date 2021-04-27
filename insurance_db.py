from pymongo import MongoClient

myclient = MongoClient('mongodb://localhost:27017/')
db = myclient['insurance_database']
collection_user = db['user_details']
collection_prediction = db['prediction_details']

def register_user(user_data):
    user_data_dict = {}
    user_data_dict['name'] = user_data['name']
    user_data_dict['password'] = user_data['password']
    user_data_dict['mailid'] = user_data['mailid']
    user_data_dict['phone'] = user_data['phone']

    collection_user.insert_one(user_data_dict)

    return 'success'

def login_user(login_details):
    user_data_dict = {}
    user_data_dict['mailid'] = login_details['mailid']
    user_data_dict['password'] = login_details['password']
    
    response = collection_user.find_one(user_data_dict)
    if not response:
        return 'Invalid User id or Password'
    return 'Login Successfully'

def save_charges_details(age,gender,bmi,children,smoker, region,prediction):

    insurance_charges_details = {'age':age,'gender':gender,
                'bmi':bmi,'children':children,'smoker':smoker, 'region':region,'prediction':prediction}
                
    collection_prediction.insert_one(insurance_charges_details)

    return 'saved successfully'