from flask import Flask
import threading
from conversationbot2 import run_bot  # Garanta que esteja corretamente importando a função

app = Flask(__name__)

bot_thread = None  # Guarda a referência para a thread do bot

@app.route('/')
def start_bot():
    global bot_thread
    if bot_thread is None or not bot_thread.is_alive():
        bot_thread = threading.Thread(target=run_bot)
        bot_thread.start()
        return 'Bot iniciado'
    else:
        return 'Bot já está rodando'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)  # use_reloader=False para evitar problemas com threads durante o desenvolvimento
