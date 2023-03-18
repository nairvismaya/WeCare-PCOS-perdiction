from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import pickle
from flask_bootstrap import Bootstrap4
app = Flask(__name__)
Bootstrap4(app)
with open("modal/PCOSS.pkl", "rb") as f:
    loaded_model = pickle.load(f)

loaded_model=pickle.load(open("modal/PCOSS.pkl",'rb'))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/remedy")
def remedy():
    return render_template("remedy.html")


# @app.route("/sol")
# def sol():
#     return render_template("sol.html")


@app.route("/result", methods=["POST", "GET"])
def result():
    age = int(request.form['Age (yrs)'])
    bmi = float(request.form['BMI'])
    cycle = int(request.form['Cycle(R/I)'])
    cycles = int(request.form['Cycle length(days)'])
    marriage = int(request.form['Marraige Status (Yrs)'])
    pregnant = int(request.form['Pregnant(Y/N)'])
    abortions = int(request.form['No. of aborptions'])
    waist = float(request.form['Waist:Hip Ratio'])
    tsh = float(request.form['TSH (mIU/L)'])
    prl = float(request.form['PRL(ng/mL)'])
    vitd = float(request.form['Vit D3 (ng/mL)'])
    rbs = float(request.form['RBS(mg/dl)'])
    weight = int(request.form['Weight gain(Y/N)'])
    hairs = int(request.form['hair growth(Y/N)'])
    skin = int(request.form['Skin darkening (Y/N)'])
    hair = int(request.form['Hair loss(Y/N)'])
    pimples = int(request.form['Pimples(Y/N)'])
    food = int(request.form['Fast food (Y/N)'])
    exercise = int(request.form['Reg.Exercise(Y/N)'])

    form_array = np.array(
        [[age, bmi, cycle, cycles, marriage, pregnant, abortions, waist,tsh,prl,vitd,rbs, weight, hairs, skin, hair,
          pimples, food, exercise]])

    output = loaded_model.predict(form_array)
    print(output)
    if output == 1:
        return render_template("pcos.html")

    else:
        return render_template("nopcos.html")


if __name__ == "__main__":

    app.run(debug=True)
