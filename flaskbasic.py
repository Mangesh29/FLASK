from flask import Flask ,render_template,  request, jsonify

 

app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def home_page():
    return render_template("index.html")

@app.route('/math',methods=['POST'])
def math_ops():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(ops == 'add'):
            r = num1+ num2
            addresult= "sum  of "+ str(num1) + str(num2) +"is"+str(r)

        elif(ops == 'subtract'):
            r = abs(num1- num2)
            addresult= "subtract of "+ str(num1) + str(num2) +"is"+str(r)

        elif(ops == 'multiply'):
            r = num1* num2
            addresult= "multiply  of "+ str(num1) + str(num2) +"is"+str(r)

        elif(ops == 'divide'):
            r = num1/ num2
            addresult= "divide by "+ str(num1) + str(num2) +"is"+str(r)
                
        return render_template('result.html',result=addresult)   


# @app.route("/")
# def hello_world():
#     return "<h1 hello, world </h1>"

# @app.route("/test")
# def test2():
#     data = request.args.get('x')
#     return "this is data input from my url :{}".format(data)

# @app.route("/login")
# def test3():
#     return "<h1>logeed in!</h1>"

if __name__ =="__main__":
    app.run(host="0.0.0.0")
