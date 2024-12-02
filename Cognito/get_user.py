import os
import boto3
from dotenv import load_dotenv
load_dotenv()

client = boto3.client('cognito-idp', region_name=os.getenv('COGNITO_REGION_NAME'))

access_token = 'eyJraWQiOiJBa3ZMcmI2NTZrU08yK0N1cmdSM0U3blJ5SmhNOFwvYjhzWVJydXpmSjBCaz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIzMDljZTlhYy1kMDIxLTcwZmQtNTkxZi01M2VhNzdlZmFhNjAiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuZXUtbm9ydGgtMS5hbWF6b25hd3MuY29tXC9ldS1ub3J0aC0xX2Y3VEpHR09QUiIsImNsaWVudF9pZCI6IjZnb3BqMzF0ZWpsaXVsMjZ2OGhyZnN2OGlhIiwib3JpZ2luX2p0aSI6IjY1ZTM1ZGMwLTUwNGEtNDIwNC1hNzE0LTI3YzkwODc0OGUzYyIsImV2ZW50X2lkIjoiNzFkMjM3YTctNWUzZi00MjcyLTlhYzUtZmVlMTM5NmQ5NWM1IiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJhd3MuY29nbml0by5zaWduaW4udXNlci5hZG1pbiIsImF1dGhfdGltZSI6MTczMzEzOTc3NSwiZXhwIjoxNzMzMTQzMzc0LCJpYXQiOjE3MzMxMzk3NzUsImp0aSI6ImQ4ZDM1Nzg5LWUyNjUtNDNmNC1iZjgyLWFhMGVmYzdiYzgwZCIsInVzZXJuYW1lIjoidG9tY29sYWRhIn0.LoicCDiplACTSC-llE5gES-uCFd4WRge_oSHKvEKIUYSKdYfx8XcHuHHdAOmrdRMamGQwEiqNQWHh_GJKuYqH5DHmZT-CZp1YrD0EEY-oUAHjXataT9oJe83lRuJN-i1CiP8VpKHoyMrFX-Kz1P_qgaeMIiT6hSbb3P3eqXQL-YtmPsDNaiolk_Hrp21uaut97thsy5igFgLfg1S7y2-PSG1pRiAr8XWPyiuiDz6jrDEnz4fz91lurqc8PA-11rZVaa4xj-VKOl_oQMnZ6u7HoyLTVxjzzODkSEE__71b6JV8ZXfVK_bpvKNdC047SCwqF8XoOpHDJ2t7aBlDgynOg'
response = client.get_user(
    AccessToken = access_token
    )

attr_sub = None
for attr in response['UserAttributes']:
    if attr['Name'] == 'sub':
        attr_sub = attr['Value']
        break

print('UserSub', attr_sub)