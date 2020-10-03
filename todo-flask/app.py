from flask import Flask           # import flask
app = Flask("python+app_in_aws")             # create an app instance

@app.route("/<name>")                   # at the end point /
def hello(name):                      # call method hello
    return "Hello " + name + " I am successful!"         # which returns "hello world"
if __name__ == "__main__":        # on running python app.py
    app.run(debug = True)                     # run the flask app
