import requests

data = {"data": "Flask-API"}
#with open("../Demographic_Statistics_By_Zip_Code.csv", 'r') as f:
    #data = f.read()
    #print(dir(f))

#files = {'file': open('C:\\Users\\Abhishek\\Downloads\\train.csv', 'rb')}
files = {'file': open('C:\\Users\\Abhishek\\Downloads\\Demographic_Statistics_By_Zip_Code.csv', 'rb')}

#headers = {'Content-type': 'application/x-url-encoded'}
res = requests.post("http://localhost:5000/data", files=files, data=data)
#res = requests.post("http://localhost:5000/data", data=data)

print(res.content)
