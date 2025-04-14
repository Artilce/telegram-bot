# coin_bot.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# User coin data (သိမ်းထားတဲ့ memory — restart ပြန်ရင် refresh)
user_data = {}

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_data[user_id] = 0  # initialize coins

    keyboard = [
        [InlineKeyboardButton("🪙 Get Coin", callback_data="get_coin")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("🎮 Coin Game စတင်ပါပြီ!", reply_markup=reply_markup)

# Callback for button press
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    if user_id not in user_data:
        user_data[user_id] = 0

    if query.data == "get_coin":
        user_data[user_id] += 1
        coins = user_data[user_id]
        await query.answer()
        await query.edit_message_text(
            text=f"🪙 မင်္ဂလာပါ {query.from_user.first_name}!\nသင်မှာ Coins: {coins} 🧮",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🪙 Get More Coin", callback_data="get_coin")]
            ])
        )

# Main function
if __name__ == '__main__':
    app = ApplicationBuilder().token("Stop").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Coin Game Bot is running...")
    app.run_polling()
