import requests

# parse env file
try:
    with open('.env') as env_file:
        for line in env_file:
            if(line.split('=')[0] == "DISCORD_TOKEN"):
                DISCORD_TOKEN = line.split('=')[1].splitlines()[0]
            elif(line.split('=')[0] == "DISCORD_APPLICATION_ID"):
                DISCORD_APPLICATION_ID = line.split('=')[1].splitlines()[0]
            elif(line.split('=')[0] == "REGISTER_COMMAND"):
                REGISTER_COMMAND = line.split('=')[1].splitlines()[0]
            # Ignore, this is another method of authentication
            elif(line.split('=')[0] == "DISCORD_CREDENTIALS_TOKEN"):
                DISCORD_CREDENTIALS_TOKEN = line.split('=')[1].splitlines()[0]

            # print(),  # The comma to suppress the extra new line char
except Exception as e:
    print(e)
    print('Could not parse env file!')
    quit()

# Main logic for registering discord slash command directly with discord
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
    try:
        # For authorization, you can use either your bot token
        headers = {
            "Authorization": "Bot {}".format(DISCORD_TOKEN)
        }
    except NameError:
        print('wrong name')
        # or a client credentials token for your app with the applications.commands.update scope
        headers = {
            "Authorization": "Bearer {}".format(DISCORD_CREDENTIALS_TOKEN)
        }

    r = requests.post(url, headers=headers, json=json)

    if(r.status_code == 200):
        print('Successfully registered GLOBAL discord slash commands')
    else:
        print('Discord GLOBAL slash commands could not be registered')
        print(r.content)
        # quit()
else:
    print('Skipped registering discord slash command')