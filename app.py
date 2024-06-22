from flask import Flask,render_template,request,redirect
import os
from werkzeug.utils import secure_filename
import mouth_cancer  as mc
import breast_cancer as bc

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def welcome():
    return render_template('index.html')
@app.route('/getstarted')
def get_started():
    return render_template('getstarted.html')
@app.route('/getstarted/breast_cancer')
def breast_cancer():
    return render_template('breast_cancer.html')
@app.route('/knowmore')
def know_more():
    return render_template('knowmore.html')
@app.route('/about')
def about_us():
    return render_template('about.html')
@app.route('/contact_us')
def contact():
    return render_template('contact.html')
@app.route('/submit',methods=['POST'])
def submit():
    data=[]
    print(data)
    for i in range(1,19):
        data.append(request.form['f'+str(i)])
    result=bc.predict(data)
    print(result)
    if (result==1):
        return 'I am sorry to say that your tumor is malignent'
    return 'your tumor is begign'
@app.route('/getstarted/mouth_cancer')
def mouth_cancer():
    return render_template('mouth_cancer.html')
@app.route('/submit1', methods = ['POST'])
def upload_file():
    if 'image' not in request.files:
        return redirect(request.url)
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # Process the image here
        path1 = 'uploads/'+filename
        prediction = mc.make_prediction(path1)[0][0]
        print(prediction)
        return render_template('mouth_cancer_result.html',prediction =prediction*100)
@app.route('/submit1', methods = ['POST'])
def upload_file1():
    if 'image' not in request.files:
        return redirect(request.url)
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # Process the image here
        path1 = 'uploads/'+filename
        prediction = mc.make_prediction(path1)[0][0]
        print(prediction)
        return render_template('mouth_cancer_result.html',prediction =prediction*100)
@app.route('/getstarted/skin_cancer')    
def skin_cancer():
    return render_template('skin_cancer.html')
@app.route('/submit2', methods = ['POST'])
def upload_file2():
    if 'image' not in request.files:
        return redirect(request.url)
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # Process the image here
        path1 = 'uploads/'+filename
        prediction = mc.make_prediction(path1)
        if prediction[0][0]>0.9 :
            prediction='Positive'
        else:
            prediction= 'Negative'   
        print(prediction)
        return render_template('mouth_cancer_result.html',prediction =prediction)
        
    

app.run(debug=True)