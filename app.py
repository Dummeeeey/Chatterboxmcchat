from flask import Flask, request, jsonify
from requests import post

app = Flask("app",host="0.0.0.0")

@app.post("/")
def forward():
	print("recieved")
	if request.is_json:
		data = request.get_json()
		post(data["webhook"], data["data"])
		return 201
	return 415
