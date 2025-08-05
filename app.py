from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://api.adviceslip.com/advice"
    headers = {"Accept": "application/json"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            advice = data["slip"]["advice"]  # Extract the advice text
        else:
            advice = f"Failed with status code {response.status_code}: {response.reason}"
    except requests.exceptions.RequestException as e:
        advice = f"An error occurred: {e}"

    return render_template("index.html", advice=advice)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
