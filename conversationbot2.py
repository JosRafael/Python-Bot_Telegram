from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import asyncio

# Isso assume que o código acima está
def run_bot():
    # Cria um novo loop de eventos para a thread
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    application = Application.builder().token('6330118321:AAEWvqhsEdViobXtbT-F4ODrwDnvknUId2A').build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.CONTACT, contact_handler))  # Ajuste conforme necessário
    
    # Usa o loop de eventos da thread para executar o bot
    loop.run_until_complete(application.run_polling())
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Cria um botão que solicita o contato do usuário
    keyboard = [[KeyboardButton("Compartilhar Contato", request_contact=True)]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    
    # Envia uma mensagem ao usuário com o botão
    await update.message.reply_text('Por favor, compartilhe seu contato.', reply_markup=reply_markup)

async def contact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Ação a ser realizada quando o usuário compartilha o contato
    user_contact = update.message.contact

    # Abre o arquivo em modo de anexação ('a') para adicionar o novo lead
    with open('leads.txt', 'a') as file:
        file.write(f"Nome: {user_contact.first_name}, Telefone: {user_contact.phone_number}\n")

    await update.message.reply_text(f'Obrigado por compartilhar seu contato, {user_contact.first_name}!')


def main():
    # Substitua 'YOUR_TOKEN' pelo token do seu bot fornecido pelo BotFather
    application = Application.builder().token('6330118321:AAEWvqhsEdViobXtbT-F4ODrwDnvknUId2A').build()

    # Adiciona um manipulador para o comando /start
    application.add_handler(CommandHandler("start", start))
    
    # Adiciona um manipulador para quando um contato é recebido
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, contact_handler))

    # Inicia o bot
    application.run_polling()

if __name__ == '__main__':
    main()
