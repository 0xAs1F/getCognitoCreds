import boto3,argparse

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--identitypoolid", dest = "IdentityPoolId" , help="Enter Identity Pool ID")
parser.add_argument("-r", "--region",dest ="region", help="Enter the region")
args = parser.parse_args()

client = boto3.client('cognito-identity',region_name=args.region)
response = client.get_id(IdentityPoolId=args.IdentityPoolId)

credentials = client.get_credentials_for_identity(IdentityId=response['IdentityId'])

print("Access Key: " + credentials['Credentials']['AccessKeyId'])
print("Secret Key: " + credentials['Credentials']['SecretKey'])
print("Session Token: " + credentials['Credentials']['SessionToken'])
