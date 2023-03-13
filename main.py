from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
import json
import os

# Useful docs:
# https://discord.com/developers/docs/interactions/receiving-and-responding#security-and-authorization
# 
# https://stackoverflow.com/a/67661930/14670874
# similar attempts ^
# 
# https://discord.com/developers/docs/interactions/application-commands#making-a-global-command
# registering commands on the bot ^

def lambda_handler(event, context):
    PUBLIC_KEY = os.environ['DISCORD_PUBLIC_KEY']
    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))
    signature = event['headers']['x-signature-ed25519']
    timestamp = event['headers']['x-signature-timestamp']

    try:
        # ed25519 check
        verify_key.verify(f'{timestamp}{event["body"]}'.encode(), bytes.fromhex(signature))
        
        # respond to PING with PONG
        if json.loads(event['body'])['type'] == 1:
            return {"type": 1}
        else:
            data = json.loads(event['body'])['data']
            
            # proof of concept command 1
            if(data['name'] == 'blep'):
                return {"type": 4,
                    "data": {
                        "tts": False,
                        "content": "Blop!",
                        "embeds": [],
                        "allowed_mentions": { "parse": [] }
                        }
                    }
            # proof of concept command 2
            elif(data['name'] == 'blap'):
                return {"type": 4,
                    "data": {
                        "tts": False,
                        "content": "Blap blap!",
                        "embeds": [],
                        "allowed_mentions": { "parse": [] }
                        }
                    }
    except (BadSignatureError) as e:
        return {'statusCode': 401,
            'body': "Bad Signature"
        }