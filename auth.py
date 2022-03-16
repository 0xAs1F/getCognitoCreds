import boto3
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--idtoken", dest = "token", help="Enter Identity Token")
parser.add_argument("-p", "--identitypoolid", dest = "IdentityPoolId" , help="Enter Identity Pool ID")
parser.add_argument("-a", "--userpoolid",dest ="user_pool_id", help="Enter the User Pool ID e.g us-east-1_testuserskldnl")
parser.add_argument("-r", "--region",dest ="region", help="Enter the region")
args = parser.parse_args()

#region =args.region 
client = boto3.client('cognito-identity' , region_name=args.region)

#token=args.token
user_pool_id = args.user_pool_id
arn_user_pool = f'cognito-idp.{args.region}.amazonaws.com/{user_pool_id}'
#IdentityPoolId = args.IdentityPoolId

response=client.get_id( IdentityPoolId= args.IdentityPoolId, Logins ={
       arn_user_pool:args.token
    })

credentials = client.get_credentials_for_identity(IdentityId=response["IdentityId"], Logins ={
       arn_user_pool:args.token
    })

#access_key = credentials['Credentials']['AccessKeyId']
#secret_key = credentials['Credentials']['SecretKey']
#session_token = credentials['Credentials']['SessionToken']

print("Access Key: " + credentials['Credentials']['AccessKeyId'])
print("Secret Key: " + credentials['Credentials']['SecretKey'])
print("Session Token: " + credentials['Credentials']['SessionToken'])
