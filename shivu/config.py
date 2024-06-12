
import os

class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = '6781100064'
    sudo_users = "5696053228", "6781100064"
    GROUP_ID = -1002246683431
    TOKEN = "7296531189:AAFIBo4Fh-DAzP7OipnMDrO17dl_oEMApko"
    mongo_url = "mongodb+srv://Shiki:xnp9czdVYgpT4KBE@shiki.smrp72r.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "NandhaChat"
    UPDATE_CHAT = "namupdates"
    BOT_USERNAME = "NamoHaremBot"
    CHARA_CHANNEL_ID = "-1002186861561"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
