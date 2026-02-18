from flask import Flask, render_template, request
import pickle
import re

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

def extract_features(url):
    return [
        len(url),
        url.count('.'),
        1 if "https" in url else 0,
        1 if re.search(r'\d', url) else 0
    ]

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        url = request.form["url"]
        features = [extract_features(url)]
        prediction = model.predict(features)[0]
        result = "Phishing ⚠️" if prediction == 1 else "Legitimate ✅"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
