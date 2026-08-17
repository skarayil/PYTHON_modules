# 🔮 Python Module 10 - FuncMage (Fonksiyonel Programlama)

<div align="center">

![42 School](https://img.shields.io/badge/School-42-black?style=for-the-badge&logo=42)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Module](https://img.shields.io/badge/Module-python10-blue?style=for-the-badge)

**Büyücülük/sihir temasıyla lambda, higher-order fonksiyonlar, closure, `functools` ve decorator'lar**

</div>

---

## 🎯 Modülün Amacı

Klasik `for`/`while` döngüleri ve upuzun fonksiyonlar yazmak yerine, fonksiyonları birer veri gibi kullanarak (First-Class Citizen) daha az kodla daha esnek çözümler üretmeyi öğretir. Beş aşamalı bu modül, `lambda`'dan başlayıp decorator'larla biter.

### 🎓 Ana Öğrenme Hedefleri

#### ⚡ Lambda ve Yerleşik Fonksiyonlar
- İsimsiz, tek satırlık `lambda` fonksiyonları yazmak
- Bunları `sorted(key=...)`, `filter(...)`, `map(...)` ile birleştirmek

#### 🔁 Higher-Order Functions
- Bir fonksiyonu başka bir fonksiyona parametre olarak geçmek
- Bir fonksiyonun, çağrıldığında yeni bir fonksiyon **döndürmesi**

#### 🧠 Closure & Scope
- İç içe tanımlanan bir fonksiyonun, dış fonksiyonun o anki durumunu "hatırlaması" (closure)
- `global` yerine `nonlocal` anahtar kelimesiyle bu durumu güncellemek

#### 🧰 `functools` Kütüphanesi
- `functools.reduce()` ile bir listeyi kümülatif olarak tek bir değere indirgemek
- `functools.partial()` ile bazı argümanları önceden sabitlemek
- `@functools.lru_cache` ile tekrarlı hesaplamaları önbelleğe almak (memoization)
- `@functools.singledispatch` ile gelen verinin tipine göre farklı davranmak

#### 🎁 Decorators
- `@functools.wraps` kullanarak orijinal fonksiyonun kimliğini (adı, docstring'i) koruyarak onu sarmalamak
- Parametre alan decorator'lar (`power_validator(min_power)`) yazmak
- `@staticmethod` ile bir sınıfın örneğine ihtiyaç duymadan çağrılabilen metotlar tanımlamak

---

## ✨ Egzersiz Detayları

### 📋 Egzersiz Tablosu

| Egzersiz | Dosya | Konu | Temel Kavram |
|----------|-------|------|---------------|
| **ex0** | `lambda_spells.py` | Lambda & Built-ins | `lambda`, `sorted`, `filter`, `map` |
| **ex1** | `higher_magic.py` | Higher-Order Functions | Fonksiyon parametre/dönüş değeri olarak |
| **ex2** | `scope_mysteries.py` | Closure & Scope | `nonlocal` |
| **ex3** | `functools_artifacts.py` | `functools` | `reduce`, `partial`, `lru_cache`, `singledispatch` |
| **ex4** | `decorator_mastery.py` | Decorators | `@wraps`, parametreli decorator, `@staticmethod` |

---

### **ex0 — Lambda & Built-ins (`lambda_spells.py`)**

```python
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact['power'], reverse=True)

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))

def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))
```

`mage_stats()` ise `min`, `max`, `sum`, `len` ve `round` fonksiyonlarını bir arada kullanarak bir listeden istatistik (min/max/ortalama güç) çıkarır.

---

### **ex1 — Higher-Order Functions (`higher_magic.py`)**

```python
def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified
```

| Fonksiyon | Ne Yapar |
|-----------|----------|
| `spell_combiner` | İki fonksiyonu alıp ikisini de çalıştıran ve sonuçları `tuple` olarak döndüren bir fonksiyon üretir |
| `power_amplifier` | Bir fonksiyonun gücünü dışarıdan verilen bir çarpanla artıran yeni bir fonksiyon döndürür |
| `conditional_caster` | Bir koşul fonksiyonu sağlanmazsa `"Spell fizzled"` döndürür |
| `spell_sequence` | Bir fonksiyon listesini sırayla çalıştırıp sonuçları liste olarak döndürür |

---

### **ex2 — Closure & Scope (`scope_mysteries.py`)**

```python
def mage_counter() -> Callable:
    count: int = 0
    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter
```

`mage_counter()`'dan üretilen her sayaç kendi izole hafızasında `count` değerini tutar; birden fazla sayaç birbirini etkilemez. `memory_vault()`, `store`/`recall` adında iki iç fonksiyon döndürerek dışarıdan doğrudan erişilemeyen bir "hafıza kasası" oluşturur.

---

### **ex3 — `functools` Kütüphanesi (`functools_artifacts.py`)**

```python
@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0: return 0
    if n == 1: return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
```

| Fonksiyon | `functools` Aracı | Amaç |
|-----------|--------------------|------|
| `spell_reducer` | `functools.reduce` | Listeyi kümülatif olarak tek değere indirger (`add`, `multiply`, `max`, `min`) |
| `partial_enchanter` | `functools.partial` | Bazı argümanları (`power`, `element`) önceden sabitler |
| `memoized_fibonacci` | `functools.lru_cache` | Tekrarlı fibonacci hesaplarını önbelleğe alır |
| `spell_dispatcher` | `functools.singledispatch` | Gelen verinin tipine (`int`, `str`, `list`) göre farklı davranır |

---

### **ex4 — Decorators (`decorator_mastery.py`)**

```python
def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Spell completed in {time.time() - start:.3f} seconds")
        return result
    return wrapper
```

| Decorator | Görevi |
|-----------|--------|
| `spell_timer` | Fonksiyonun çalışma süresini ölçer |
| `power_validator(min_power)` | Yetersiz güçle çağrılan fonksiyonu hiç çalıştırmadan reddeder |
| `retry_spell(max_attempts)` | Fonksiyon `Exception` fırlatırsa belirtilen sayıda tekrar dener |

`MageGuild` sınıfı, `@staticmethod` ile işaretlenmiş `validate_mage_name()` metodunu (nesne oluşturmadan `MageGuild.validate_mage_name(...)` şeklinde) ve `@power_validator(min_power=10)` ile korunan bir `cast_spell()` metodunu bir araya getirir.

---

## 📁 Dosya Yapısı

```
python10/
├── ex0/
│   └── lambda_spells.py          # lambda, sorted, filter, map
├── ex1/
│   └── higher_magic.py           # Higher-order functions
├── ex2/
│   └── scope_mysteries.py        # Closure, nonlocal
├── ex3/
│   └── functools_artifacts.py    # reduce, partial, lru_cache, singledispatch
└── ex4/
    └── decorator_mastery.py      # Decorators, @staticmethod
```

---

## 💻 Kullanım

Projede harici hiçbir bağımlılık yoktur (sadece standart kütüphane). Her aşama doğrudan çalıştırılabilir:

```bash
python3 ex0/lambda_spells.py
python3 ex1/higher_magic.py
python3 ex2/scope_mysteries.py
python3 ex3/functools_artifacts.py
python3 ex4/decorator_mastery.py
```

---

## 📚 Notlar

- Bu modülde bilinçli olarak kod içi yorum/docstring bırakılmamıştır; kod, isimlendirme ve yapısıyla kendini anlatmayı hedefler.
- Tüm fonksiyonlarda tip belirteci (`Callable`, `int`, `list`, `str`, ...) kullanılmıştır.
- `eval`/`exec` gibi riskli yapılar kullanılmamıştır; sadece standart kütüphane (`functools`, `operator`, `time`) ile çalışılmıştır.

---

## ✅ Doğrulama

```bash
python3 -m flake8 ex0/ ex1/ ex2/ ex3/ ex4/
python3 -m mypy   ex0/ ex1/ ex2/ ex3/ ex4/ --strict
```

---

### 👩‍💻 Created by Sude Naz Karayıldırım
