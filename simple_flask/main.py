from flask import Flask

app = Flask("name")


@app.route("/")
def first_template():

	return "hello world"

app.run(host="0.0.0.0", port = 5000)
