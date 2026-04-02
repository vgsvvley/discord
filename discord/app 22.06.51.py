from flask import Flask, request, redirect
import logging
from datetime import datetime
import uuid

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s"  # On gère le format manuellement pour plus de contrôle
)

app = Flask(__name__)

# Supprimer les handlers par défaut si nécessaire
app.logger.handlers.clear()

# ============= TON LIEN DISCORD =============
DISCORD_INVITE_URL = "https://discord.gg/HhyVkCpN"

@app.route('/discord')
def track_invite():
    # Récupération de l'IP réelle
    ip = request.headers.get('HTTP_TRUE_CLIENT_IP') or \
         request.headers.get('X-Forwarded-For', '').split(',')[0].strip() or \
         request.remote_addr

    user_agent = request.headers.get('User-Agent', 'Inconnu')
    referer = request.headers.get('Referer', 'Direct')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    unique_id = str(uuid.uuid4())[:8]

    # Affichage propre dans les logs
    app.logger.info("")
    app.logger.info("🎯 NOUVEAU CLIC SUR L'INVITATION")
    app.logger.info("─" * 50)
    app.logger.info(f"⏰ Horodatage       : {timestamp}")
    app.logger.info(f"🆔 ID unique         : {unique_id}")
    app.logger.info(f"🌐 IP                : {ip}")
    app.logger.info(f"📱 Navigateur        : {user_agent}")
    app.logger.info(f"🔗 Provenance        : {referer}")
    app.logger.info("─" * 50)

    return redirect(DISCORD_INVITE_URL, code=302)

@app.route('/')
def home():
    return redirect(DISCORD_INVITE_URL, code=302)   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)   
