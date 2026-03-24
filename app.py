from flask import Flask, render_template,request
app = Flask(__name__)
@app.route('/')
def home():
  return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
  email_text=request.form['email']

  if 'free' in email_text.lower():
    result = 'spam'
  else:
    result = 'Not Spam'
  return render_template('index.html',prediction=result)
if __name__=='__main__':
  app.run()
