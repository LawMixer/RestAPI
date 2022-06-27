from flask import Flask
from flask import jsonify
import requests
app = Flask('app')

discordId = 247036279420747776
money = 100

req1 = requests.get(f"https://verify.eryn.io/api/user/{discordId}")
robloxUsername = req1.json()["robloxUsername"]

req2 = requests.get(f"https://verify.eryn.io/api/user/{discordId}")
robloxId = req2.json()["robloxId"]

# https://lk.policelaw14.repl.co/users/247036279420747776
# api.lawmixerscpf.tk/users/{discordId}
@app.route(f"/users/{discordId}")
def get_roblox_info():
  return jsonify(f"money: {money}, robloxUsername: {robloxUsername}, robloxId: {robloxId}")


app.run(host='0.0.0.0', port=8080)