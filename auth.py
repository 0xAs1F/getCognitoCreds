import boto3
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--idtoken", dest = "token", help="Enter Identity Token")
parser.add_argument("-p", "--identitypoolid", dest = "IdentityPoolId" , help="Enter Identity Pool ID")
parser.add_argument("-a", "--userpoolarn",dest ="arn_user_pool", help="Enter the User Pool ARN e.g cognito-idp.us-east-1.amazonaws.com/us-east-1_testuserskldnl")
parser.add_argument("-r", "--region",dest ="region", help="Enter the region")
args = parser.parse_args()

region = args.region
client = boto3.client('cognito-identity' , region_name=region)

token=args.token

arn_user_pool =args.arn_user_pool

IdentityPoolId = args.IdentityPoolId

response=client.get_id( IdentityPoolId= IdentityPoolId, Logins ={
       arn_user_pool:token
    })

identity_id = response["IdentityId"]

credentials = client.get_credentials_for_identity(IdentityId=identity_id, Logins ={
       arn_user_pool:token
    })

access_key = credentials['Credentials']['AccessKeyId']
secret_key = credentials['Credentials']['SecretKey']
session_token = credentials['Credentials']['SessionToken']


print("Access Key: " + access_key)
print("Secret Key: " + secret_key)
print("Session Token: " + session_token)
