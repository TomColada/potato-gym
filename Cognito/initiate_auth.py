import os
import boto3
from dotenv import load_dotenv
load_dotenv()

username = 'tomcolada'
password = '#Abc1234'
email = 'maciejhenrykowski@onet.pl'
user_pool_id = os.getenv('COGNITO_USER_POOL_ID')
app_client_id = os.getenv('COGNITO_CLIENT_ID')
confirmation_code = '842318'

client = boto3.client('cognito-idp', region_name=os.getenv('COGNITO_REGION_NAME'))
user_attributes = [{'Name': 'email', 'Value': email}]
response = client.initiate_auth(
    ClientId=os.getenv('COGNITO_CLIENT_ID'),
    AuthFlow = 'USER_PASSWORD_AUTH',
    AuthParameters={
        'USERNAME': username,
        'PASSWORD': password
        }
    )

print('AccessToken',response['AuthenticationResult']['AccessToken'])
print('RefreshToken',response['AuthenticationResult']['RefreshToken'])