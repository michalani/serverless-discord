import requests

with open('.env') as env_file:
    for line in env_file:
        if(line.split('=')[0] == "DISCORD_TOKEN"):
            DISCORD_TOKEN = line.split('=')[1].splitlines()[0]
        elif(line.split('=')[0] == "DISCORD_APPLICATION_ID"):
            DISCORD_APPLICATION_ID = line.split('=')[1].splitlines()[0]
        elif(line.split('=')[0] == "REGISTER_COMMAND"):
            REGISTER_COMMAND = line.split('=')[1].splitlines()[0]
        # print(),  # The comma to suppress the extra new line char

if(REGISTER_COMMAND != 'false'):
    url = "https://discord.com/api/v10/applications/{}/commands".format(DISCORD_APPLICATION_ID)

    # This is an example CHAT_INPUT or Slash Command, with a type of 1
    json = {
        "name": "blep",
        "type": 1,
        "description": "Respond to blop with Blop!",
        "options": [
            {
                "name": "animal",
                "description": "The type of animal",
                "type": 3,
                "required": True,
                "choices": [
                    {
                        "name": "Dog",
                        "value": "animal_dog"
                    },
                    {
                        "name": "Cat",
                        "value": "animal_cat"
                    },
                    {
                        "name": "Penguin",
                        "value": "animal_penguin"
                    }
                ]
            },
            {
                "name": "only_smol",
                "description": "Whether to show only baby animals",
                "type": 5,
                "required": False
            }
        ]
    }

    # For authorization, you can use either your bot token
    headers = {
        "Authorization": "Bot {}".format(DISCORD_TOKEN)
    }

    # # or a client credentials token for your app with the applications.commands.update scope
    # headers = {
    #     "Authorization": "Bearer <my_credentials_token>"
    # }

    r = requests.post(url, headers=headers, json=json)

    if(r.status_code == 200):
        print('Successfully registered discord slash commands')
    else:
        print('Discord slash command could not register')
        print(r.content)
else:
    print('Skipped registering discord slash command')