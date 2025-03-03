from flask import Flask, request
import requests

TOKEN = "7712064275:AAG2lixEH7q_JWXGwhUcndfcE4F8AD9oub4"  
WEBHOOK_URL = "http://www.doreakhar.ir:2082/"

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)