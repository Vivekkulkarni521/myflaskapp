from flask import Flask
app = flask(__name__)
@app.route("/")
def Hello():
	return "Hello Flask"
app.run(host="0.0.0.0",port=5000)

