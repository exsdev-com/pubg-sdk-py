import os
from dotenv import dotenv_values
from pubg_client import Client

config = dotenv_values(".env")
pubg = Client(auth=config.get("PUBG_API_KEY"))

# samples = pubg.shards.samples(platform="steam")
# print(samples)

user_data = pubg.players.search(platform="steam", account_id="PLAYERUNKNOWN")
print(user_data)