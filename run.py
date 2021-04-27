from flask import Flask, request, jsonify
import insurance_db
import test_model

app = Flask(__name__)

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        data = request.form
        response = insurance_db.register_user(data)

    return jsonify({'msg':response})

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data = request.form
        response = insurance_db.login_user(data)
    return jsonify({'msg':response})

@app.route('/predict_insurance_charges', methods=['GET', 'POST'])
def predict_insurance_charges():
    if request.method == 'POST':
        age= int(request.form['age'])
        gender = request.form['gender']
        bmi = int(request.form['bmi'])
        children = int(request.form['children']) 
        smoker = request.form['smoker']
        region =request.form['region']      
        
        print('age,gender,bmi,children,smoker, region',age,gender,bmi,children,smoker, region)
        
        ir = test_model.insurance_knn_model()
        charges  = ir.predict_charges( age,gender,bmi,children,smoker, region)

        insurance_db.save_charges_details(age,gender,bmi,children,smoker, region,charges)
        
        return 'The predicted insurance prize is rs.{}' .format(round(charges,2))
    return 'Wrong Method '

if __name__ == "__main__":
    print("Starting Python Flask Server For Insurance charges Prediction...")
    app.run(debug=False)