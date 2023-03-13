## To do list

Port ENV key to parameter store or secrets manager (preffered)

Port Lambda code to Docker in order to remove the .zip layer

~~Port everything to IaC such as TF~~

## How to use

1. Create `.env` file and add:
```
DISCORD_TOKEN=replace_me
DISCORD_APPLICATION_ID=replace_me
DISCORD_PUBLIC_KEY=replace_me
ENDPOINT_PATH=/interactions
REGISTER_COMMAND=true
```

2. Install python3
```
sudo apt install python3
sudo apt install python3-pip
```

3. Run terraform
```
$ terraform init
$ terraform apply
$ terraform output -raw InteractionsEndpointURL
```
