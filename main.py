from flask import Flask, render_template
from steam import Steam
from decouple import config

app = Flask(__name__)

@app.route("/")
def index():
    gamesList = steamdata()
    game = gamesList[1]
    return render_template('steamdata.html', logo=game[1], name=game[0], playtime=game[2])

def steamdata():
    KEY = config("STEAM_API_KEY")
    steam = Steam(KEY)
    steamid = "76561198025213722"
    latest = steam.users.get_user_recently_played_games(steamid)
    gamedata = []

    for game in latest["games"]:
        name = game.get("name")
        logoKey = game.get("img_icon_url")
        appid = game.get("appid")
        logoUrl = "http://media.steampowered.com/steamcommunity/public/images/apps/" + str(appid) + "/" + str(logoKey) + ".jpg"
        alltime = game.get("playtime_forever")
        alltimeFormat = '{:02d}:{:02d}'.format(*divmod(alltime, 60))
        onegame = [name, logoUrl, alltimeFormat]
        gamedata.append(onegame)
    return gamedata

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4000, debug=True)
