from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    res = requests.get("https://api.thecatapi.com/v1/images/search?limit=10")
    data = res.json()

    nasa_response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2020-1-1")
    nasa_data = nasa_response.json()
    return render_template('index.html', data=data, nasa_data=nasa_data)

app.run(host='0.0.0.0', port=8080)