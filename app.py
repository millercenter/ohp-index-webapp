from flask import Flask
import boto3
import json

ssm = boto3.client('ssm')

app = Flask(__name__)


@app.route('/')
def hello_world():
    db = ssm.get_parameter(Name='/ohp-index-webapp/dbname')
    db = db['Parameter']['Value']
    return "Hello, World: " + db

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5002)
