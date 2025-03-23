class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7453473569"
    sudo_users = "7453473569"
    GROUP_ID = "-1002162699434"
    TOKEN = "7713565665:AAHtXfP9dW2HG3DS5NOvG8JPnnpR2bXBAAM"
    mongo_url = "mongodb+srv://mangalsg27: lDA08mAApf42eLRo@cluster0.rapan.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/e82d9ba84396bf1b1a9ca.jpg", "https://telegra.ph/file/e370ab1aeea76df6024c8.jpg"]
    SUPPORT_CHAT = "pull_your_waifu"
    UPDATE_CHAT = "pull_your_waifu"
    BOT_USERNAME = "Karin_assistant_bot"
    CHARA_CHANNEL_ID = "-1002521099319"
    api_id = "23015141"
    api_hash = "cc8bfa305e9a3f5000603efc79020301"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
