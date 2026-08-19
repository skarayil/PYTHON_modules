# 🐍 Python Modules

<div align="center">

![42 School](https://img.shields.io/badge/School-42-black?style=for-the-badge&logo=42)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Modules](https://img.shields.io/badge/Modules-python00--python10-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

**42 Kocaeli Python Piscine — python00'dan python10'a, temel sözdiziminden Design Patterns'a uzanan tüm modüllerin toplandığı ana repo.**

[Kurulum](#-kurulum) • [Modül Haritası](#-modül-haritası) • [Python Nasıl Çalışır](#️-python-nasıl-çalışır) • [Kullanım](#-kullanım)

</div>

---

## 🎯 Repo Hakkında

<div align="center">
  <img
    alt="Python Modules Animation"
    width="500"
    src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2M3NXczazJteXdxZ3pwcWFqaGFlZTNhZ2s0cWk3b3k4bDVjdTZmMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/37mOoBDsOjKdFGqXaZ/giphy.gif"
  >
</div>

<br>

Bu repo, 42 Kocaeli'nin Python Piscine müfredatını baştan sona takip eden **11 modülü** (`python00` → `python10`) tek bir çatı altında toplar. Her modül bir öncekinin üzerine inşa edilir; fonksiyon tanımlamayla başlayıp, veri yapıları, hata yönetimi, dosya I/O, OOP, Design Patterns, sanal ortamlar/pydantic ve fonksiyonel programlama ile biter.

Her modülün kendi klasöründe, o modüle özel **detaylı bir README.md** bulunur (metaforlar, adım adım anlatım, kod örnekleri dahil). Bu ana README ise **tüm haritayı** tek bakışta görmeniz için hazırlandı.


---

## 🗺️ Modül Haritası

| # | Modül | Tema | Ana Konu |
|---|-------|------|----------|
| [`python00`](./python00) | 🌱 Growing Code | Bahçe | Fonksiyonlar, `input`/`print`, koşullar, döngüler, recursion, type hints |
| [`python01`](./python01) | 🌿 Gizemli Bahçe | Botanik Bahçesi | List, Dictionary, Tuple, Set, iç içe veri yapıları |
| [`python02`](./python02) | 🚨 Hata Yakalama Sanatı | Bahçe | `try/except`, `raise`, custom exceptions, `finally` |
| [`python03`](./python03) | ⚔️ Veri Macerası | RPG | String manipülasyonu, f-string, `split`/`join`, sözlük yönetimi, set işlemleri |
| [`python04`](./python04) | 📜 Kadim Parşömenler I | Kadim Parşömenler | Dosya okuma/yazma (`r`/`w`/`a`), context manager (`with`) |
| [`python05`](./python05) | 📜 Kadim Parşömenler II | Kadim Parşömenler | `seek`/`tell`, akış yönetimi, güvenli dosya erişimi |
| [`python06`](./python06) | 📜 Kadim Parşömenler III | Kadim Parşömenler | Kapsamlı dosya I/O pratiği, hata güvenliği |
| [`python07`](./python07) | 🃏 DataDeck | Kart Oyunu | Abstract Factory, Capability/Mixin, Strategy Pattern |
| [`python08`](./python08) | 🖥️ Matrix Environment | Matrix | Sanal ortamlar, `pyproject.toml`/`requirements.txt`, `.env` & environment variables |
| [`python09`](./python09) | 🚀 Uzay Yolculuğu | Uzay | OOP temelleri, `__init__`, `self`, inheritance, Pydantic veri doğrulama |
| [`python10`](./python10) | 🧙 FuncMage | Büyücülük | Lambda, higher-order functions, closures, `functools`, decorators |

```
python_modules/
├── python00/   Growing Code           (Fonksiyon temelleri)
├── python01/   Gizemli Bahçe          (Veri yapıları)
├── python02/   Hata Yakalama Sanatı   (Exceptions)
├── python03/   Veri Macerası          (String/Veri işleme)
├── python04/   Kadim Parşömenler I    (Dosya I/O)
├── python05/   Kadim Parşömenler II   (Dosya I/O — seek/tell)
├── python06/   Kadim Parşömenler III  (Dosya I/O — kasa güvenliği)
├── python07/   DataDeck               (Design Patterns)
├── python08/   Matrix Environment     (Venv & Env Variables)
├── python09/   Uzay Yolculuğu         (OOP & Pydantic)
├── python10/   FuncMage               (Fonksiyonel Programlama)
└── README.md   ← şu an okuduğunuz dosya
```

---

## 🚀 Kurulum

### 📋 **Ön Gereksinimler**

![Python3](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)
![Unix](https://img.shields.io/badge/Unix-Compatible-green?style=flat-square&logo=linux&logoColor=white)

- **Python 3**: `python3 --version` ile kontrol edilebilir
- **Unix-like System**: Linux, macOS, WSL

### 📥 **Repository Klonlama**

```bash
git clone https://github.com/skarayil/python_modules.git
cd python_modules/python00
```

> Farklı bir modülü incelemek isterseniz `cd python_modules/python07` gibi ilgili klasöre geçmeniz yeterli — her modül kendi içinde bağımsız çalışabilir şekilde tasarlanmıştır (bazıları `pydantic`, `pandas`, `python-dotenv` gibi ek bağımlılıklar gerektirir; ilgili modülün README'sindeki kurulum adımlarına bakınız).

---

## ⚙️ Python Nasıl Çalışır?

Python kodu yazıldığından itibaren çalıştırılabilir hale gelene kadar şu aşamalardan geçer:

```
.py dosyası  →  Bytecode (.pyc)  →  Python Virtual Machine (PVM)  →  Bilgisayar
  (Kaynak)       (Ara format)         (Yorumlayıcı)                  (İşlemci)
```

| Aşama | Açıklama |
|-------|----------|
| **Python dosyası (.py)** | Bizim yazdığımız insan okunabilir kaynak kod |
| **Bytecode (.pyc)** | Kaynak kodun makineye yakın ara formata çevrilmiş hali |
| **Python Virtual Machine** | Bytecode'u okuyup işlemlere çeviren sanal makine |
| **Bilgisayar** | Gerçek işlemlerin donanım üzerinde çalıştırıldığı katman |

---

## 💻 Kullanım

Her modülün kendi `README.md`'si, o modüle özel çalıştırma komutlarını ve örnek çıktıları içerir. Genel mantık şu şekildedir:

```bash
# Bir modülün klasörüne gir
cd python00

# Ana test dosyası varsa onu çalıştır
python3 main.py

# Veya belirli bir egzersizi doğrudan çalıştır
cd ex2
python3 -c "from ft_plot_area import ft_plot_area; ft_plot_area()"
```

Design Pattern (`python07`) ve OOP/Pydantic (`python09`) gibi modüllerde egzersizler doğrudan çalıştırılabilir script'lerdir:

```bash
cd python07
python3 battle.py       # Abstract Factory
python3 capacitor.py    # Capabilities / Mixin
python3 tournament.py   # Strategy Pattern

cd ../python09/ex0
python3 space_station.py
```

Sanal ortam / bağımlılık yönetimi gerektiren modüllerde (`python08`):

```bash
cd python08/ex1
poetry install        # veya: pip install -r requirements.txt
python3 loading.py
```

---

## 🧪 Doğrulama (flake8 & mypy)

Kod kalitesi standart olarak `flake8` (PEP-8) ve `mypy --strict` (tip kontrolü) ile denetlenir. Örnek:

```bash
python3 -m flake8 python07/ex0 python07/ex1 python07/ex2
python3 -m mypy   python07/ex0 python07/ex1 python07/ex2 --strict
```

---

## 📚 Genel Öğrenme Yolculuğu

```
python00 ──► Fonksiyon & değişken temelleri
   │
   ▼
python01 ──► Veri yapıları (list/dict/tuple/set)
   │
   ▼
python02 ──► Hata yönetimi (try/except/raise/finally)
   │
   ▼
python03 ──► String & veri işleme (RPG temalı)
   │
   ▼
python04-06 ──► Dosya I/O (okuma, yazma, seek/tell, güvenlik)
   │
   ▼
python07 ──► Design Patterns (Abstract Factory, Mixin, Strategy)
   │
   ▼
python08 ──► Sanal ortam & environment variables
   │
   ▼
python09 ──► OOP temelleri & Pydantic veri doğrulama
   │
   ▼
python10 ──► Fonksiyonel programlama (lambda, closure, decorator)
```

---

<div align="center">

### 👨‍💻 Created by Sude Naz Karayıldırım

[![42 Profile](https://img.shields.io/badge/42%20Profile-skarayil-black?style=flat-square&logo=42&logoColor=white)](https://profile.intra.42.fr/users/skarayil)
[![GitHub](https://img.shields.io/badge/GitHub-skarayil-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/skarayil)

**⭐ Eğer bu proje işinize yaradıysa, repo'ya star vermeyi unutmayın!**

</div>
