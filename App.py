from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return '<h1> Hi How are you ??</h1>'

@app.route('/Page1')
def Page1():
    return 'This is page 1'

@app.route('/Page2')
def Page2():
    return 'This is page 2'

@app.route('/Page3/<name>')
def Page3(name):
    return 'Hello %s and type is %s'%(name,type(name).__name__)

@app.route('/Page4/<int:ID>')
def Page4(ID):
    return 'Hello %d and type is %s'%(ID,type(ID).__name__)











if __name__=='__main__':
    app.run(debug=True)
