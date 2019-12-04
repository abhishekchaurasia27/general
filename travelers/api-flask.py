from flask import Flask, request, jsonify, json
import pandas as pd
from pandas.io.json import json_normalize

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
@app.route("/home")
def home():
    return "Hello Flask"

@app.route("/data", methods=['GET', 'POST'])
def data():
    if request.method == 'GET':
        return "GET Request"
    if request.method == 'POST':
        file = request.files['file']
        #print(file.name + "---" + file.filename + '---' + file.mimetype + '---')
        df = pd.read_csv(file)
        data = request.form.get('data')
        #print(df.shape)
        #print (dir(request.data))
        #nycphil = json_normalize(ds['programs'])
        #works_data = json_normalize(data=ds['programs'], record_path='works', meta=['id', 'orchestra', 'programID', 'season'])
        #data = df.to_json(orient='records', lines=True)
        data = df.to_json()
        #return json.dumps(data, indent=4, sort_keys=True)
        return jsonify(data)
        return "output" + str(df.shape)


if __name__ == "__main__":
    app.run(debug=True)