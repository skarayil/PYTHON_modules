# 🌱 Python Module 00 - Growing Code

<div align="center">

![42 School](https://img.shields.io/badge/School-42-black?style=for-the-badge&logo=42)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Module](https://img.shields.io/badge/Module-python00-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

**Python programlamaya giriş — fonksiyonlar, kullanıcı girdisi, koşullar, döngüler ve tip sistemi**

*Bu modül, Python'un temel yapı taşlarını bir bahçe teması etrafında öğretir: fonksiyon tanımlamadan özyinelemeli algoritmalara kadar adım adım ilerler.*

</div>

---

## 🎯 Modülün Amacı

Bu modül, **Python'un temel kavramlarını** bir bahçe simülasyonu teması üzerinden öğretmeyi amaçlar. Her egzersiz, bir öncekinin üzerine inşa edilerek programlamanın temel yapı taşlarını adım adım pekiştirir.

### 🎓 **Ana Öğrenme Hedefleri:**

#### 🔧 **Fonksiyon Temelleri**
- `def` anahtar kelimesiyle fonksiyon tanımlama
- Python'da scope ve girinti (indentation) kavramı
- Süslü parantez yerine iki nokta (`:`) ile blok yapısı

#### 💬 **Kullanıcı ile Etkileşim**
- `input()` ile terminal üzerinden veri alma
- `print()` ile ekrana çıktı verme
- f-string ile değişkenleri metne gömmek (`f"..."`)

#### 🔢 **Veri Türleri ve Dönüşümler**
- `input()` ile gelen verilerin varsayılan olarak `str` olması
- `int()` ile tür dönüşümü yapma
- Aritmetik işlemler: çarpma ve toplama

#### 🔀 **Koşul Yapıları**
- `if` ve `else` ile karar mekanizmaları
- Karşılaştırma operatörleri (`<=`, `>`)

#### 🔁 **Döngüler ve Özyineleme**
- `for` döngüsü ve `range()` fonksiyonu
- Recursive (özyinelemeli) fonksiyon mantığı
- Durdurma koşulunun önemi

#### ✍️ **Tip Belirtme ve Formatlama**
- Type hint'ler (`str`, `int`, `-> None`)
- `.capitalize()` ile string standardizasyonu
- `if/elif/else` ile çoklu koşul kontrolü

---

## ✨ Egzersiz Detayları

<div align="center">

![Functions](https://img.shields.io/badge/Functions-8-brightgreen?style=for-the-badge)
![Exercises](https://img.shields.io/badge/Exercises-ex0--ex7-blue?style=for-the-badge)
![Theme](https://img.shields.io/badge/Theme-Garden-orange?style=for-the-badge)

</div>

### 📋 **Egzersiz Tablosu**

| Egzersiz | Fonksiyon | Konu | Temel Kavram |
|----------|-----------|------|--------------|
| **ex0** | `ft_hello_garden` | Merhaba Dünya | `def`, `print` |
| **ex1** | `ft_garden_name` | Kullanıcı Girişi | `input`, `print` |
| **ex2** | `ft_plot_area` | Alan Hesabı | `int()`, çarpma |
| **ex3** | `ft_harvest_total` | Toplama İşlemi | `int()`, toplama |
| **ex4** | `ft_plant_age` | Bitki Yaşı | `if/else` |
| **ex5** | `ft_water_reminder` | Sulama Hatırlatıcısı | `if/else` |
| **ex6** | `ft_count_harvest_*` | Gün Sayımı | `for`, `range`, recursive |
| **ex7** | `ft_seed_inventory` | Tohum Envanteri | type hints, `elif` |

---

### **ex0 — Fonksiyon Tanımlama**

```python
def ft_hello_garden():
    print("Hello, Garden Community!")
```

| Kavram | Açıklama |
|--------|----------|
| `def` | Fonksiyon tanımlamayı başlatır |
| `:` (iki nokta) | Fonksiyonun gövdesini başlatır; `{}` yerine Python bu yapıyı kullanır |
| Girinti | Fonksiyon scope'u içindeki kodlar 4 boşluk girintili yazılır |

---

### **ex1 — Terminal İşlemleri**

```python
def ft_garden_name():
    garden_name = input("Enter garden name: ")
    print("Garden:", garden_name)
    print("Status: Growing well!")
```

| Kavram | Açıklama |
|--------|----------|
| `input()` | Terminal üzerinden kullanıcıdan string değer alır |
| `print()` | Ekrana çıktı verir; virgülle birden fazla değer yazdırılabilir |

---

### **ex2 — Veri Türü Dönüşümü ve Alan Hesabı**

```python
def ft_plot_area():
    length = int(input("Enter length: "))
    width  = int(input("Enter width: "))
    print("Plot area:", length * width)
```

| Kavram | Açıklama |
|--------|----------|
| `int()` | `input()` ile gelen string veriyi integer'a çevirir |
| Çarpma işlemi | `length * width` ile alan hesaplanır |

---

### **ex3 — Toplama İşlemi**

```python
def ft_harvest_total():
    day1 = int(input("Day 1 harvest: "))
    day2 = int(input("Day 2 harvest: "))
    day3 = int(input("Day 3 harvest: "))
    print("Total harvest:", day1 + day2 + day3)
```

`ex2` ile aynı mantık; fark olarak çarpma yerine **toplama** işlemi kullanılır.

---

### **ex4 & ex5 — Koşul Yapıları (If-Else)**

```python
# ex4 - Bitki Yaşı
def ft_plant_age():
    plant_age = int(input("Enter plant age in days: "))
    if plant_age <= 60:
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")

# ex5 - Sulama Hatırlatıcısı
def ft_water_reminder():
    water_reminder = int(input("Days since last watering: "))
    if water_reminder <= 2:
        print("Plants are fine")
    else:
        print("Water the plants!")
```

| Kavram | Açıklama |
|--------|----------|
| `if` | Koşul doğruysa çalışır |
| `else` | Koşul yanlışsa çalışır |
| `<=` | Küçük eşit karşılaştırma operatörü |

---

### **ex6 — Döngüler (Iterative & Recursive)**

Bu egzersizde aynı işi yapmanın iki farklı yolu öğrenilir:

#### 🔁 Iterative (Döngüsel) Yöntem

```python
def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        print(f"Day {i}")
    print("Harvest time!")
```

| Kavram | Açıklama |
|--------|----------|
| `range(1, n)` | 1'den n-1'e kadar sayı dizisi üretir |
| `range(1, n, 2)` | Üçüncü parametre adım miktarını belirler (1, 3, 5...) |
| `for i in range(...)` | `i` her turda sıradaki değeri alır |
| `f"Day {i}"` | f-string: metnin içine değişkeni `{}` ile gömer |

#### 🔄 Recursive (Özyinelemeli) Yöntem

```python
def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    def helper(day):
        if day > days:
            print("Harvest time!")
            return
        print(f"Day {day}")
        helper(day + 1)
    helper(1)
```

| Kavram | Açıklama |
|--------|----------|
| Özyineleme | Fonksiyonun kendisini tekrar çağırması |
| Durdurma koşulu | `if day > days` olmadan fonksiyon sonsuz döngüye girer |
| `helper(day + 1)` | Her çağrıda bir sonraki güne geçilir |

#### 🔀 **Iterative vs Recursive Karşılaştırması**

| Özellik | Iterative | Recursive |
|---------|-----------|-----------|
| **Okunabilirlik** | Doğrudan, açık | Zarif ama karmaşık |
| **Bellek Kullanımı** | Sabit | Her çağrıda stack büyür |
| **Durdurma** | `range` otomatik durur | Base case zorunlu |
| **Kullanım Alanı** | Genel döngüler | Ağaç/grafik yapıları |

---

### **ex7 — Tip Belirtme ve Formatlama**

```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()

    if unit == "packets":
        print(f"{seed_type} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_type} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
```

| Kavram | Açıklama |
|--------|----------|
| `seed_type: str` | Parametrenin `str` türünde olacağını belirtir (Type Hint) |
| `quantity: int` | Parametrenin `int` türünde olacağını belirtir |
| `-> None` | Fonksiyonun bir değer döndürmeyeceğini belirtir |
| `.capitalize()` | İlk harfi büyütür: `"tomato"` → `"Tomato"` |
| `if/elif/else` | Birden fazla koşulu sırayla kontrol eder |

---

## 📁 Dosya Yapısı

```
python00/
│
├── 📄 main.py                          # Ana test dosyası — tüm egzersizleri çalıştırır
│
├── 🌱 ex0/
│   └── ft_hello_garden.py              # Fonksiyon tanımlama
│
├── 🌿 ex1/
│   └── ft_garden_name.py               # Terminal girişi
│
├── 📐 ex2/
│   └── ft_plot_area.py                 # Alan hesabı
│
├── 🧺 ex3/
│   └── ft_harvest_total.py             # Toplama işlemi
│
├── 🌻 ex4/
│   └── ft_plant_age.py                 # Koşul yapısı
│
├── 💧 ex5/
│   └── ft_water_reminder.py            # Koşul yapısı
│
├── 📅 ex6/
│   ├── ft_count_harvest_iterative.py   # For döngüsü
│   └── ft_count_harvest_recursive.py   # Özyinelemeli fonksiyon
│
└── 🌾 ex7/
    ├── ft_seed_inventory.py            # Type hints ve elif
    └── main.py                         # ex7 için test dosyası
```
---

## 💻 Kullanım

### 🖥️ **Ana Test Dosyası ile Çalıştırma**

```bash
python3 main.py
```

Çalıştırınca aşağıdaki menü açılır:

```
🌱 Welcome to Growing Code! 🌱

Which exercise would you like to test?

0 - ft_hello_garden     (Say hello to the garden community)
1 - ft_garden_name      (Display garden name)
2 - ft_plot_area        (Calculate garden plot area)
3 - ft_harvest_total    (Add up harvest weights)
4 - ft_plant_age        (Check if plant is ready)
5 - ft_water_reminder   (Check if plants need water)
6 - ft_count_harvest    (Count days to harvest)
7 - ft_seed_inventory   (Seed inventory with type hints)
a - test all exercises

Enter your choice:
```

### 📝 **Tek Egzersizi Çalıştırma**

```bash
# Sadece belirli bir egzersizi test etmek için
cd ex2
python3 -c "from ft_plot_area import ft_plot_area; ft_plot_area()"
```

---

## 📚 Notlar

### 💡 **Öğrenme İpuçları**

#### 🔑 **Temel Kavramlar**
- Python'da her satır başındaki girinti (boşluk) kritiktir — yanlış girinti `IndentationError` verir
- `input()` her zaman `str` döndürür; sayısal işlem yapacaksan `int()` veya `float()` ile dönüştür
- f-string kullanımı (`f"..."`) klasik string birleştirmeden çok daha okunaklıdır
- Recursive fonksiyonlarda durdurma koşulunu (base case) unutursan program çöker

#### ⚠️ **Sık Yapılan Hatalar**

| Hata | Sebebi | Çözüm |
|------|--------|-------|
| `TypeError: unsupported operand type(s)` | `input()` sonucu `int()`'e çevrilmemiş | `int(input(...))` kullan |
| `IndentationError` | Yanlış girinti | 4 boşluk veya tek tab kullan |
| Sonsuz döngü (recursive) | Base case eksik | `if day > days: return` ekle |
| `NameError` | Fonksiyon çağrılmadan önce tanımlanmamış | `def` bloğunu öne al |

#### 🎯 **Best Practices**
1. Fonksiyon isimlerini anlamlı yaz: `ft_plot_area` ne yaptığını söylüyor
2. Type hint ekle: kodun ne beklediği anında anlaşılıyor
3. `.capitalize()` gibi built-in metodları öğren — çok zaman kazandırır
4. Her egzersizi `main.py` üzerinden test et

---

## 🏆 Modül Başarıları

<div align="center">

![Score](https://img.shields.io/badge/Score-Completed-gold?style=for-the-badge)
![Tests](https://img.shields.io/badge/Tests-All%20Passed-success?style=for-the-badge)
![Exercises](https://img.shields.io/badge/Exercises-ex0--ex7-brightgreen?style=for-the-badge)

### 📊 **Modül İstatistikleri**

| Metrik | Değer |
|--------|-------|
| **Toplam Egzersiz** | 8 (ex0 – ex7) |
| **Fonksiyon Sayısı** | 9 (iterative + recursive dahil) |
| **Öğrenilen Kavram** | fonksiyon, input, koşul, döngü, tip belirtme |
| **Tema** | 🌱 Bahçe simülasyonu |

</div>

---

<div align="center">

### 🎯 **Kazanılan Temel Beceriler**

![Functions](https://img.shields.io/badge/Functions-blue?style=flat-square)
![Conditionals](https://img.shields.io/badge/Conditionals-green?style=flat-square)
![Loops](https://img.shields.io/badge/Loops-orange?style=flat-square)
![Recursion](https://img.shields.io/badge/Recursion-red?style=flat-square)
![Type Hints](https://img.shields.io/badge/Type%20Hints-purple?style=flat-square)

---

**🌱 "Every great program starts with a single function — just like every great garden starts with a single seed."**

*Bu modül, Python'un temellerini sağlam bir şekilde öğrenerek ilerleyen modüllere hazırlık sağlar.*

---

### 👩‍💻 Created by Sude Naz Karayıldırım

[![42 Profile](https://img.shields.io/badge/42%20Profile-skarayil-black?style=flat-square&logo=42&logoColor=white)](https://profile.intra.42.fr/users/skarayil)
[![GitHub](https://img.shields.io/badge/GitHub-skarayil-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/skarayil)

**⭐ Eğer bu proje işinize yaradıysa, repo'ya star vermeyi unutmayın!**

</div>
