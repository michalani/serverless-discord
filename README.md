## What is this?

As of 2022 discord supports slashes functionality [1], this means that you no longer are stuck to listenining for message events as discord forwards the events to your endpoint themselves.

With those changes it's possible to invoke lambda only when you recieve a request massively saving you on compute time as you can utilize AWS Lambda to serverlessly perform the actions.

This repository is just a proof of this concept, this can be used in many situations such as user authorization, admin managment, or automatic game servers initialization allowing you to save on computing and utilize scaling aspect of AWS to host your game servers for when you need it with your friends.

[1] https://support.discord.com/hc/en-us/articles/1500000368501-Slash-Commands-FAQ
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
