from flask import Flask, render_template, request
import predictor
import os
import random
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)

# set paths to upload folder
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/", methods=["GET","POST"])
def predict():
    pi_est=None
    num=None
    if request.method  == "POST":
        num = int(request.form["num"])
        c,s=0,0
        pis=[]
        x_values=list(range(1,num+1))
        for i in range(num):
            x=random.uniform(-1, 1)
            y=random.uniform(-1, 1)
            if x**2 + y**2 <=1:
              c+=1
            s+=1
            pi_est = 4*c/s
            pis.append(pi_est)

        graph_path=os.path.join(os.path.join(APP_ROOT,"static"),"g.png")
        if os.path.isfile(graph_path):
            os.remove(graph_path) 
        plt.xlabel("number of points considered")
        plt.ylabel("estimated value of pi")
        plt.plot(x_values,pis)
        plt.savefig(graph_path)
        plt.close()
        pi_est=format(pi_est, ".4f")
    return render_template("index.html",pi=pi_est,selected=num)

if __name__=="__main__":
    app.run(debug=True)