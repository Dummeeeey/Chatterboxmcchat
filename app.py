from flask import Flask, request, jsonify
from requests import post

app = Flask("app")

@app.post("/")
def forward():
	if request.is_json:
		data = request.get_json()
		post(data["webhook"], data["data"])
		return 201
	return 415