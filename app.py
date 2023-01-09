from flask import Flask
from flask_api import status
import pandas as pd
import requests

app = Flask(__name__)

# DEFINING THE URL
URL = 'https://docs.google.com/spreadsheets/u/0/d/1wRVoUiLhDmchtiVRhwR2aeYNz2crWrO5/export?format=csv&id=1wRVoUiLhDmchtiVRhwR2aeYNz2crWrO5&gid=987275882'

@app.route('/')
def index():
    """
    This functions handling the operations to do when the route is the home page
    """
    # RETURNING A STATUS SUCCESS IN THE HOME PAGE
    return {'status': 'Success'}, status.HTTP_200_OK

@app.route('/status')
def status_funtion():
    
    """
    This function handling the operations to do when the route is the home page
    """
    # RETURNING A STATUS WITH THE SERVER RUNNING
    return {'status': 'Server is running'}, status.HTTP_200_OK

@app.route('/add_users')
def add_users():
    """
    This functions handling the operations to do when the route is the home page
    it read a spreadsheet by a URL next it use a for cycle to call a API user where it send a payload using the endpoint to register
    """
    try:
        # USING PANDAS READ A CSV BY A URL
        df = pd.read_csv(URL)
    except:
        # IF WE HAVE A ERROR READING THE ARCHIVE IT RETURN A MESSAGE OF ERROR
        return {'error': 'error to open file'}, status.HTTP_404_NOT_FOUND
    
    # USING A FOR CYCLE TAKE THE INFORMATION
    for i in range(len(df)):
        first_name = df.iloc[i]['first_name']
        email = df.iloc[i]['email']
        password = df.iloc[i]['password']
        
        # PAYLOAD GENERATE BY THE INFORMATION
        payload = {
            'name': first_name,
            'email': email,
            'password': password
        }
        
        # RESPONSE USING AN ENDPOINT
        API_END_POINT = 'http://127.0.0.1:8000/v1/register/'
        response = requests.post(url=API_END_POINT, data=payload)

    # RETURNING AN STATUS SUCCESSFULLY WHEN ALL USERS WERE ADD
    return {'status': 'users added successfully'}, status.HTTP_200_OK

# HOST AND PORT CONFIGURATION
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9001, debug=True)