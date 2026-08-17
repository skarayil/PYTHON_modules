# 🚨 Python Module 02 - Hata Yakalama Sanatı (Exceptions)

<div align="center">

![42 School](https://img.shields.io/badge/School-42-black?style=for-the-badge&logo=42)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Module](https://img.shields.io/badge/Module-python02-blue?style=for-the-badge)

**Bahçe temalı sıcaklık ve sulama senaryolarıyla try/except, raise, özel hata sınıfları ve finally**

</div>

---

## 🎯 Modülün Amacı

Yazılımda her şey planlandığı gibi gitmez: kullanıcı harf yerine sayı girer, dosya bulunamaz, iş kuralı ihlal edilir. Bu modül, programın çökmesini (crash) engelleyip hatayı kontrollü şekilde ele almayı; hatta bazı durumlarda kendi hatanı bilinçli olarak fırlatmayı (`raise`) öğretir.

### 🎓 Ana Öğrenme Hedefleri

#### 🛡️ Try-Except Blokları
- Hata verebilecek riskli kodu (`int(...)`) `try:` bloğuna almak
- Hatayı `except Exception as e:` ile yakalayıp programın devam etmesini sağlamak

#### 🎯 Özel Hata Yakalama
- Tek bir genel `except Exception:` yerine `ValueError`, `ZeroDivisionError`, `FileNotFoundError`, `TypeError` gibi belirli hata tiplerini ayrı ayrı yakalamak
- Python'un `match/case` yapısıyla farklı hata senaryoları üretip test etmek

#### ⚠️ Kendi Hatanı Fırlatmak (`raise`)
- Teknik olarak geçerli ama iş mantığına aykırı bir durumda (`-5` derece gibi) `raise Exception(...)` ile kontrolü ele almak

#### 🏷️ Özel Hata Sınıfları (Custom Exceptions)
- `Exception`'dan miras alarak proje için anlamlı isimlendirilmiş hata sınıfları (`PlantError`, `WaterError`) tanımlamak
- Bu sınıfları ortak bir üst sınıftan (`GardenError`) türeterek tek bir `except GardenError:` ile hepsini yakalayabilmek

#### 🧹 Temizlik Aşaması (`finally`)
- Hata olsa da olmasa da mutlaka çalışması gereken kodu `finally:` bloğuna yazmak

---

## ✨ Egzersiz Detayları

### 📋 Egzersiz Tablosu

| Egzersiz | Dosya | Konu | Temel Kavram |
|----------|-------|------|---------------|
| **ex0** | `ft_first_exception.py` | İlk güvenlik ağı | `try/except` |
| **ex1** | `ft_raise_exception.py` | Kendi hatanı fırlat | `raise Exception(...)` |
| **ex2** | `ft_different_errors.py` | Hata tipine göre davran | `except ValueError / ZeroDivisionError / FileNotFoundError / TypeError` |
| **ex3** | `ft_custom_errors.py` | Kendi hata sınıfların | `class PlantError(GardenError)` |
| **ex4** | `ft_finally_block.py` | Kesin temizlik | `try/except/finally` |

---

### **ex0 — İlk Güvenlik Ağı (`ft_first_exception.py`)**

```python
def input_temperature(temp_str: str) -> int:
    return int(temp_str)
```

`"25"` gibi geçerli bir string sorunsuz `int()`'e çevrilir; `"abc"` gönderildiğinde oluşan `ValueError`, çağıran taraftaki `try/except Exception as e:` bloğu tarafından yakalanıp programın çökmesi engellenir.

---

### **ex1 — Kendi Hatanı Fırlat (`ft_raise_exception.py`)**

`int()` dönüşümü başarılı olsa bile (örn. `100` veya `-50`), bu değerler bir bitki için mantıksız olduğundan kod bilinçli olarak hata fırlatır:

```python
if not 0 <= _degree <= 40:
    if _degree > 40:
        raise Exception(f"{_degree}°C is too hot for plants (max 40°C)")
    else:
        raise Exception(f"{_degree}°C is too cold for plants (min 0°C)")
```

---

### **ex2 — Hata Tipine Göre Davran (`ft_different_errors.py`)**

`match/case` ile beş farklı riskli işlem (`int("abc")`, `1/0`, olmayan dosya açma, `"a" + 1`, ...) üretilir ve her biri kendi spesifik `except` bloğuyla yakalanır:

```python
except ValueError as e:
    print(f"Caught ValueError: {e}")
except ZeroDivisionError as e:
    print(f"Caught ZeroDivisionError: {e}")
except FileNotFoundError as e:
    print(f"Caught FileNotFoundError: {e}")
except TypeError as e:
    print(f"Caught TypeError: {e}")
```

Bu, tek bir kör `except:` yazmak yerine hatanın tipine göre farklı davranabilmeyi gösterir.

---

### **ex3 — Kendi Hata Sınıfların (`ft_custom_errors.py`)**

```python
class GardenError(Exception):
    def __init__(self, message: str = "Garden error") -> None:
        super().__init__(message)

class PlantError(GardenError):
    ...

class WaterError(GardenError):
    ...
```

`PlantError` ve `WaterError` ayrı ayrı yakalanabildiği gibi, ortak üst sınıfları `GardenError` üzerinden tek bir `except GardenError as e:` bloğuyla da yakalanabilir — bu, büyük projelerde hata hiyerarşisi kurmanın temelidir.

---

### **ex4 — Kesin Temizlik (`ft_finally_block.py`)**

```python
try:
    for plant in plants_list:
        water_plant(plant)
except PlantError as e:
    print(f"Caught PlantError: {e}")
    return
finally:
    print("Closing watering system")
```

`water_plant()`, ismi büyük harfle başlamayan bir bitki adı geldiğinde `PlantError` fırlatır. Döngü hata sebebiyle erken sonlansa bile `finally` bloğu — "sulama sistemini kapat" — her koşulda çalışır.

---

## 📁 Dosya Yapısı

```
python02/
├── ex0/
│   └── ft_first_exception.py   # try/except temelleri
├── ex1/
│   └── ft_raise_exception.py   # raise ile kendi hatanı fırlatma
├── ex2/
│   └── ft_different_errors.py  # Hata tipine özel except blokları
├── ex3/
│   └── ft_custom_errors.py     # GardenError, PlantError, WaterError
└── ex4/
    └── ft_finally_block.py     # try/except/finally
```

---

## 💻 Kullanım

```bash
python3 ex0/ft_first_exception.py
python3 ex3/ft_custom_errors.py
```

---

## 📚 Notlar

- `except Exception:` gibi çok genel bir yakalama, hatanın gerçek nedenini gizleyebilir; mümkün olduğunca spesifik hata tipleri (`ValueError`, `ZeroDivisionError`, ...) yakalanmalıdır.
- `raise` ile fırlatılan bir hata, onu yakalayan bir `except` bulunana kadar çağrı yığınında (call stack) geriye doğru yayılır; hiçbir yerde yakalanmazsa program `Traceback` ile durur.
- `finally` bloğu, `try` içinde `return` çalışsa bile mutlaka çalışır — bu yüzden dosya/bağlantı kapatma gibi işlemler için idealdir.

---

<div align="center">
    
### 👩‍💻 Created by Sude Naz Karayıldırım

[![42 Profile](https://img.shields.io/badge/42%20Profile-skarayil-black?style=flat-square&logo=42&logoColor=white)](https://profile.intra.42.fr/users/skarayil)
[![GitHub](https://img.shields.io/badge/GitHub-skarayil-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/skarayil)

**⭐ Eğer bu proje işinize yaradıysa, repo'ya star vermeyi unutmayın!**

</div>
