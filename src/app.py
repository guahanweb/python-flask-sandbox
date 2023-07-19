from flask import Flask
from flask import render_template

import os

import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

import logging
config = {
    "DYNAMODB_ENDPOINT": os.getenv("DYNAMODB_ENDPOINT"),
    "AWS_REGION": os.getenv("AWS_REGION"),
}
print(config)
logger = logging.getLogger(__name__)

def checkTables():
    endpoint = config['DYNAMODB_ENDPOINT']
    client = boto3.resource('dynamodb', endpoint_url=endpoint)
    response = list(client.tables.all())
    print(response)

def main():
    checkTables()
    app = Flask(__name__)

    @app.get("/")
    def home():
        return render_template('home.html', title="Home")
    
    return app

if __name__ == "__main__":
    # checkTables()
    app = main()
    app.run(host='0.0.0.0')
