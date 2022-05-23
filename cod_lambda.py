import json
import boto3 ## IMPORTANTE MOD boto3

region = 'us-east-2'  # INFORMANDO A REGIÃO QUE VAI SER EXCECUTADO LAMBDA
ec2 = boto3.client('ec2', region_name=region)


def lambda_handler(event, context):  # CRIAÇÃO DA FUNÇÃO
    instances = event["instances"].split(',')
    action = event["action"]
    
    if action == 'Start':  # LIGA A EC2
         print("STARTing you instances: " + str(instances))
         ec2.start_instances(InstanceIds=instances)
         response = "Successfully started instances: " + str(instances)  # CONCTENANDO INT PARA STR
    elif action == 'Stop':  # PARE EC2
         print("STOPping you instances: " + str(instances))
         ec2.stop_instances(InstanceIds=instances)
         response = "Successfully stopped instances: " + str(instances)  # CONCTENANDO INT PARA STR
        
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
