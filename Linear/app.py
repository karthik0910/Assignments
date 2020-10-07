from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)


@app.route('/', methods=['GET'])
@cross_origin()
def homepage():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def index():
    try:
        crim = float(request.form['crim'])
        zn = float(request.form['zn'])
        indus = float(request.form['indus'])
        chas = float(request.form['chas'])
        nox = float(request.form['nox'])
        rm = float(request.form['rm'])
        age = float(request.form['age'])
        dis = float(request.form['dis'])
        tax = float(request.form['tax'])
        ptratio = float(request.form['ptratio'])
        b = float(request.form['b'])
        lstat = float(request.form['lstat'])
        scaler = StandardScaler()
        filename = 'finalized_model.pickle'
        loaded_model = pickle.load(open(filename, 'rb'))
        prediction = loaded_model.predict(scaler.fit_transform([[crim, zn, indus, chas, nox, rm,
                                                             age, dis, tax, ptratio, b, lstat]]))
        return render_template('results.html', prediction=prediction[0])
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
