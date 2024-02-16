from flask import Flask,render_template,request
import joblib

app=Flask(__name__)

model=joblib.load('knn_model1.joblib')

@app.route('/')
def index():
    return render_template('index2.html')

def predict_iris(sepal_length,sepal_width,petal_length,petal_width):
    sepal_length=float(sepal_length)
    sepal_width=float(sepal_width)
    petal_length=float(petal_length)
    petal_width=float(petal_width)

    input_data=[[sepal_length,sepal_width,petal_length,petal_width]]

    prediction=model.predict(input_data)

    return prediction[0]

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        sepal_length=request.form['sepal_length']
        sepal_width=request.form['sepal_width']
        petal_length=request.form['petal_length']
        petal_width=request.form['petal_width']

        prediction=predict_iris(sepal_length,sepal_width,petal_length,petal_width)
        if prediction==1:
            output='Setosa'
        elif prediction==2:
            output='Versicolor'
        else:
            output='Virginica'

        return render_template('irisout.html',prediction=output)



if __name__=='__main__':
    app.run(debug=True)


