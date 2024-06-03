import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import os
import http.server
import socketserver

from http import HTTPStatus


# Set up logging for debugging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# Replace 'YOUR_BOT_TOKEN' with your actual token from BotFather
BOT_TOKEN = '7149467380:AAG7_UN-t0xLYztX4J1EwsAP1DS8eOqacxA'

# Echo function to handle incoming messages
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register the echo handler for text messages
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
@@ -17,3 +45,6 @@ def do_GET(self):
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
