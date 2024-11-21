from flask import Flask, render_template, request, jsonify
from weather_logic import get_weather

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    city = request.form.get("city")
    if not city:
        return jsonify({"error": "City is required!"})

    weather_data = get_weather(city)
    return jsonify(weather_data)

if __name__ == "__main__":
    app.run(debug=True)
