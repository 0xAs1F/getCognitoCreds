import boto3,argparse,sys

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--idtoken", dest = "token", help="Enter Identity Token")
parser.add_argument("-i", "--identitypoolid", dest = "IdentityPoolId" , help="Enter Identity Pool ID")
parser.add_argument("-u", "--userpoolid",dest ="user_pool_id", help="Enter the User Pool ID e.g us-east-1_testuserskldnl")
parser.add_argument("-r", "--region",dest ="region", help="Enter the region")
args = parser.parse_args()

if len(sys.argv) == 1:
   print('\033[1;31mKindly pass on the necessary arguments or -h/--help for help ')
   print('Example: python3 auth.py -t eyJraWQiOiJ... -i us-east-1:544545fff6adc-b1ef-4193-aa09-8e9c555ff5b1cc8 -u us-east-2_trrrfrdiHHI -r us-east-1 \033[0;0m')
   sys.exit()
else:
    print("\033[1;36m\nPlease wait while we serve you aws credentials")
    print("---------------------------------------------- \033[0;0m\n")

client = boto3.client('cognito-identity' , region_name=args.region)

user_pool_id = args.user_pool_id
arn_user_pool = f'cognito-idp.{args.region}.amazonaws.com/{user_pool_id}'

response=client.get_id( IdentityPoolId= args.IdentityPoolId, Logins ={
       arn_user_pool:args.token
    })

credentials = client.get_credentials_for_identity(IdentityId=response["IdentityId"], Logins ={
       arn_user_pool:args.token
    })

print("Access Key: " + "\033[1;32m"+credentials['Credentials']['AccessKeyId'] + "\033[0;0m")
print("Secret Key: " +"\033[1;32m"+ credentials['Credentials']['SecretKey']+"\033[0;0m")
print("Session Token: " +"\033[1;32m"+ credentials['Credentials']['SessionToken']+"\033[0;0m")