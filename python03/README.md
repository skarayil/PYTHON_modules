# ⚔️ Python Module 03 - Veri Macerası (Argümanlar, Kümeler, Üreteçler ve Comprehensions)

<div align="center">

![42 School](https://img.shields.io/badge/School-42-black?style=for-the-badge&logo=42)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Module](https://img.shields.io/badge/Module-python03-blue?style=for-the-badge)

**Bir RPG/oyun teması üzerinden komut satırı argümanları, kümeler, üreteçler (generator) ve comprehension'lar**

</div>

---

## 🎯 Modülün Amacı

Bu modül, verinin her zaman program içinden gelmediğini — terminalden (`sys.argv`) veya kullanıcı girdisinden de gelebileceğini gösterir. Buradan yola çıkarak kümelerle (set) tekrarsız veri yönetimini, üreteçlerle (generator) belleği verimli kullanmayı ve comprehension'larla döngüleri tek satıra indirmeyi öğretir.

### 🎓 Ana Öğrenme Hedefleri

#### 📟 Komut Satırı Argümanları (`sys.argv`)
- `sys.argv[0]` programın adını, `sys.argv[1:]` ise kullanıcının verdiği parametreleri tutar
- Argümanları döngüyle gezip her birini doğrulamak, geçersiz olanları atlayıp devam etmek

#### 🔢 Hazır Fonksiyonlarla Sayısal Analiz
- `sum()`, `max()`, `min()`, `len()` gibi yerleşik fonksiyonlarla liste üzerinde toplam/ortalama/en yüksek/en düşük hesaplamak

#### 📐 Matematiksel Hesaplamalar
- `math.sqrt()` ile iki nokta arası Öklid mesafesini hesaplamak
- Kullanıcıdan `"x,y,z"` formatında virgülle ayrılmış float girdisi alıp doğrulamak

#### 🎒 Sözlükle Envanter Yönetimi
- `"isim:miktar"` formatındaki argümanları `.split(":")` ile ayırıp bir sözlüğe (dict) dönüştürmek
- Yüzde hesabı, en çok/en az bulunan öğeyi manuel döngüyle bulmak

#### 🧩 Kümeler (Set) ile Tekilleştirme
- `set()` ile tekrarsız koleksiyonlar oluşturmak
- `union()`, `intersection()`, `difference()` ile kümeler arası birleşim, kesişim ve fark işlemleri

#### ♻️ Üreteçler (Generators)
- `yield` ile sonsuz veya tembel (lazy) bir veri akışı üretmek
- `next()` ile bir üreteçten tek tek değer çekmek

#### 🧪 List / Dict Comprehension
- `[x for x in liste]` ve `{k: v for k, v in ...}` yapılarıyla döngüleri tek satırda ifade etmek

---

## ✨ Egzersiz Detayları

### 📋 Egzersiz Tablosu

| Egzersiz | Dosya | Konu | Temel Kavram |
|----------|-------|------|---------------|
| **ex0** | `ft_command_quest.py` | Komut argümanları | `sys.argv` |
| **ex1** | `ft_score_analytics.py` | Skor analitiği | `sum()`, `max()`, `min()` |
| **ex2** | `ft_coordinate_system.py` | Koordinat sistemi | `math.sqrt`, girdi doğrulama |
| **ex3** | `ft_achievement_tracker.py` | Başarım takibi | `set`, `union`, `intersection`, `difference` |
| **ex4** | `ft_inventory_system.py` | Envanter sistemi | `dict`, `sys.argv`, manuel karşılaştırma |
| **ex5** | `ft_data_stream.py` | Veri akışı | `generator`, `yield`, `next()` |
| **ex6** | `ft_data_alchemist.py` | Veri simyası | List/Dict comprehension |

---

### **ex0 — Komut Argümanları (`ft_command_quest.py`)**

```python
print(f"Program name: {sys.argv[0]}")
args_count = len(sys.argv)
...
print(f"Argument {i}: {sys.argv[i]}")
```

Argüman verilmeden çalıştırılırsa `"No arguments provided!"` yazdırır; verilen her argüman numarasıyla birlikte listelenir.

---

### **ex1 — Skor Analitiği (`ft_score_analytics.py`)**

Argüman olarak verilen skorlar `int()`'e çevrilmeye çalışılır; çevrilemeyenler `"Invalid parameter"` olarak raporlanıp atlanır. Kalan geçerli skorlar üzerinden:

```python
total_score = sum(scores)
avg_score = total_score / total_players
high_score = max(scores)
low_score = min(scores)
```

---

### **ex2 — Koordinat Sistemi (`ft_coordinate_system.py`)**

Kullanıcıdan `"x,y,z"` formatında bir satır alınır, `.split(',')` ile üçe bölünür ve her parça `float()`'a çevrilmeye çalışılır. Geçersiz bir parça varsa hata mesajı verilip tekrar sorulur:

```python
dist_center = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
dist_2 = math.sqrt((pos2[0]-pos1[0])**2 + (pos2[1]-pos1[1])**2 + (pos2[2]-pos1[2])**2)
```

İlk çağrıda orijine olan mesafe, ikinci çağrıda ise iki nokta arasındaki mesafe hesaplanır.

---

### **ex3 — Başarım Takibi (`ft_achievement_tracker.py`)**

`random.sample()` ile her oyuncuya rastgele bir başarım kümesi (`set`) üretilir. Ardından küme operasyonlarıyla:

```python
all_achievements = p1.union(p2).union(p3).union(p4)
shared = p1.intersection(p2).intersection(p3).intersection(p4)
exclusive = players[i].difference(others)
missing = all_achievements.difference(players[i])
```

Tüm oyuncuların topladığı benzersiz başarımlar, ortak başarımlar, her oyuncuya özel başarımlar ve eksik başarımlar hesaplanır.

---

### **ex4 — Envanter Sistemi (`ft_inventory_system.py`)**

`sys.argv` üzerinden `"isim:miktar"` formatında parametreler okunur. Format hatalıysa veya isim tekrarlıysa uyarı verilir; geçerli olanlar `inventory` sözlüğüne eklenir:

```python
name, qty_str = arg.split(":")
inventory[name] = int(qty_str)
```

Toplam miktar, her ürünün yüzdesi hesaplanır; en çok/en az bulunan ürün, `max()`/`min()` yerine bilinçli olarak **manuel bir `while` döngüsüyle** karşılaştırılarak bulunur. Son olarak `inventory.update({"magic_item": 1})` ile sözlüğe yeni bir kayıt eklenir.

---

### **ex5 — Veri Akışı (`ft_data_stream.py`)**

```python
def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(players), random.choice(actions))
```

`gen_event()` sonsuz bir üreteçtir; `next(stream)` ile tek tek olay (event) çekilir. 1000 olay tüketildikten sonra 10 tanesi bir listeye toplanır ve `consume_event(lst)` — kendisi de bir üreteç olan bu fonksiyon — listeden rastgele elemanları `yield`leyerek tüketir.

---

### **ex6 — Veri Simyası (`ft_data_alchemist.py`)**

```python
capitalized_all = [name.capitalize() for name in players]
only_capitalized = [name for name in players if name[0].isupper()]
score_dict = {name: random.randint(0, 1000) for name in capitalized_all}
high_scores = {name: score for name, score in score_dict.items() if score > score_avg}
```

Aynı işi klasik bir `for` döngüsüyle yazmak yerine list/dict comprehension kullanarak tek satırda gerçekleştirir.

---

## 📁 Dosya Yapısı

```
python03/
├── ex0/
│   └── ft_command_quest.py        # sys.argv temelleri
├── ex1/
│   └── ft_score_analytics.py      # sum/max/min ile skor analitiği
├── ex2/
│   └── ft_coordinate_system.py    # math.sqrt ile mesafe hesabı
├── ex3/
│   └── ft_achievement_tracker.py  # set: union/intersection/difference
├── ex4/
│   └── ft_inventory_system.py     # sys.argv + dict envanter
├── ex5/
│   └── ft_data_stream.py          # generator, yield, next()
└── ex6/
    └── ft_data_alchemist.py       # list/dict comprehension
```

---

## 💻 Kullanım

```bash
# ex0, ex1, ex4 argüman alır:
python3 ex0/ft_command_quest.py arg1 arg2
python3 ex1/ft_score_analytics.py 10 20 30
python3 ex4/ft_inventory_system.py sword:3 shield:1

# ex2 terminalden interaktif girdi ister:
python3 ex2/ft_coordinate_system.py

# ex3, ex5, ex6 parametresiz çalışır:
python3 ex3/ft_achievement_tracker.py
python3 ex5/ft_data_stream.py
python3 ex6/ft_data_alchemist.py
```

---

## 📚 Notlar

- `ex4`'te en çok/en az bulunan ürün bilinçli olarak `max()`/`min()` kullanılmadan, manuel bir döngüyle bulunur; bu, algoritmanın kendisini anlamak içindir.
- `ex5`'teki üreteçler sonsuz olabilir (`while True: yield ...`); bu yüzden `next()` ile tek tek çekilmeleri gerekir, `list()` ile tamamını almaya çalışmak programı kilitler.
- `random.sample()` ve `random.choice()` her çalıştırmada farklı sonuç üretir; bu modüldeki çıktılar deterministik değildir.

---

### 👩‍💻 Created by Sude Naz Karayıldırım
