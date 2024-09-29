from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = "7852752280:AAGGw-WGAmpgLabreTbfLdVmT-IUk0Ycxoo"
BOT_USERNAME: Final = "@tamana_first_tele_bot"

#Commands
async def start_command(update : Update, context: ContextTypes.DEFAULT_TYPE):
      await update.message.reply_text("Hello My Friend :), How Can I Help You? 😀")

async def help_command(update : Update, context: ContextTypes.DEFAULT_TYPE):
      await update.message.reply_text("Okay You are asking for help, First of all type something for me to get a respond 😁")

async def custom_command(update : Update, context: ContextTypes.DEFAULT_TYPE):
      await update.message.reply_text("This is a custom command :))")

# BOT responses 

def response_En(text: str) -> str :
      if 'hello' in text:
            return " such a polite friend you are , Hi ;))"
      





