from flask import Flask, request, jsonify
from requests import post

app = Flask("app")

@app.post("/")
def forward():
	print("recieved")
	if request.is_json:
		data = request.get_json()
		post(data["webhook"], data["data"])
		return data,201
	return {"error":"yousuckpleaselockin"},415
