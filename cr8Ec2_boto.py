import boto3
client = boto3.client('ec2',region_name="us-east-1")
resp = client.run_instances(ImageId= 'ami-0b69ea66ff7391e80',MinCount = 1,MaxCount = 1,InstanceType = 't2.micro',KeyName = 'myPublic',
SubnetId = 'subnet-0ee9de2a2626d76fb',SecurityGroupIds = ['sg-0fdf2e8093dba9b6c'])
for instance in resp['Instances']:
    print(instance['InstanceId'])

