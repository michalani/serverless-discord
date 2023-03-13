## To do list

Port ENV key to parameter store or secrets manager (preffered)

Port Lambda code to Docker in order to remove the .zip layer

~~Port everything to IaC such as TF~~

## How to use

1. create `.env` file and add:
```
DISCORD_PUBLIC_KEY = replace_me
```

2. 
```
$ terraform init
$ terraform apply
```
3. Profit