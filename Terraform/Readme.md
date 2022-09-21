terraform command:

terraform init
terraform plan --var-file=./env/qa.tfvars -out out.terraform
terraform apply "out.terraform"
terraform destroy --var-file=./env/asg.tfvars --auto-approve