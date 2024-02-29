from flask import Flask,render_template,request
import joblib

app=Flask(__name__)

model=joblib.load('svc_model1.joblib')

@app.route('/')
def index():
    return render_template('index1.html')

def make_prediction(mean_radius, mean_texture):
    mean_radius=float(mean_radius)
    mean_texture=float(mean_texture)
    
    input_data=[[mean_radius, mean_texture]]
    prediction=model.predict(input_data)

    return prediction[0]

@app.route('/predict',methods=['POST'])
def predict_endpoint():
    if request.method=='POST':
        mean_radius=request.form['mean_radius']
        mean_texture=request.form['mean_texture']
        

        prediction =make_prediction(mean_radius, mean_texture)
        if prediction==0:
            output='malignant'
        else:
            output='benign'
        return render_template('irisout.html',prediction=output)


if __name__=='__main__':
    app.run(debug=True)

    
