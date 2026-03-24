from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# تحميل الموديل
model, vectorizer = pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    email_text = request.form["email"]

    # تحويل النص لارقام
    text_vec = vectorizer.transform([email_text])

    # التوقع
    prediction = model.predict(text_vec)[0]

    if prediction == 1:
        result = "Spam Email 🚨"
    else:
        result = "Not Spam ✅"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
