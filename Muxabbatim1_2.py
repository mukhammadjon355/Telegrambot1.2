import telebot
from telebot import types
import random
from datetime import datetime, timedelta
import time
import threading

# ====== 1. API TOKEN ======
API_TOKEN = ""
bot = telebot.TeleBot(API_TOKEN)
user_ids = set()

# ====== 2. Kontentlar ======
iliq_sozlar = [
    "Sen mening eng azizimsan.", "Har tong seni o‘ylab uyg‘onaman.",
    "Sen hayotimga rang bag‘ishlaysan.", "Yuragim faqat sen uchun uradi.",
    "Sen bilan har daqiqa baxtdir.", "Ko‘zlaring — qalbimni yoritadi.",
    "Sening ovozing — yuragim ohangi.", "Sen mening ilhomimsan.",
    "Senga mehrim cheksiz.", "Sening borlig‘ing baxtim.", "Kulishlaring meni mendan oladi.",
    "borligingni o'zi bir baxt.", "Shaxlo ko'zlaring juda chiroyli.", "Bilasanmi Erkaliging ham bir yoqimli.", 
    "Sen Mening quyoshchamsan.", "Asalim o'zimni.", "Shirinim meni.", "Bazida erkalikni oshirvorsang ham sevaveraman negadur seni."
] * 3

topshiriqlar = [
    "Bugun o'zingga tabassum qil!", "Do‘stlaringga mehr ko‘rsat.",
    "Oynaga qarab, o‘zingni qadrlashni unutmang.", "Bugun ijobiy fikr bilan yur.",
    "Biror kishiga yaxshi so‘z ayt.", "Bitta orzu yozib qo‘y.",
    "Yuragingdagi eng katta orzuni esla.", "Muxammadjonga xabar yoz.",
    "Bugun arab tilidan 1 harf yodla.", "Muxabbat hayotingga go‘zallik olib kiradi.",
    "Xayollaringga diqqatli bol asalim.", "Bugub meni kunim bo'lsin erkalat meni.",
] * 3

sherlar = [
    "Sen keldingu tonglarim quyoshli,\nYashashga sabab bo‘lding beg‘ubor.",
    "Menga bir nigohing yetarli,\nQalbingda yashashni xohlayman, sevgilim.",
    "Ko‘zing porlaydi yulduzlardan ham,\nSening mehri qalbimni tutib olgan.",
    "Sen bilan hayot — shirin ertak,\nMen sendan boshqa hech kimni istamayman.",
    "Yuragimda sen, har nafasda sen,\nTuyg‘ularim faqat sen uchun.",
    "Sen kelding, qalbimni to’ldirib,\nYuragimni sevgi bilan yoritib. \nKo’zlaringda dengiz, go’zal bir dunyo, \nMening dunyom – faqat sen bilan jonli.",
    "Har so’zingda mehr, har qarashingda nur, \nMuxabbat, sen – hayotimning eng katta qurur. \nSen bilan dunyo, boshqacha go’zal, \nSen mening ilhomim, chin dildan sevgan malalim.",
    "Muxabbat, yuragim sen bilan to‘la, \nSo‘zlaring yurakni qiladi hola. \nKo‘zlaring boqsa, yuragim titraydi, \nSensiz bu dunyo ko‘zimga torla.",
    "Sen bilan har kunim bahor kabi, \nKulgingda yashnaydi ishqning nuri. \nBir jilvang yetadi osmon ochilsin, \nMuxabbat, sen – qalbimning iftixori.",
    "Senga ataladi har bir nafasim, \nSen bilan go‘zal har bir tafakkurim. \nOlamda faqat bir haqiqat bor, \nMuxabbatimsan, yuragimga nurim."
] * 6

hikoyalar = [
    "Muxabbatxon erta tongda uyg‘ondi. Yuragida iliqlik, ko‘zlarida quvonch bor edi.",
    "U oynaga qarab: 'Men baxtliman, chunki yuragimda muhabbat bor' dedi.",
    "Yomg‘ir yog‘ardi, lekin Muxabbatxon ichkarida quyoshni his qilardi.",
    "Muxammadjon unga xat yozdi: 'Sen mening yuragimsan, Muxabbatxon'.",
    "Muxabbat tongda uyg‘onib, hayotini go‘zallashtirishga qaror qildi.",
    "Yuragimdagi Ism Muxammad ertalab uyg‘onib, telefoniga qaradi. Ekranda bitta so‘z: “Muxabbat”. Shu so‘z yuragida tongni iliq qildi. Bugun yana unga yaxshi so‘z yozadi…",
    "Oynadagi Ko‘zlar Muxabbat oynaga qarab jilmaydi. “Bugun yana bir inson yuragim uchun yashaydi,” dedi u. U bilmasdi, o‘sha inson allaqachon oynadagi jilmayishga oshiq bo‘lgan edi.",
    "Ketgan Vaqt Vaqt tez o‘tardi. Lekin har kech, Muxammad qog‘ozga “Men seni yaxshi ko‘raman,” deb yozardi. Qachonlardir bu so‘zlar Muxabbatga yetib borishini bilardi.",
    "Birinchi Xat Ular hali uchrashmagan edi. Faqat bitta xat: “Salom, qalbingiz qanday?” O‘sha kundan boshlab ikki yurak orzularini bir-biriga bitib bordi.",
    "Jim So‘zlar Muxabbat hech narsa demadi. Faqat jilmaydi. Muxammad ham jim edi. Chunki sevgi ba’zida so‘zlarda emas, nigohlarda yashaydi."
] * 6

hayrli_tun_sozlar = ["Shirinim", "Jonim", "Asalim", "Sevgilim"]

# ====== 3. Visol kuni ======
target_date = datetime(2025, 11, 17)

def days_until_visol():
    return (target_date - datetime.now()).days

# ====== 4. Har soatga mo‘ljallangan xabarlar ======
def morning_message():
    return f"{random.choice(iliq_sozlar)}\n\nHayrli tong, Muxabbatim!\n\nVisol kunimizgaga {days_until_visol()} kun qoldi. Inshaallah"

def lunch_poem():
    return f"Bugungi she’r:\n\n{random.choice(sherlar)}"

def evening_story():
    return f"Bugungi hikoya:\n\n{random.choice(hikoyalar)}"

def night_message():
    return f"{random.choice(hayrli_tun_sozlar)}, yaxshi dam ol!"

# ====== 5. Bot tugmalari ======
def create_buttons():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add("Qancha kun qoldi?", "Bugungi topshiriq")
    return markup

# ====== 6. /start komandasi ======
@bot.message_handler(commands=["start"])
def handle_start(message):
    user_ids.add(message.chat.id)
    bot.send_message(
        message.chat.id,
        "Salom, Muxabbatim! Bugundan har kunlik iliq so‘zlar, topshiriqlar, she’rlar va hikoyalar sizni kutyapti!",
        reply_markup=create_buttons()
    )

# ====== 7. Tugmalarni bir marta bosish imkoniyatini tekshirish ======
used_buttons = {}

@bot.message_handler(func=lambda m: m.text == "Qancha kun qoldi?")
def send_days_left(message):
    if message.chat.id in used_buttons and "Qancha kun qoldi?" in used_buttons[message.chat.id]:
        bot.send_message(message.chat.id, "Siz bugungi kun uchun faqat bir marta bu tugmani bosishingiz Mumkun, \nasalim ozgarib qolmaydi Kunlar soni. ")
    else:
        used_buttons.setdefault(message.chat.id, []).append("Qancha kun qoldi?")
        bot.send_message(message.chat.id, f"Visol kuniga {days_until_visol()} kun qoldi.")

@bot.message_handler(func=lambda m: m.text == "Bugungi topshiriq")
def send_task(message):
    if message.chat.id in used_buttons and "Bugungi topshiriq" in used_buttons[message.chat.id]:
        bot.send_message(message.chat.id, "Siz bugungi topshiriqni faqat bir marta olish imkoniyatiga egasiz Asalim Chalg'masdan topshiriqni bajaring.")
    else:
        used_buttons.setdefault(message.chat.id, []).append("Bugungi topshiriq")
        bot.send_message(message.chat.id, f"Bugungi topshiriq:\n{random.choice(topshiriqlar)}")

# ====== 8. Avtomatik xabar yuboruvchi funksiya ======
def schedule_messages():
    sent_flags = {"08:00": False, "12:00": False, "18:00": False, "21:00": False}
    while True:
        now = datetime.now().strftime("%H:%M")
        for user_id in user_ids:
            if now == "08:00" and not sent_flags["08:00"]:
                bot.send_message(user_id, morning_message())
                sent_flags["08:00"] = True
            elif now == "12:00" and not sent_flags["12:00"]:
                bot.send_message(user_id, lunch_poem())
                sent_flags["12:00"] = True
            elif now == "18:00" and not sent_flags["18:00"]:
                bot.send_message(user_id, evening_story())
                sent_flags["18:00"] = True
            elif now == "21:00" and not sent_flags["21:00"]:
                bot.send_message(user_id, night_message())
                sent_flags["21:00"] = True

        if now == "00:00":
            for key in sent_flags:
                sent_flags[key] = False

        time.sleep(30)

# ====== 9. Botni ishga tushurish ======
if __name__ == "__main__":
    threading.Thread(target=schedule_messages).start()
    bot.infinity_polling()
