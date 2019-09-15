from flask import Flask
app = Flask(__name__)

@app.route("/<name>")
def hello(name):
  return "Hello, " + name.capitalize()

if __name__ == "__main__":
  app.run(debug=True)
