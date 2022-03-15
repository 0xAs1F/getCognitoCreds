import boto3
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--identitypoolid", dest = "IdentityPoolId" , help="Enter Identity Pool ID")
parser.add_argument("-r", "--region",dest ="region", help="Enter the region")
args = parser.parse_args()


region=args.region

IdentityPoolId=args.IdentityPoolId

client = boto3.client('cognito-identity',region_name=region)
response = client.get_id(IdentityPoolId=IdentityPoolId)
IdentityId= response['IdentityId']

credentials = client.get_credentials_for_identity(IdentityId=IdentityId)

access_key = credentials['Credentials']['AccessKeyId']
secret_key = credentials['Credentials']['SecretKey']
session_token = credentials['Credentials']['SessionToken']
identity_id = credentials['IdentityId']

print("Access Key: " + access_key)
print("Secret Key: " + secret_key)
print("Session Token: " + session_token)
print("Identity Id: " + identity_id)