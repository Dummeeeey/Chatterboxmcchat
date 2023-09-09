from flask import Flask, request, jsonify
from requests import post
from sys import stderr

app = Flask("app")

@app.post("/")
def forward():
	if request.is_json:
		data = request.get_json()
		a = post(data["webhook"], data["data"])
		return str(a.status_code),201
	return {"error":"yousuckpleaselockin"},415
