# 🃏 Python Module 07 - DataDeck (Soyut Kart Mimarisi / Design Patterns)

<div align="center">

![42 School](https://img.shields.io/badge/School-42-black?style=for-the-badge&logo=42)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Module](https://img.shields.io/badge/Module-python07-blue?style=for-the-badge)

**Creature tabanlı bir kart oyunu altyapısı üzerinden Abstract Factory, Capability/Mixin ve Strategy tasarım desenleri**

</div>

---

## 🎯 Modülün Amacı

Bu modül, önceki modüllerdeki temel OOP bilgisinin (`class`, miras alma) üzerine üç klasik **tasarım desenini (design pattern)** katmanlı biçimde inşa eder: nesne üretimini standartlaştırmak (Abstract Factory), yaratıklara sınıftan bağımsız yetenekler eklemek (Capability/Mixin) ve savaş mantığını dışarıdan yönetmek (Strategy).

### 🎓 Ana Öğrenme Hedefleri

#### 🏭 Abstract Factory
- Soyut bir `CreatureFactory` sınıfı tanımlayıp somut fabrikaların (`FlameFactory`, `AquaFactory`) onu implemente etmesini sağlamak
- Hangi fabrika kullanıldığını umursamadan aynı kodla (`test_factory()`) farklı yaratık aileleri üretebilmek (polimorfizm)

#### 🧩 Capabilities / Mixin
- Yaratıklara yeni bir sınıf türetmeden, bağımsız `HealCapability` ve `TransformCapability` sınıflarını çoklu miras (`class Sproutling(Creature, HealCapability)`) ile eklemek
- `isinstance(creature, HealCapability)` ile bir yaratığın hangi yetenek(ler)e sahip olduğunu çalışma zamanında kontrol etmek

#### ♟️ Strategy Pattern
- Saldırı mantığını yaratığın içine gömmek yerine, dışarıda ayrı "beyin" sınıfları (`NormalStrategy`, `AggressiveStrategy`, `DefensiveStrategy`) olarak tasarlamak
- Bir yaratığa savaşa girerken bir strateji atamak; yaratık sadece `execute()`/`act()` der, gerisini o an atanmış strateji halleder
- Uyumsuz bir strateji-yaratık kombinasyonunda (`ValueError`) turnuvanın kontrollü şekilde durmasını sağlamak

---

## ✨ Egzersiz Detayları

### 📋 Egzersiz Tablosu

| Egzersiz | Dosya | Desen | Temel Kavram |
|----------|-------|-------|---------------|
| **ex0** | `ex0/creature.py`, `ex0/factory.py`, `battle.py` | Abstract Factory | `ABC`, `@abstractmethod`, polimorfizm |
| **ex1** | `ex1/capability.py`, `ex1/creature.py`, `ex1/factory.py`, `capacitor.py` | Capability / Mixin | Çoklu miras, `isinstance` |
| **ex2** | `ex2/strategy.py`, `tournament.py` | Strategy | Davranışı dışarıdan enjekte etme |

---

### **ex0 — Abstract Factory (`battle.py`)**

Yaratıklar doğrudan elle oluşturulmaz; bir fabrikaya sipariş verilir:

```python
class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature: ...
    @abstractmethod
    def create_evolved(self) -> Creature: ...

class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()
    def create_evolved(self) -> Creature:
        return Pyrodon()
```

| Aile | Temel | Gelişmiş |
|------|-------|----------|
| 🔥 Ateş | `Flameling` | `Pyrodon` |
| 💧 Su | `Aquabub` | `Torragon` |

`test_factory()` fonksiyonu, hangi fabrika (`FlameFactory` ya da `AquaFactory`) verilirse verilsin aynı şekilde çalışır — bu polimorfizmin somut bir örneğidir.

---

### **ex1 — Capabilities / Mixin (`capacitor.py`)**

Yaratıklara yeni bir sınıf türetmeden "Heal" (iyileştirme) ve "Transform" (dönüşüm) özellikleri eklenir:

```python
class Shiftling(Creature, TransformCapability):
    def attack(self) -> str:
        if self.transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."
```

| Yetenek | Yaratıklar | Metotlar |
|---------|-----------|----------|
| 🌿 Heal | `Sproutling`, `Bloomelle` | `attack()` + `heal()` |
| 🔀 Transform | `Shiftling`, `Morphagon` | `attack()` → `transform()` → `attack()` → `revert()` |

Özellikler `Creature`'dan bağımsız yaşar; bir yaratığın hangi yeteneğe sahip olduğu `isinstance(creature, HealCapability)` ile kontrol edilir.

---

### **ex2 — Strategy Pattern (`tournament.py`)**

Karakterin saldırı mantığı kendi içine yazılmaz; dışarıda tasarlanan bir "beyin" ona atanır:

```python
class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{creature.name}' for this aggressive strategy")
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
```

| Strateji | Uyumlu Yaratık | Eylem |
|----------|-----------------|-------|
| `NormalStrategy` | Hepsi | `attack()` |
| `AggressiveStrategy` | `TransformCapability` | `transform()` → `attack()` → `revert()` |
| `DefensiveStrategy` | `HealCapability` | `attack()` → `heal()` |

`battle()` fonksiyonu, verilen tüm rakip çiftlerini (`itertools` gerektirmeden `i`, `j` döngüsüyle) bir kez eşleştirir; uyumsuz bir kombinasyon `ValueError` fırlattığında turnuva `except ValueError` ile yakalanıp kontrollü şekilde durur.

---

## 📁 Dosya Yapısı

```
python07/
├── ex0/                    ← Abstract Factory
│   ├── creature.py         Tüm yaratık sınıfları
│   ├── factory.py          Fabrika sınıfları
│   └── __init__.py         Dışarıya sadece fabrikalar açık
│
├── ex1/                    ← Capabilities (Mixin)
│   ├── capability.py       HealCapability, TransformCapability
│   ├── creature.py         Yetenekli yaratıklar
│   ├── factory.py          Yetenekli fabrikalar
│   └── __init__.py
│
├── ex2/                    ← Strategy Pattern
│   ├── strategy.py         Normal / Aggressive / Defensive strateji
│   └── __init__.py
│
├── battle.py                python3 battle.py      → ex0 testi
├── capacitor.py              python3 capacitor.py   → ex1 testi
└── tournament.py              python3 tournament.py  → ex2 testi
```

---

## 💻 Kullanım

```bash
python3 battle.py       # EX0 — Abstract Factory
python3 capacitor.py    # EX1 — Capabilities
python3 tournament.py   # EX2 — Strategy + Turnuva
```

---

## 🔗 Kural Zinciri

```
ex0  ──►  Creature + Factory sistemi kurulur
  │
  ▼
ex1  ──►  ex0'ı alır, Capability + Mixin eklenir
  │
  ▼
ex2  ──►  ex0 + ex1'i alır, Strategy + Tournament çalışır
```

---

## 📚 Notlar

- `ABC` ve `@abstractmethod`, bir sınıfın doğrudan örneklenemeyeceğini ve alt sınıfların belirli metotları implemente etmek zorunda olduğunu garanti eder.
- Çoklu miras (`class Sproutling(Creature, HealCapability)`), Python'da MRO (Method Resolution Order) kurallarına göre çözülür; her iki üst sınıfın `__init__`'i de gerektiğinde açıkça çağrılmalıdır.
- Strategy deseni sayesinde yeni bir strateji eklemek, mevcut `Creature` sınıflarına hiç dokunmadan mümkündür — bu Open/Closed prensibinin bir örneğidir.

---

## ✅ Doğrulama

```bash
python3 -m flake8 ex0/ ex1/ ex2/ battle.py capacitor.py tournament.py
python3 -m mypy   ex0/ ex1/ ex2/ battle.py capacitor.py tournament.py --strict
```

---

### 👩‍💻 Created by Sude Naz Karayıldırım
