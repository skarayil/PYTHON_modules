# 🌱 Python Module 01 - Sınıflarla Tanışma (Nesne Yönelimli Programlamaya Giriş)

<div align="center">

![42 School](https://img.shields.io/badge/School-42-black?style=for-the-badge&logo=42)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Module](https://img.shields.io/badge/Module-python01-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

**Bahçe temasını sürdürerek Python'da sınıf (class), nesne (object), encapsulation, miras alma (inheritance) ve statik/sınıf metotlarına giriş**

</div>

---

## 🎯 Modülün Amacı

Bu modül, `python00`'da öğrenilen fonksiyon/koşul/döngü temellerinin üzerine **Nesne Yönelimli Programlama (OOP)**'yı ekler. Her egzersiz aynı `Plant` (Bitki) fikrini biraz daha ileri taşır: önce düz değişkenlerle başlar, sonra bir sınıfa dönüştürür, sonra o sınıfa davranış (metot), koruma (encapsulation) ve miras (inheritance) ekler.

### 🎓 Ana Öğrenme Hedefleri

#### 🏗️ Sınıf ve Nesne
- `class` anahtar kelimesiyle bir şablon (sınıf) tanımlamak
- `__init__` ile bir nesne oluşturulduğu anda ona başlangıç özellikleri (attribute) vermek
- `self` ile bir metodun kendi nesnesinin verilerine erişmesi

#### 🔒 Encapsulation (Kapsülleme)
- `_height`, `_age` gibi "korumalı" (leading underscore) alanlar tanımlamak
- Getter/setter metotlarıyla (`get_height`, `set_height`) veriye kontrollü erişim sağlamak
- Setter içinde geçersiz veriyi (örn. negatif değer) reddetmek

#### 🧬 Miras Alma (Inheritance)
- `class Flower(Plant):` ile ana sınıfın (`Plant`) özelliklerini alt sınıflara (`Flower`, `Tree`, `Vegetable`) aktarmak
- `super().__init__()` ve `super().show()` ile ana sınıfın metotlarını çağırmak
- Alt sınıfın `show()` metodunu override ederek kendi ek bilgisini eklemesi (polimorfizm)

#### 🧠 İleri Seviye Sınıf Araçları
- `@staticmethod`: nesneye ihtiyaç duymadan sınıf üzerinden çağrılabilen yardımcı fonksiyonlar
- `@classmethod`: sınıfın kendisini (`cls`) alıp alternatif bir kurucu (`create_anonymous`) gibi davranan metotlar
- İç içe sınıflar (nested class): `Plant._Stats` gibi bir sınıfın başka bir sınıfın içinde tanımlanması ve onun tarafından kullanılması

---

## ✨ Egzersiz Detayları

### 📋 Egzersiz Tablosu

| Egzersiz | Dosya | Konu | Temel Kavram |
|----------|-------|------|---------------|
| **ex0** | `ft_garden_intro.py` | Giriş | Değişkenler, `f-string`, henüz sınıf yok |
| **ex1** | `ft_garden_data.py` | İlk Sınıf | `class`, `__init__`, `show()` |
| **ex2** | `ft_plant_growth.py` | Davranış Ekleme | `grow()`, `age()` metotları, state güncelleme |
| **ex3** | `ft_plant_factory.py` | Nesne Listesi | Birden fazla nesne üretip listede tutmak |
| **ex4** | `ft_garden_security.py` | Encapsulation | `_height`/`_age`, getter/setter, veri doğrulama |
| **ex5** | `ft_plant_types.py` | Inheritance | `Flower`, `Tree`, `Vegetable` alt sınıfları |
| **ex6** | `ft_garden_analytics.py` | İleri OOP | `@staticmethod`, `@classmethod`, nested class, çoklu miras zinciri |

---

### **ex0 — Giriş (`ft_garden_intro.py`)**

Henüz sınıf yok; sadece değişkenler ve `f-string` ile ekrana bilgi basılıyor:

```python
def main() -> None:
    name: str = "Rose"
    height: int = 25
    age: int = 30
    print(f"Plant: {name}")
```

| Kavram | Açıklama |
|--------|----------|
| Type hint | `name: str`, `height: int` ile değişken tipini belirtmek |
| f-string | Değişkeni `{}` içine gömerek metne yerleştirmek |

---

### **ex1 — İlk Sınıf (`ft_garden_data.py`)**

```python
class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
```

`Plant("Rose", 25, 30)` dendiği anda `__init__` çalışır ve `self.name`, `self.height`, `self.age` nesneye kaydedilir.

---

### **ex2 — Davranış Ekleme (`ft_plant_growth.py`)**

`Plant` artık bir `growth` (büyüme hızı) değeriyle üretiliyor; `grow()` boyu, `age()` ise yaşı artırıyor:

```python
def grow(self) -> None:
    self.height += self.growth

def age(self) -> None:
    self._age += 1
```

7 gün boyunca döngüyle `grow()` ve `age()` çağrılıp her günün sonunda `show()` ile durum yazdırılıyor.

---

### **ex3 — Nesne Listesi (`ft_plant_factory.py`)**

Birden fazla `Plant` nesnesi bir listede tutulup `for` döngüsüyle hepsinin `show()` metodu çağrılıyor:

```python
plants = [Plant("Rose", 25.0, 30), Plant("Oak", 200.0, 365), ...]
for plant in plants:
    plant.show()
```

---

### **ex4 — Encapsulation (`ft_garden_security.py`)**

Bu egzersizde `height`/`age` doğrudan dışarıdan değiştirilebilen alanlar olmaktan çıkıp, `_height`/`_age` şeklinde "korumalı" hale geliyor. Değer değiştirmek için `set_height()`/`set_age()` çağrılması gerekiyor ve bu setter'lar negatif değerleri reddediyor:

```python
def set_height(self, h) -> None:
    if h < 0:
        print(f"{self.name}: Error, height can't be negative")
        print("Height update rejected")
    else:
        self._height = h
```

`get_height()` / `get_age()` ile mevcut değer okunuyor.

---

### **ex5 — Miras Alma (`ft_plant_types.py`)**

`Plant` artık üç alt sınıfa ayrılıyor, her biri kendi ek özelliğini ve `show()` davranışını ekliyor:

| Alt Sınıf | Ek Özellik | Ek Metot |
|-----------|------------|----------|
| `Flower` | `color`, `bloomed` | `bloom()` |
| `Tree` | `trunk_diameter` | `produce_shade()` |
| `Vegetable` | `harvest_season`, `nutritional_value` | `grow()` (override) |

```python
class Flower(Plant):
    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
```

`super().show()` çağrısı ana sınıfın `show()` metodunu çalıştırır, alt sınıf ise üstüne kendi satırlarını ekler.

---

### **ex6 — İleri OOP (`ft_garden_analytics.py`)**

Son egzersiz, önceki tüm kavramları birleştirip üstüne ekliyor:

- **Nested class**: Her `Plant`, kendi içinde tanımlı bir `_Stats` sınıfından bir istatistik nesnesi tutar (`self._stats = self._Stats()`), her `grow()`/`age()`/`show()` çağrısını sayar.
- **`@staticmethod`**: `Plant.is_older_than_a_year(age_in_days)` — nesne oluşturmadan sınıf üzerinden çağrılabilir.
- **`@classmethod`**: `Plant.create_anonymous()` — `cls("Unknown plant", 0.0, 0)` diyerek alternatif bir kurucu gibi davranır.
- **Genişletilmiş miras zinciri**: `Tree`, kendi `_TreeStats` sınıfını (`Plant._Stats`'tan miras alan) kullanır; `Seed`, `Flower`'dan miras alıp `bloom()`'u override eder.

```python
class Tree(Plant):
    class _TreeStats(Plant._Stats):
        def record_shade(self) -> None:
            self._shade += 1
```

---

## 📁 Dosya Yapısı

```
python01/
├── ex0/
│   └── ft_garden_intro.py       # Değişkenler ve f-string
├── ex1/
│   └── ft_garden_data.py        # İlk sınıf: Plant
├── ex2/
│   └── ft_plant_growth.py       # grow(), age() metotları
├── ex3/
│   └── ft_plant_factory.py      # Nesne listesi
├── ex4/
│   └── ft_garden_security.py    # Encapsulation, getter/setter
├── ex5/
│   └── ft_plant_types.py        # Flower, Tree, Vegetable (inheritance)
└── ex6/
    └── ft_garden_analytics.py   # staticmethod, classmethod, nested class
```

---

## 💻 Kullanım

Her egzersiz kendi klasöründe doğrudan çalıştırılabilir:

```bash
python3 ex1/ft_garden_data.py
python3 ex5/ft_plant_types.py
python3 ex6/ft_garden_analytics.py
```

---

## 📚 Notlar

- `self` her zaman metodun ilk parametresidir; Python bunu otomatik olarak nesnenin kendisiyle doldurur.
- `_height` gibi tek alt çizgili alanlar Python'da teknik olarak hâlâ erişilebilirdir (gerçek `private` değildir); bu bir "dokunma, dışarıdan değiştirme" kuralıdır.
- `super()` çağrısı yapılmazsa alt sınıf, ana sınıfın `__init__`'ini veya `show()`'unu otomatik miras almaz — bilinçli olarak çağrılması gerekir.

---
<div align="center">
    
### 👩‍💻 Created by Sude Naz Karayıldırım

[![42 Profile](https://img.shields.io/badge/42%20Profile-skarayil-black?style=flat-square&logo=42&logoColor=white)](https://profile.intra.42.fr/users/skarayil)
[![GitHub](https://img.shields.io/badge/GitHub-skarayil-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/skarayil)

**⭐ Eğer bu proje işinize yaradıysa, repo'ya star vermeyi unutmayın!**

</div>
