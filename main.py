from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = "7852752280:AAGGw-WGAmpgLabreTbfLdVmT-IUk0Ycxoo"
BOT_USERNAME: Final = "@tamana_first_tele_bot"

##Pacages To install
# pip install python-telegram-bot 

##Commands
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

# Message Hundler Function send it back to user(While in PV or Groups)
async def message_handle(update : Update, context : ContextTypes.DEFAULT_TYPE):
      # To infrorm whether is a PV or Group Chat 
      message_type : str = update.message.chat.type
      # The message we process
      text : str = update.message.text

      #debugger(clean then)
      print(f'User ({update.message.chat.id}) in {message_type}: "{text}')

      #check  Point for Being in PV other Chat
      if message_type == "group":
            if BOT_USERNAME in text:
                  # to change the bot username , strip =  checking for no wite spaces
                  new_text : str = text.replace(BOT_USERNAME, " ").strip()
                  response: str = response_En(new_text)
            else:
                  return
      else:
            #For PV Chats
            response:str = response_En(text)
      
      print("BOT:" ,response)
      await update.message.reply_text(response)


#Logging errors 
async def error_en(update : Update , context: ContextTypes.DEFAULT_TYPE):
      print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
      print("Starting bot...")
      app = Application.builder().token(TOKEN).build()

      # to add handlers to the command hundlers
      app.add_handler(CommandHandler("start",start_command))
      app.add_handler(CommandHandler("help",help_command))
      app.add_handler(CommandHandler("custom",custom_command))
      
      # Message Hundlers 
      app.add_handler(MessageHandler(filters.TEXT, message_handle))

      # ERRors Haundlers
      app.add_error_handler("{error}")

      #Updates For new message and responds (poll_interval = to tell the program how often check the updated)
      print('polling..')
      app.run_polling(poll_interval =3)


     





