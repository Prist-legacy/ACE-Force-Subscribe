import os

class Config():
  # Bot Token (Use @BotFather)
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "5853392984:AAE6C7DhVtxGAINDFo5PDjMOBSLqhRKm61U")

  # Bot Updates Channel Username (without @)
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "pristbank")

  # PostgresSQL DB URL (Use ElephantSQL)
  DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://prist:PgWERBWTNck58YqEr3cc@containers-us-west-82.railway.app")

  # API & HASH (Use my.telegram.org)
  APP_ID = os.environ.get("APP_ID", 20818634)
  API_HASH = os.environ.get("API_HASH", "f7c5ae05e2860fae8c89da23e8604ae0")

  # Sudo users (Put your User ID)
  SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "920015079").split()))
  SUDO_USERS.append(5524391658)
  SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "**🤖 𝗔𝗖𝗘 - Force Subscribe Bot**\n\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**⚙️ Setup**\n\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**🎲 Commmands**\n\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn of ForceSubscribe.\n/ForceSubscribe {channel username or channel ID} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n/source_code - To get bot source code😍\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
       "**👨‍💻 Developed By @ACE_ML**"
      ]
      SC_MSG = "**Hey [{}](tg://user?id={})**\n click on below👇 button to get my source code, for more help ask in my support group👇👇 "

      START_MSG = "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /help__"
