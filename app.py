from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello():
    return "Hello, World!"

@app.route('/<name>',methods=['GET','POST'])
def about(name):
    return name

if __name__=='__main__':
    app.run(debug=True)