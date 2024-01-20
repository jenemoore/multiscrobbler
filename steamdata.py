from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")
steam = Steam(KEY)
steamid = "76561198025213722"

user = steam.users.get_user_details(steamid)
games = steam.users.get_owned_games(steamid)
latest = steam.users.get_user_recently_played_games(steamid)

for game in latest["games"]:
    name = game.get("name")
    logoKey = game.get("img_icon_url")
    appid = game.get("appid")
    logoUrl = "http://media.steampowered.com/steamcommunity/public/images/apps/" + str(appid) + "/" + str(logoKey) + ".jpg"
    alltime = game.get("playtime_forever")
    alltimeFormat = '{:02d}:{:02d}'.format(*divmod(alltime, 60))
    print(name + ", " + alltimeFormat)


