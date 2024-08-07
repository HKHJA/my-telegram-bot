from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import logging
import nest_asyncio

# Apply the workaround for nested event loops
nest_asyncio.apply()

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define the command handler function
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello! I am your bot.')
    logging.info("Sent '/start' response.")

async def main() -> None:
    # Create the Application and pass it your bot's token
    application = Application.builder().token('7284156733:AAHUpfjB65s7C-ciuHZP8eEM_BgId4-yGTA').build()

    # Add a command handler
    application.add_handler(CommandHandler('start', start))

    logging.info("Bot is starting...")

    # Run the bot until you send a signal to stop
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
