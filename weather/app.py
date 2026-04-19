from flask import Flask, render_template, request
import requests
import os
app = Flask(__name__)

API_KEY = os.getenv("API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None

    if request.method == "POST":
        city = request.form["city"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        data = requests.get(url).json()

        if data["cod"] != 200:
            weather_data = {"error": "City not found"}
        else:
            weather_data = {
                "city": city,
                "main": data["weather"][0]["main"],
                "desc": data["weather"][0]["description"],
                "temp": round(data["main"]["temp"] - 273.15, 2),
                "temp_max": round(data["main"]["temp_max"] - 273.15, 2),
                "temp_min": round(data["main"]["temp_min"] - 273.15, 2),
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "wind": round(data["wind"]["speed"] * 3.6, 2)
            }

    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000))