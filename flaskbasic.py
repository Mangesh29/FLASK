from flask import Flask ,render_template,  request, jsonify

 

app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def home_page():
    return render_template("index.html")

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
