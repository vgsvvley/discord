from flask import Flask, request, redirect
import datetime
import uuid

app = Flask(__name__)

# ================== TON LIEN DISCORD ==================
DISCORD_INVITE_URL = "https://discord.gg/HhYVkCpN"

@app.route('/discord')
def track_invite():
    # Récupération de l'IP réelle sur Render
    ip = request.headers.get('HTTP_TRUE_CLIENT_IP') or \
         request.headers.get('X-Forwarded-For', '').split(',')[0].strip() or \
         request.remote_addr

    user_agent = request.headers.get('User-Agent', 'Inconnu')
    referer = request.headers.get('Referer', 'Direct')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    unique_id = str(uuid.uuid4())[:8]

    print("=" * 70)
    print(f"[{timestamp}] NOUVEL CLIC SUR L'INVITATION !")
    print(f"ID unique          : {unique_id}")
    print(f"Adresse IP          : {ip}")
    print(f"Navigateur/Appareil : {user_agent}")
    print(f"Provenance          : {referer}")
    print("=" * 70)

    return redirect(DISCORD_INVITE_URL, code=302)

@app.route('/')
def home():
    return "<h1>Tracker Discord - Prêt à l'emploi</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)   
