from flask import Flask, request, redirect
import datetime
import uuid

app = Flask(__name__)

# ================== TON LIEN DISCORD ==================
DISCORD_INVITE_URL = "https://discord.gg/HhYVkCpN"   # ← Ton lien

@app.route('/invite/<invite_code>')
def track_invite(invite_code):
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Inconnu')
    referer = request.headers.get('Referer', 'Direct')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    unique_id = str(uuid.uuid4())[:8]

    print("=" * 70)
    print(f"[{timestamp}] NOUVEL CLIC SUR L'INVITATION !")
    print(f"Code d'invite utilisé : {invite_code}")
    print(f"ID unique          : {unique_id}")
    print(f"Adresse IP          : {ip}")
    print(f"Navigateur/Appareil : {user_agent}")
    print(f"Provenance          : {referer}")
    print("=" * 70)

    # Redirection vers ton serveur Discord
    return redirect(DISCORD_INVITE_URL, code=302)


# Page d'accueil (optionnelle)
@app.route('/')
def home():
    return """
    <h1>Tracker d'invitation Discord</h1>
    <p>Utilise ce lien pour tracker : <strong>/invite/toncode</strong></p>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)