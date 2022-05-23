# Automação: Start e Stop com os seguintes serviços AWS: EC2 -Lambda com código Python e EventBridge 🤓✌️



### Neste repositório, mostrarei como iniciar e parar instâncias do EC2 com python lambda. Também usaremos o Amazon EventBridge para configurar regras que acionarão o AWS Lambda que inicia ou interrompe instâncias do EC2.

#### Serviços usados dutante o projeto:

##### AWS-EC2
##### AWS-Lambda
##### AWS-EventBridge


----

### Projeto.

![lambda](https://user-images.githubusercontent.com/102867453/169884118-34170bb8-ca1a-4c71-b945-76c498ba50b1.jpg)


- [x] Introduction to Starting and Stopping EC2 Instances with AWS Lambda Python
- [x] Setting up EC2 Instances
- [x] Setting up AWS Lambda in Python to Start and Stop EC2 Instances
- [x] Create AWS Lambda Role to Start - Stop EC2 Instances
- [x] Writing Lambda Code to Start - Stop EC2 Instances
- [x] Testing our Lambda that Starts and Stops EC2 Instances
- [x] Testing Stopping EC2 Instances with Lambda
- [x] Testing Starting EC2 Instances with Lambda
- [x] Using Amazon EventBridge to trigger Lambda
- [x] Create an Amazon EventBridge rule with Cron Expression to Start - Stop EC2 Instances


## Código que foi usado em **Python**:

```
import json
import boto3 
region = 'us-east-2'  
ec2 = boto3.client('ec2', region_name=region)


def lambda_handler(event, context):  
    instances = event["instances"].split(',')
    action = event["action"]
    
    if action == 'start':  # LIGA A EC2
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
    
    
```
