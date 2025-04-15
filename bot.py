from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Auto reply function
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"မင်္ဂလာပါ! နေကောင်းပါသလား: {user_message}")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ခဏလေးက စောင့်ပါ လိုအပ်တာများ ရှာဖွေနေပါတယ်...")

# Main function
if __name__ == '__main__':
    app = ApplicationBuilder().token("7696355745:AAGEuIGobaMzJk-2V8QpMpukfrn-tfkmszE").build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), auto_reply))

    print("Bot is running...")
    app.run_polling()
