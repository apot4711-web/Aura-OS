import customtkinter as ctk
import os
import sys
import json
import webbrowser
import arabic_reshaper
from bidi.algorithm import get_display


CONFIG_DIR = os.path.expanduser("~/.config/aura-welcome")
CONFIG_FILE = os.path.join(CONFIG_DIR, "settings.json")


def check_startup_preference():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
                if not data.get("show_on_startup", True):
                    sys.exit(0)  # Close app immediately if user disabled it
        except Exception:
            pass

check_startup_preference()


def ar(text):
    return get_display(arabic_reshaper.reshape(text))

def save_preference_and_close():
    
    dont_show_again = dont_show_var.get()
    
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump({"show_on_startup": not dont_show_again}, f)
    
    app.destroy()

# Theme Setup
ctk.set_appearance_mode("Dark")      
ctk.set_default_color_theme("blue")    

app = ctk.CTk()
app.geometry("540x520")                
app.resizable(False, False)           

# App Actions
def open_discover():
    os.system("plasma-discover &")           

def open_website():
    webbrowser.open("https://github.com/apot4711-web/Aura-OS") 

# Fonts
ARABIC_FONT = ("Noto Sans Arabic", 14)
TITLE_FONT = ("Noto Sans Arabic", 22, "bold")
SUBTITLE_FONT = ("Noto Sans Arabic", 12)

ENGLISH_FONT = ("Arial", 14)
ENGLISH_TITLE_FONT = ("Arial", 22, "bold")
ENGLISH_SUBTITLE_FONT = ("Arial", 12)

current_lang = "ar"

def get_arabic_subtitle():
    lines = [
        "AURA OS",
        "توزيعة لينكس عربية مبنية على Arch Linux.",
        "مُصممة لتقديم بيئة عمل متكاملة للمطورين والمبدعين بأعلى مستويات الأداء.",
        "ابدأ رحلتك الآن!"
    ]
    reshaped = [arabic_reshaper.reshape(line) for line in lines]
    return get_display("\n".join(reshaped))

def get_english_subtitle():
    return (
        "AURA OS\n"
        "An Arabic Linux distribution based on Arch Linux.\n"
        "Designed to offer an integrated environment for developers and creators.\n"
        "Start your journey now!"
    )

# Language Toggle
def toggle_language():
    global current_lang

    if current_lang == "ar":
        current_lang = "en"
        app.title("Welcome Screen")
        title.configure(text="Welcome to Aura OS!", font=ENGLISH_TITLE_FONT)
        subtitle.configure(text=get_english_subtitle(), font=ENGLISH_SUBTITLE_FONT)
        btn_discover.configure(text="🛍️ Software Center (Discover)", font=ENGLISH_FONT)
        btn_web.configure(text="🌐 Distro GitHub", font=ENGLISH_FONT)
        btn_close.configure(text="Get Started", font=ENGLISH_FONT)
        chk_dont_show.configure(text="Don't show this message again on startup", font=("Arial", 11))
        btn_lang.configure(text=ar("العربية 🌐"), font=ARABIC_FONT)
    else:
        current_lang = "ar"
        app.title(ar("شاشة الترحيب"))
        title.configure(text=ar("مرحباً بك في Aura OS!"), font=TITLE_FONT)
        subtitle.configure(text=get_arabic_subtitle(), font=SUBTITLE_FONT)
        btn_discover.configure(text=ar("🛍️ مركز التطبيقات (Discover)"), font=ARABIC_FONT)
        btn_web.configure(text=ar("🌐 قيت هب التوزيعة"), font=ARABIC_FONT)
        btn_close.configure(text=ar("ابدأ الاستخدام"), font=ARABIC_FONT)
        chk_dont_show.configure(text=ar("عدم إظهار هذه الرسالة مرة أخرى عند التشغيل"), font=("Noto Sans Arabic", 11))
        btn_lang.configure(text="English 🌐", font=ENGLISH_FONT)



btn_lang = ctk.CTkButton(
    app, 
    text="English 🌐", 
    command=toggle_language,
    width=100,
    height=28,
    fg_color="#333333",
    hover_color="#444444"
)
btn_lang.pack(anchor="ne", padx=20, pady=(15, 0))

# 2. Title & Subtitle
title = ctk.CTkLabel(
    app, 
    text=ar("مرحباً بك في Aura OS!"), 
    font=TITLE_FONT
)
title.pack(pady=(10, 5))               

subtitle = ctk.CTkLabel(
    app, 
    text=get_arabic_subtitle(), 
    font=SUBTITLE_FONT,
    justify="center"
)
subtitle.pack(pady=(0, 20))

#Buttons
btn_discover = ctk.CTkButton(
    app, 
    text=ar("🛍️ مركز التطبيقات (Discover)"), 
    font=ARABIC_FONT,
    command=open_discover,
    width=260,
    height=38
)
btn_discover.pack(pady=8)

btn_web = ctk.CTkButton(
    app, 
    text=ar("🌐 قيت هب التوزيعة"), 
    font=ARABIC_FONT,
    command=open_website,
    width=260,
    height=38
)
btn_web.pack(pady=8)

#  Checkbox
dont_show_var = ctk.BooleanVar(value=False)
chk_dont_show = ctk.CTkCheckBox(
    app,
    text=ar("عدم إظهار هذه الرسالة مرة أخرى عند التشغيل"),
    variable=dont_show_var,
    font=("Noto Sans Arabic", 11)
)
chk_dont_show.pack(pady=(20, 10))


btn_close = ctk.CTkButton(
    app, 
    text=ar("ابدأ الاستخدام"), 
    font=ARABIC_FONT,
    command=save_preference_and_close,                
    fg_color="transparent",             
    border_width=2,
    width=140
)
btn_close.pack(pady=(10, 0))


app.mainloop()
