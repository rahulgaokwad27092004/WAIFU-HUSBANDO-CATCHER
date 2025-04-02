
import os

class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = '7453473569'
    sudo_users = "7453473569", "1890903731"
    GROUP_ID = -1002424371945
    TOKEN = "7713565665:AAHtXfP9dW2HG3DS5NOvG8JPnnpR2bXBAAM"
    mongo_url = "mongodb+srv://mangalsg27:lDA08mAApf42eLRo@cluster0.rapan.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "karinupdatee"
    UPDATE_CHAT = "pull_your_waifu"
    BOT_USERNAME = "NamoHaremBot"
    CHARA_CHANNEL_ID = "-1002521099319"
    api_id = 26626068
    api_hash = "cc8bfa305e9a3f5000603efc79020301"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
