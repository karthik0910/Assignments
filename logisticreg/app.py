from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle


app = Flask(__name__)


@app.route('/', methods=['GET'])
@cross_origin()
def homepage():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def index():
    try:
        intercept = 1
        age = int(request.form['age'])
        years_married = int(request.form['years_married'])
        religious = int(request.form['religious'])
        children = int(request.form['children'])
        marriage_rating = int(request.form['marriage_rating'])
        edu = int(request.form['edu'])
        wif_occupation = request.form['wif_occupation']
        if wif_occupation == "farming":
            occ_2 = 1
            occ_3 = 0
            occ_4 = 0
            occ_5 = 0
            occ_6 = 0
        elif wif_occupation == "white_collar":
            occ_2 = 0
            occ_3 = 1
            occ_4 = 0
            occ_5 = 0
            occ_6 = 0
        elif wif_occupation == "teacher":
            occ_2 = 0
            occ_3 = 0
            occ_4 = 1
            occ_5 = 0
            occ_6 = 0
        elif wif_occupation == "managerial":
            occ_2 = 0
            occ_3 = 0
            occ_4 = 0
            occ_5 = 1
            occ_6 = 0
        elif wif_occupation == "professional":
            occ_2 = 0
            occ_3 = 0
            occ_4 = 0
            occ_5 = 0
            occ_6 = 1
        else:
            occ_2 = 0
            occ_3 = 0
            occ_4 = 0
            occ_5 = 0
            occ_6 = 0

        hus_occupation = request.form["hus_occupation"]

        if hus_occupation == "farming":
            occ_husb_2 = 1
            occ_husb_3 = 0
            occ_husb_4 = 0
            occ_husb_5 = 0
            occ_husb_6 = 0
        elif hus_occupation == "white_collar":
            occ_husb_2 = 0
            occ_husb_3 = 1
            occ_husb_4 = 0
            occ_husb_5 = 0
            occ_husb_6 = 0
        elif hus_occupation == "teacher":
            occ_husb_2 = 0
            occ_husb_3 = 0
            occ_husb_4 = 1
            occ_husb_5 = 0
            occ_husb_6 = 0
        elif hus_occupation == "managerial":
            occ_husb_2 = 0
            occ_husb_3 = 0
            occ_husb_4 = 0
            occ_husb_5 = 1
            occ_husb_6 = 0
        elif hus_occupation == "professional":
            occ_husb_2 = 0
            occ_husb_3 = 0
            occ_husb_4 = 0
            occ_husb_5 = 0
            occ_husb_6 = 1
        else:
            occ_husb_2 = 0
            occ_husb_3 = 0
            occ_husb_4 = 0
            occ_husb_5 = 0
            occ_husb_6 = 0
        filename = 'finilized_model.pickle'
        loaded_model = pickle.load(open(filename, 'rb'))
        prediction = loaded_model.predict([[intercept, age, years_married, religious, children, edu, marriage_rating,
                                            occ_2, occ_3, occ_4, occ_5, occ_6, occ_husb_2, occ_husb_3, occ_husb_4,
                                            occ_husb_5, occ_husb_6]])
        if prediction[0]==0:
            return render_template('results.html', prediction="Woman doesn't have an affiar")
        else:
            return render_template('results.html', prediction="Woman have an affiar")

    except KeyError:
        msg = 'Unknown error'
        try:
            msg = json_object['message']
        except KeyError:
            pass

        print(msg)
        return render_template('results.html', error=msg)


if __name__ == '__main__':
    app.run(debug=True)