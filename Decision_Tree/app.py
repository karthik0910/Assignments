from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)

@app.route('/', methods=['GET'])
@cross_origin()
def homepage():
    return render_template('index.html')


@app.route('/predict', methods = ['POST'])
def index():
    df = pd.read_xlsx()
    try:
        age = int(request.form['age'])
        sibsp = int(request.form['sibsp'])
        parch = int(request.form['parch'])
        fare = int(request.form['fare'])
        sex = request.form['sex']
        if sex == 'male':
            sex_male = 1
        else:
            sex_male = 0
        deck_class = request.form['class']
        if deck_class == 'first_class':
            pclass_1  = 1
            pclass_2  = 0
        elif deck_class == 'second_class':
            pclass_1 = 0
            pclass_2 = 1
        else:
            pclass_1 = 0
            pclass_2 = 0

        scaler = StandardScaler()
        filename = 'finilized_model.pickle'
        loaded_model = pickle.load(open(filename, 'rb'))
        prediction = loaded_model.predict(scaler.fit_transform([[age, sibsp, parch, fare, sex_male, pclass_1, pclass_2]]))
        if prediction[0] == 1:
            return render_template('results.html', prediction="Yay the person has survived")
        else:
            return render_template('results.html', prediction="Rest In Peace")
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






