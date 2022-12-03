## Cross Account Role Stack

**Template path:** JK-Access/CF_JK_Role.json


### Create Stack
```shell
aws cloudformation create-stack --stack-name k2cloud-iam-role --profile prod --template-body file://JK-Access/CF_JK_Role.json --capabilities CAPABILITY_NAMED_IAM
```

### Update Stack
```shell
aws cloudformation update-stack --stack-name k2cloud-iam-role --profile prod --template-body file://JK-Access/CF_JK_Role.json --capabilities CAPABILITY_NAMED_IAM
```

### Delete Stack
```shell
aws cloudformation delete-stack --stack-name k2cloud-iam-role --profile prod
```

# SAML Roles for developers

### Create stack
```shell
aws cloudformation create-stack --stack-name SAMLDevelopersRole --template-body file://Prod-Developers-SAML-Role.json --profile prod --capabilities CAPABILITY_NAMED_IAM
```

### Update stack
```shell
aws cloudformation update-stack --stack-name SAMLDevelopersRole --template-body file://Prod-Developers-SAML-Role.json --profile prod --capabilities CAPABILITY_NAMED_IAM
```


# SAML Roles for DevOps Team

### Create stack
```shell
aws cloudformation create-stack --stack-name SAMLDevOpsRole --template-body file://Prod-DevOps-SAML-Role.json --profile prod --capabilities CAPABILITY_NAMED_IAM
```

### Update stack
```shell
aws cloudformation update-stack --stack-name SAMLDevOpsRole --template-body file://Prod-DevOps-SAML-Role.json --profile prod --capabilities CAPABILITY_NAMED_IAM
```
