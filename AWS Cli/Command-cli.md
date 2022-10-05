1. To Make profile--> aws configure --profile profile_name
                  --> Enter access keys, secret keys , region .

2. Launch the Stack :                
``` 
      aws cloudformation create-stack --stack-name myteststack --template-body file://deploy_ec2_network_v1.json --parameters ParameterKey=KeyP,ParameterValue=key1 ParameterKey=InstanceType,ParameterValue=t2.micro --profile blogprofile
      
      
      
      aws cloudformation create-stack --stack-name myteststack --template-body file://test-webacl.json  --profile chandan-access

 ```

 3. Check the Status of the Stack
 ```
    aws cloudformation describe-stacks --stack-name <stack_id> --profile blogprofile
 ```

 4. Delete the Stack :
     aws cloudformation delete-stack --stack-name <stack ID> --profile blogprofile

5. aws cloudformation list-stacks :
        