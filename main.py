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
      # Remember python is sensetive on lower and upperCase 
      uper_lower_text : str = text.lower()

      if 'hello' in uper_lower_text:
            return " such a polite friend you are , Hi ;))"
      if 'I need Your Help' in uper_lower_text:
            return "Ohh That sounds Gret What Can I do For You ?"
      if 'can you find a friend for me ?' in uper_lower_text:
            return "Ummm You need to talk with humans not me :(. Did You Find It hard to talk with humans?"
      if 'Yes' in uper_lower_text:
            return "Hey You Are a Wonderfull person, Why You don't try talking one?"
      
      return "I Don't Understand What To Do, Help Me Please !!"


     





