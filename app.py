from flask import Flask, request, jsonify
from requests import post
from sys import stderr

app = Flask("app")

@app.post("/")
def forward():
	if request.is_json:
		data = request.get_json()
		print(data["webhook"], file=stderr)
		print(data["data"], file=stderr)
		post(data["webhook"], data["data"])
		return data,201
	return {"error":"yousuckpleaselockin"},415
