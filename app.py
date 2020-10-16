
from flask import Flask,render_template,request
import pickle 


model=pickle.load(open('final_model.pkl','rb'))

app=Flask(__name__,)

@app.route('/')

def fun1():
    return render_template('home.html')


@app.route('/predict',methods=['POST'])

def home():
    d1=request.form['age']
    d2=request.form['anaemia']
    d3=request.form['creatinine_phosphokinase']
    d4=request.form['diabetes']
    d5=request.form['ejection_fraction']
    d6=request.form['high_blood_pressure']
    d7=request.form['platelets']
    d8=request.form['serum_creatinine']
    d9=request.form['serum_sodium']
    d10=request.form['gender']
    d11=request.form['smoking']

    inp=[[int(d1),int(d2),int(d3),int(d4),int(d5),int(d6),int(d7),float(d8),int(d9),int(d10),int(d11)]]

    pred=model.predict(inp)
  
    #print(inp,pred)

    return render_template('final.html',data=pred)















if __name__=="__main__":
    app.run(debug=True)