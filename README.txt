How to setup the bot.

Step 0:
  https://discordpy.readthedocs.io/en/latest/discord.html

Step 1:
  Download python 3.8 on the device you plan to run the bot on 24/7 link to download: https://www.python.org/downloads/release/python-386/

Step 2:
  Install python
  Make sure that you add pip to path or else it will make things harder to setup.
  finish installation as usual.

Step 3:
  open cmd or equivalent and run the following commands:
    pip install requests
    pip install discord
    pip install asyncio

Step 4:
  Setting up the config file

  to setup the config file you will want to put the bot token in the "BOT TOKEN" area of the config.json
  Also change the text channel id to the
  for each company it will follow the same rules
  replace "compID" with the id of the torn company and where it says "Director of this company's APIKey" you want the director of the company's APIkey in there
  to add more the copy and paste the "compID" : "Director of this company's APIKey" and put the correct values separated by a comma
    Ex:
    {"APIKeys":
    {"compID" : "Director of this company's APIKey",
    "comp2ID" : "Director of this company's APIKey",
    "comp3ID" : "Director of this company's APIKey",
    "comp4ID" : "Director of this company's APIKey"},
    "Token" : "BOT TOKEN",
    "Channel" : Text Channel ID no quotes}
