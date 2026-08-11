# Mrd OS
mrd os هي توزيعة مبنية على ارش لينكس (Arch Linux) باستخدام archiso ،مزودة بسطح مكتب KDE Plasma ونواة Zen.

---

## كيف تبني التوزيعة بنفسك؟
اذا عندك نظام لينكس (اي توزيعة)، تقدر تبني ملف ISO الخاص بـ Mrd-OS بهذه الخطوات:

### 1. ثبت ادوات البناء
**على Arch Linux:**
```bash
sudo pacman -S archiso
```
**على Fedora:**
```bash
sudo dnf install archiso
```
**على Ubuntu / Debian:**
```bash
sudo apt install archiso
```

---

### تحميل الكود المصدري
```bash
git clone https://github.com/apot4711-web/Mrd-OS.git
```
### افتح الملف وابدا البناء
```bash
cd Mrd-OS
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
