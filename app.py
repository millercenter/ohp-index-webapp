from flask import Flask
import boto3
import json

ssm = boto3.client('ssm', region_name='us-east-1')

app = Flask(__name__)


@app.route('/')
def index_rte():
    db = ssm.get_parameter(Name='/ohp-index-webapp/dbname')
    db = db['Parameter']['Value']
    return "Hello world! " + db

@app.route('/tt')
def tt_rte():
    return "yeah it worked"

@app.route('/test')
def test_rte():
    #db = ssm.get_parameter(Name='/ohp-index-webapp/dbname')
    #db = db['Parameter']['Value']
    db = 'blah'
    return "Hello, World: " + db

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5002)
