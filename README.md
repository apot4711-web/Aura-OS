# Aura OS
aura os هي توزيعة مبنية على ارش لينكس (Arch Linux) باستخدام archiso ،مزودة بسطح مكتب KDE Plasma ونواة Zen.

---

## كيف تبني التوزيعة بنفسك؟
اذا عندك نظام ارش لينكس-Arch Linux (فقط), تقدر تبني ملف ISO الخاص بـAURA OSالخطوات:

### 1. ثبت ادوات البناء
**على Arch Linux:**
```bash
sudo pacman -S archiso
```

---

### تحميل الكود المصدري
```bash
git clone https://github.com/h44-aura-dev/Aura-OS.git
```
### افتح الملف وابدا البناء
```bash
cd Aura-OS
```
**ابدأ البناء**
```bash
sudo mkarchiso -v .
```
**البناء بياخذ 10-30 دقيقة حسب قوة جهازك**

### وين تلقى الملف؟
بعد ما يخلص البناء ،ملف ISO راح يكون موجود في مجلد:
```bash
out/
```
