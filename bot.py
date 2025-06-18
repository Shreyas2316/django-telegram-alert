from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os
from dotenv import load_dotenv
from duckduckgo_search import DDGS

load_dotenv(os.path.join("backend_project", "backend_project", ".env"))
TOKEN = os.getenv("TELEGRAM_TOKEN")

# --- Command Handlers ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"👋 Hello {update.effective_user.first_name}, I'm your Django bot!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Available commands:\n"
        "/start - Greet the user\n"
        "/help - List commands\n"
        "/status - Show bot status\n"
        "/feedback <your message> - Send feedback\n"
        "/contact - Contact the developer\n"
        "Or type any question to search!"
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is running fine!")

# --- Search + Logging ---
async def general_search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.strip()
    user_id = update.effective_user.id
    username = update.effective_user.username or "unknown"

    try:
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, region="wt-wt", safesearch="Moderate", max_results=3):
                results.append(f"🔎 {r['title']}\n{r['href']}\n\n{r['body']}")

        if results:
            reply = "\n\n---\n\n".join(results)
            await update.message.reply_text(reply[:4096])
        else:
            reply = "❌ No relevant results found."
            await update.message.reply_text(reply)
        log_interaction(
            user_id=update.effective_user.id,
            username = update.effective_user.username or f"{update.effective_user.first_name} {update.effective_user.last_name or ''}".strip(),
            user_message=query,
            bot_response=reply[:4096]
    )   

        # ✅ Log interaction
        log_interaction(user_id, username, query, reply[:500])

    except Exception as e:
        error_message = f"⚠️ Error: {str(e)}"
        await update.message.reply_text(error_message)
        log_interaction(user_id, username, query, error_message)

# --- Logger Function ---
def log_interaction(user_id, username, user_message, bot_response):
    name = username if username else f"UserID-{user_id}"
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"👤 {name} asked: {user_message}\n")
        f.write(f"🤖 Bot replied: {bot_response}\n")
        f.write("-" * 50 + "\n")

async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = " ".join(context.args)
    if not message:
        await update.message.reply_text("✍️ Please provide feedback after the /feedback command.")
        return
    with open("feedback.txt", "a", encoding="utf-8") as f:
        f.write(f"{user.username or user.first_name} ({user.id}) sent feedback: {message}\n")
        f.write("-" * 50 + "\n")
    await update.message.reply_text("✅ Thanks for your feedback!")

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📧 You can contact the developer at: example@email.com\nOr raise issues on GitHub.")
async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = " ".join(context.args)
    if not message:
        await update.message.reply_text("✍️ Please provide feedback after the /feedback command.")
        return
    with open("feedback.txt", "a", encoding="utf-8") as f:
        f.write(f"{user.username or user.first_name} ({user.id}) sent feedback: {message}\n")
        f.write("-" * 50 + "\n")
    await update.message.reply_text("✅ Thanks for your feedback!")

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📧 You can contact the developer at: shreyasneet162004@email.com\nOr raise issues on GitHub.")

# --- Bot Init ---
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("feedback", feedback))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, general_search))


    print("🤖 Bot is polling...")
    app.run_polling()
