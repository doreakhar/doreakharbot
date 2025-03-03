import os
import telebot
import requests
from flask import Flask, request

# دریافت توکن از متغیر محیطی در Railway
TOKEN = os.getenv("BOT_TOKEN")  
WEBHOOK_URL = "https://your-railway-url.up.railway.app/"  # بعداً با URL واقعی جایگزین می‌کنیم

app = Flask(__name__)
bot = telebot.TeleBot(TOKEN)

@app.route("/", methods=["GET"])
def home():
    return "The bot is running!", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("درخواست جدید دریافت شد:", data)

    if "my_chat_member" in data:
        chat = data["my_chat_member"]["chat"]
        new_status = data["my_chat_member"]["new_chat_member"]["status"]

        if new_status == "member":
            user_id = chat["id"]
            welcome_text = (
                "👋 سلام، به دور آخر خوش آمدی دوست من!\n\n"
                "دور آخر، نقطه‌ی عطفی ست برای رهایی از "
                "هر چرخه‌ی ناسالمی که هیچ‌گاه به نفع تو نبود.\n\n"
                "✨ *این‌بار، رها شدن قدرت توست.* ✨\n\n"
                "ما بر مدل‌های بهبودی و مسیر آن سواریم، بنابراین در کنار تو هستیم تا در هر نقطه‌ای که هستی قدم بعدی رو برداری،\n"
                "خودت رو بهتر بشناسی و از این چرخه‌ی وابستگی و فشارهای عاطفی بیرون بیایی. 💙\n\n"
                "💬 اگر درگیر رابطه‌ای هستی که احساس سردرگمی و ناامنی (یا فرسودگی) داری، "
                "برای ما توضیح بده که در چه موقعیتی قرار داری."
            )

            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
            params = {"chat_id": user_id, "text": welcome_text}
            requests.post(url, params=params)

    return "OK", 200

if name == "__main__":
    port = int(os.environ.get("PORT", 5000))  # تنظیم پورت برای Railway
    app.run(host="0.0.0.0", port=port)
