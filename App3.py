from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)


@app.route('/')
def home():
    return render_template('home2.html')


@app.route('/formpage',methods=['GET','POST'])
def formpage():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        return render_template('formpage.html',name=name,age=age)
    return redirect('home')


@app.route('/marklist',methods=['GET','POST'])
def marklist():
    if request.method=='POST':
        subj1=request.form['sub1']
        subj2=request.form['sub2']
        subj3=request.form['sub3']
        mark1=request.form['m1']
        mark2=request.form['m2']
        mark3=request.form['m3']
        mlist={
            subj1:mark1,
            subj2:mark2,
            subj3:mark3
        }
        return render_template('marklist.html',data=mlist)


if __name__=='__main__':
    app.run(debug=True)