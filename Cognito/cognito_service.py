import boto3
import os
from botocore.exceptions import ClientError
from dotenv import load_dotenv
load_dotenv()

class CognitoService():
    """
    A class representing a service for interacting with Amazon Cognito for user registration and login.

Attributes:
    - COGNITO_USER_POOL_ID (str): The ID of the Cognito user pool.
    - COGNITO_REGION_NAME (str): The region of the Cognito user pool.
    - COGNITO_CLIENT_ID (str): The app client ID associated with the Cognito user pool.
    - client (boto3.client): An instance of the Boto3 Cognito Identity Provider client.

Methods:
    - register_user(email: str, password: str, user_type: str) -> dict:
        Registers a new user in the Cognito user pool.

        Parameters:
            - email (str): The email address of the user.
            - password (str): The password for the user.

        Returns:
            - dict: A dictionary containing the response from the Cognito service.


        Example:
            ```python
            cognito_service = CognitoService()
            response = cognito_service.register_user(username = "johndoe", email="user@example.com", password="password123")
            print(response)
            ```

    - login_user(email: str, password: str) -> dict:
        Logs in a user with the provided credentials in the Cognito user pool.

        Parameters:
            - email (str): The email address of the user.
            - password (str): The password for the user.

        Returns:
            - dict: A dictionary containing the response from the Cognito service.


        Example:
            ```python
            cognito_service = CognitoService()
            response = cognito_service.login_user(email="user@example.com", password="password123")
            print(response)
            ```
    """

    def __init__(self):
        """
        Initializes a new instance of the CognitoService class.
        """
        self.user_pool_id = os.getenv('COGNITO_USER_POOL_ID')
        self.app_client_id = os.getenv('COGNITO_CLIENT_ID')

        self.client = boto3.client('cognito-idp', region_name=os.getenv('COGNITO_REGION_NAME'))

    def sign_up(self, username:str, email: str, password: str) -> dict:
        """
        Registers a new user in the Cognito user pool.

        Parameters:
            - email (str): The email address of the user.
            - password (str): The password for the user.

        Returns:
            - dict: A dictionary containing the response from the Cognito service.


        Example:
            ```python
            cognito_service = CognitoService()
            response = cognito_service.sign_up(username = "johndoe", email="user@example.com", password="password123")
            print(response)
            ```

        """
        user_attributes = [{'Name': 'email', 'Value': email}]
        
        response = self.client.sign_up(
            ClientId=self.app_client_id,
            Username=username, 
            Password=password,
            UserAttributes=user_attributes
        )
        return response
    
    def confirm_sign_up(self, username:str, confirmation_code:str) -> dict:
        """
        Confirms email adress of registered user.

        Parameters:
            - username (str): The username of the user.
            - confirmation_code (str): The confirmation code which user got on email.

        Returns:
            - dict: A dictionary containing the response from the Cognito service.


        Example:
            ```python
            cognito_service = CognitoService()
            response = cognito_service.confirm_sign_up(username = "johndoe", confirmation_code = "123456")
            print(response)
            ```

        """
        response = self.client.confirm_sign_up(
        ClientId=self.app_client_id,
        Username=username,
        ConfirmationCode = confirmation_code
        )
        return response