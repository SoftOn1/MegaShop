
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")
BOT_TOKEN = config["settings"]["token"]
admin_for_logs = config["settings"]["admin_id"]
admins = config["settings"]["admin_id"]
api_id = config["settings"]["api_id"]
api_hash = config["settings"]["api_hash"]
if "," in admins:
    admins = admins.split(",")
else:
    if len(admins) >= 1:
        admins = [admins]
    else:
        admins = []
        print("***** Вы не указали админ ID *****")

bot_version = "1.4"
bot_description = f"<b>▫️Слито в @END_RAID</b>\n" \
                  f"<b>▫️Версия:</b> <code>{bot_version}</code>\n" 
