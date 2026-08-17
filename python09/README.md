# 🚀 Python Module 09 - Uzay Yolculuğu (Pydantic ile Veri Doğrulama)

<div align="center">

![42 School](https://img.shields.io/badge/School-42-black?style=for-the-badge&logo=42)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Module](https://img.shields.io/badge/Module-python09-blue?style=for-the-badge)

**Uzay istasyonu / uzaylı temas raporu / görev mürettebatı senaryolarıyla Pydantic tabanlı veri doğrulama**

</div>

---

## 🎯 Modülün Amacı

Bu modül, elle yazılan `if h < 0: ...` gibi doğrulama kodlarının yerine **Pydantic**'in `BaseModel` sınıfını kullanarak veri doğrulamayı nasıl bildirimsel (declarative) şekilde tanımlayacağımızı öğretir. Alan tipleri, sınır değerleri (`ge`/`le`, `min_length`/`max_length`) ve alanlar arası iş kuralları (`model_validator`) ile geçersiz veri, nesne oluşturulduğu anda otomatik olarak reddedilir.

### 🎓 Ana Öğrenme Hedefleri

#### 📐 `BaseModel` ve `Field`
- Pydantic'in `BaseModel` sınıfından türeyerek veri şeması (schema) tanımlamak
- `Field(..., ge=..., le=..., min_length=..., max_length=...)` ile bir alanın zorunlu olup olmadığını ve sınır değerlerini belirtmek
- `Optional[str]` ile isteğe bağlı alanlar tanımlamak, varsayılan değer (`is_active: bool = True`) atamak

#### 🏷️ `Enum` ile Kısıtlı Değer Kümeleri
- `class Rank(str, Enum):` gibi hem `str` hem `Enum`'dan türeyen sınıflarla, bir alanın yalnızca belirli önceden tanımlı değerleri alabilmesini sağlamak (`cadet`, `officer`, `lieutenant`, ...)

#### 🔗 `model_validator` ile İş Kuralları
- `@model_validator(mode="after")` dekoratörüyle, tüm alanlar tek tek doğrulandıktan **sonra** birden fazla alanı birlikte kontrol eden özel kurallar yazmak
- Kural ihlalinde `raise ValueError(...)` fırlatarak Pydantic'in bunu otomatik olarak bir doğrulama hatasına çevirmesini sağlamak

#### 🧩 İç İçe Modeller
- Bir modelin başka bir modeli içeren bir liste alanına sahip olması (`crew: List[CrewMember]`) ve iç modelin de kendi doğrulama kurallarına tabi olması

---

## ✨ Egzersiz Detayları

### 📋 Egzersiz Tablosu

| Egzersiz | Dosya | Model(ler) | Temel Kavram |
|----------|-------|------------|---------------|
| **ex0** | `space_station.py` | `SpaceStation` | Temel `BaseModel` + `Field` sınırları |
| **ex1** | `alien_contact.py` | `AlienContact`, `ContactType` | `Enum`, `model_validator` ile iş kuralları |
| **ex2** | `space_crew.py` | `CrewMember`, `SpaceMission`, `Rank` | İç içe modeller (`List[CrewMember]`), çoklu iş kuralı |

---

### **ex0 — Temel Doğrulama (`space_station.py`)**

```python
class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)
```

`SpaceStation(...)` çağrısı, verilen her alanı otomatik olarak tipine ve `Field` içinde belirtilen sınırlara göre doğrular; örneğin `crew_size=25` verilirse (üst sınır 20) Pydantic bir `ValidationError` fırlatır.

---

### **ex1 — Enum ve İş Kuralları (`alien_contact.py`)**

```python
class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"
```

Alan bazlı doğrulamanın (`Field`) yetmediği durumlar için `@model_validator(mode="after")` kullanılır — bu, tüm alanlar geçerli olduktan **sonra** çalışan ve birden fazla alanı birlikte kontrol edebilen bir doğrulayıcıdır:

```python
@model_validator(mode="after")
def validate_business_rules(self) -> "AlienContact":
    if not self.contact_id.startswith("AC"):
        raise ValueError('Contact ID must start with "AC"')

    if self.contact_type == ContactType.physical and not self.is_verified:
        raise ValueError("Physical contact reports must be verified")

    if self.contact_type == ContactType.telepathic and self.witness_count < 3:
        raise ValueError("Telepathic contact requires at least 3 witnesses")

    if self.signal_strength > 7.0 and not self.message_received:
        raise ValueError("Strong signals (>7.0) should include received messages")

    return self
```

Uygulanan iş kuralları:

| Kural | Açıklama |
|-------|----------|
| ID formatı | `contact_id` `"AC"` ile başlamalı |
| Fiziksel temas | `physical` tipi temaslar `is_verified=True` olmalı |
| Telepatik temas | En az 3 tanık (`witness_count >= 3`) gerekir |
| Güçlü sinyal | `signal_strength > 7.0` ise `message_received` dolu olmalı |

---

### **ex2 — İç İçe Modeller (`space_crew.py`)**

```python
class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"

class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    duration_days: int = Field(..., ge=1, le=3650)
    ...
```

`SpaceMission`, kendi alanlarının yanı sıra bir `CrewMember` listesi içerir — her bir mürettebat üyesi de kendi `Field` sınırlarına göre ayrıca doğrulanır. `@model_validator` ile eklenen görev bazlı kurallar:

| Kural | Açıklama |
|-------|----------|
| ID formatı | `mission_id` `"M"` ile başlamalı |
| Liderlik | Mürettebatta en az bir `commander` veya `captain` bulunmalı |
| Deneyim | `duration_days > 365` ise mürettebatın en az %50'si `years_experience >= 5` olmalı |
| Aktiflik | Mürettebatta `is_active=False` olan kimse bulunmamalı |

---

## 📁 Dosya Yapısı

```
python09/
├── ex0/
│   └── space_station.py    # BaseModel + Field temelleri
├── ex1/
│   └── alien_contact.py    # Enum + model_validator ile iş kuralları
└── ex2/
    └── space_crew.py       # İç içe modeller + çoklu iş kuralı
```

---

## 💻 Kullanım

```bash
python3 ex0/space_station.py
python3 ex1/alien_contact.py
python3 ex2/space_crew.py
```

Her dosyanın `main()` fonksiyonu, kuralları sağlayan geçerli bir örnek oluşturup alanlarını ekrana yazdırır.

---

## 📚 Notlar

- Bu modül, standart Python kütüphanesinde yer almayan **`pydantic`** paketini gerektirir (`pip install pydantic`).
- `Field(..., ...)` içindeki `...` (Ellipsis), o alanın **zorunlu** olduğu, varsayılan değeri olmadığı anlamına gelir.
- `model_validator(mode="after")`, alan bazlı (`Field`) doğrulamalardan **sonra** çalışır; bu yüzden `self.contact_type` gibi alanlara güvenle erişilebilir — aksi halde henüz doğrulanmamış/eksik olabilirlerdi.
- Bir doğrulama kuralı ihlal edildiğinde Pydantic, `raise ValueError(...)` çağrısını yakalayıp kendi `ValidationError` istisnasına dönüştürür.

---

<div align="center">
    
### 👩‍💻 Created by Sude Naz Karayıldırım

[![42 Profile](https://img.shields.io/badge/42%20Profile-skarayil-black?style=flat-square&logo=42&logoColor=white)](https://profile.intra.42.fr/users/skarayil)
[![GitHub](https://img.shields.io/badge/GitHub-skarayil-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/skarayil)

**⭐ Eğer bu proje işinize yaradıysa, repo'ya star vermeyi unutmayın!**

</div>
