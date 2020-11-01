from flask import Flask, render_template, request, send_file
from flask_cors import cross_origin
import pickle
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier


app = Flask(__name__)

@app.route('/', methods = ['GET'])
@cross_origin()
def homepage():
    return render_template("index.html")

@app.route("/data",methods = ["POST"])
def data():
    try:
        file = request.form["filename"]
        data = pd.read_excel(file)
        data = data.iloc[1:, ]
        data.reset_index(drop=True, inplace=True)
        inp = data.drop(columns = ["attributes"])
        for i in range(0, len(data.attributes)):
            data["attributes"][i] = data["attributes"][i].replace(".", "")
        columns = ["workclass", "education", "marital_status", "occupation", "relationship", "race", "sex","native_country", "attributes"]
        for i in columns:
            data[i] = data[i].str.strip()
        # Replacing "?" values with Mode
        data["workclass"].replace("?", data["workclass"].mode()[0], inplace=True)
        sch = ["1st-4th", "5th-6th", "7th-8th", "9th", "10th"]
        hsgrad = ["11th", "12th"]
        data["education"].replace(to_replace=sch, value="elementary_school", inplace=True)
        data["education"].replace(to_replace=hsgrad, value="HS-grad", inplace=True)
        married = ["Married-civ-spouse", "Divorced", "Separated", "Widowed", "Married-spouse-absent", "Married-AF-spouse"]
        unmarried = ["Never-married"]
        data["marital_status"].replace(to_replace=married, value="married", inplace=True)
        data["marital_status"].replace(to_replace=unmarried, value="unmarried", inplace=True)
        data["occupation"].replace("?", data["occupation"].mode()[0], inplace=True)
        data["native_country"].replace("?", data["native_country"].mode()[0], inplace=True)
        x = data.drop(columns=["attributes"])
        y = data["attributes"]
        num_cols = ["age", "fnlwgt", "education_num", "capital_gain", "capital_loss", "hours_per_week"]
        cat_cols = ["workclass", "education", "marital_status", "occupation", "relationship", "race", "sex","native_country"]
        # converting the character variables into dummy values
        dumm = pd.get_dummies(x[cat_cols])
        # scaling the data using MinMaxScaler
        scaler = MinMaxScaler()
        scaled_data = scaler.fit_transform(x[num_cols])
        # converting the data into dataframes
        scaled_data = pd.DataFrame(scaled_data, columns=num_cols)
        dumm.drop(columns=["workclass_Never-worked", "education_Preschool", "marital_status_unmarried", "occupation_Armed-Forces","relationship_Wife", "race_Other", "sex_Female"], inplace=True)
        # Combning the scaled and dummy variable data
        x_inp = pd.concat([scaled_data, dumm], axis=1)
        filename = 'finalized_model.pickle'
        loaded_model = pickle.load(open(filename, 'rb'))
        prediction = loaded_model.predict(x_inp)
        prediction = pd.DataFrame(prediction,columns = ["Predicted"])
        data_shown = pd.concat([data.iloc[:,1:],prediction],axis=1)
        data_shown.to_csv('Prediction_download.csv', index=False)
        return render_template("results.html",data = data_shown.head(5).to_html())

    except KeyError:
        msg = 'Unknown error'
        try:
            msg = json_object['message']
        except KeyError:
            pass
        print(msg)
        return render_template('results.html', error=msg)

@app.route('/download', methods=['POST'])
def download():
    return send_file('Prediction_download.csv', mimetype='text/csv',attachment_filename='Prediction_download.csv', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)



        
