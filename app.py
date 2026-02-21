from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("models/crop_model.pkl", "rb"))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=["POST"])
def predict():
    try:
        # Get form values
        N = float(request.form["N"])
        P = float(request.form["P"])
        K = float(request.form["K"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        # Create input array
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

        # Predict
        prediction = model.predict(data)[0]

        # Image file name (must match your image names)
        image_file = prediction.lower() + ".jpg"

        return render_template(
            "index.html",
            prediction_text="Recommended Crop: " + prediction,
            image_file=image_file
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text="Error: " + str(e)
        )


if __name__ == "__main__":
    app.run(debug=True)