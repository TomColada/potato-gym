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
response = client.confirm_sign_up(
    ClientId=os.getenv('COGNITO_CLIENT_ID'),
    Username=username,
    ConfirmationCode = confirmation_code
    )

print(response)