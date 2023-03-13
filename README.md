## To do list

Port ENV key to parameter store or secrets manager (preffered)

Port Lambda code to Docker in order to remove the .zip layer

~~Port everything to IaC such as TF~~

## How to use

1. create `.env` file and add:
```
DISCORD_PUBLIC_KEY=replace_me
ENDPOINT_PATH=/interactions
```

2. 
```
$ terraform init
$ terraform apply
$ terraform output -raw InteractionsEndpointURL
```
3. Register commands with discord https://discord.com/developers/docs/interactions/application-commands#making-a-global-command

4. $$$