# 🧬 Python Module 08 - Matrix Environment (Sanal Ortamlar ve Bağımlılık Yönetimi)

<div align="center">

![42 School](https://img.shields.io/badge/School-42-black?style=for-the-badge&logo=42)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Module](https://img.shields.io/badge/Module-python08-blue?style=for-the-badge)

**"Matrix" temasıyla sanal ortamlar, bağımlılık yönetimi ve environment variable'lar**

</div>

---

## 🎯 Modülün Amacı

Bu modül, bir Python projesini sisteme zarar vermeden geliştirmenin üç temel aracını öğretir: **sanal ortamlar** ile paket kurulumunu izole etmek, **bağımlılık yönetimi** ile üçüncü parti kütüphaneleri kontrollü şekilde kullanmak, ve **environment variable'lar** ile hassas bilgileri (API anahtarı gibi) kod dışında tutmak.

### 🎓 Ana Öğrenme Hedefleri

#### 🧪 Sanal Ortam (Virtual Environment)
- `VIRTUAL_ENV` ortam değişkeninin varlığına bakarak programın izole bir ortamda mı yoksa global sistemde mi çalıştığını tespit etmek
- `python -m venv` ve `source .../activate` ile bir sanal ortam oluşturup aktif etmek

#### 📦 Bağımlılık Yönetimi
- `importlib.util.find_spec()` ile bir paketin import etmeden yüklü olup olmadığını kontrol etmek
- `pyproject.toml` (Poetry) ve `requirements.txt` (pip) ile proje bağımlılıklarını tanımlamak
- Eksik paket varsa kurulum komutunu kullanıcıya göstermek

#### 🔐 Environment Variables
- Hassas verileri (`API_KEY`, `DATABASE_URL`) kodun içine yazmak yerine `.env` dosyasında saklamak
- `python-dotenv` kütüphanesinin `load_dotenv()` fonksiyonuyla bu değişkenleri `os.environ`'a yüklemek
- `os.environ.get(key, default)` ile bir değişkeni varsayılan değerle güvenle okumak
- Zorunlu bir değişken (`API_KEY`) eksikse programı `sys.exit(1)` ile kontrollü şekilde durdurmak

---

## ✨ Egzersiz Detayları

### 📋 Egzersiz Tablosu

| Egzersiz | Dosya | Konu | Temel Kavram |
|----------|-------|------|---------------|
| **ex0** | `construct.py` | Sanal ortam kontrolü | `os.environ.get("VIRTUAL_ENV")` |
| **ex1** | `loading.py` | Bağımlılık kontrolü + analiz | `importlib.util.find_spec`, pandas/numpy/matplotlib |
| **ex2** | `oracle.py` | Environment variables | `python-dotenv`, `.env`, doğrulama |

---

### **ex0 — Sanal Ortam Kontrolü (`construct.py`)**

```python
venv = os.environ.get("VIRTUAL_ENV")
status = "Welcome to the construct" if venv else "You're still plugged in"
```

| Durum | Mesaj | Açıklama |
|-------|-------|----------|
| ✅ Sanal ortam aktif | `Welcome to the construct` | İzole ortam; `site.getsitepackages()[0]` ile paket kurulum yolu gösterilir |
| ❌ Global ortam | `You're still plugged in` | Sanal ortam oluşturma adımları terminale yazdırılır |

```bash
python -m venv matrix_env
source matrix_env/bin/activate   # Unix/macOS
matrix_env\Scripts\activate      # Windows
```

---

### **ex1 — Bağımlılık Yönetimi (`loading.py`)**

`check_deps()`, gerekli kütüphanelerin (`pandas`, `numpy`, `matplotlib`) yüklü olup olmadığını `importlib.util.find_spec()` ile kontrol eder:

```python
spec = importlib.util.find_spec(pkg)
if spec is None:
    print(f"  [MISSING] {pkg}")
else:
    mod = importlib.import_module(pkg)
    version = getattr(mod, "__version__", "unknown")
```

Tüm bağımlılıklar mevcutsa `run_analysis()` çağrılır: `numpy` ile 1000 rastgele veri noktası üretilir, `pandas` ile 50 birimlik hareketli ortalama (rolling mean) hesaplanır ve `matplotlib` ile grafik `matrix_analysis.png` olarak kaydedilir.

| Paket | Görev |
|-------|-------|
| `numpy` | Sayısal veri üretimi |
| `pandas` | Veri çerçevesi + rolling mean |
| `matplotlib` | Grafik oluşturma ve kaydetme |

---

### **ex2 — Environment Variables (`oracle.py`)**

```python
load_dotenv()
return {
    "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
    "API_KEY": os.getenv("API_KEY", ""),
    ...
}
```

| Değişken | Varsayılan | Açıklama |
|----------|------------|----------|
| `MATRIX_MODE` | `development` | `development` veya `production` |
| `DATABASE_URL` | `sqlite:///matrix_local.db` | Veri tabanı bağlantı adresi |
| `API_KEY` | *(boş)* | Zorunlu — eksikse `validate_config()` programı durdurur |
| `LOG_LEVEL` | `DEBUG` | Loglama seviyesi |
| `ZION_ENDPOINT` | `http://zion.local:8080` | Ağ uç noktası |

`validate_config()`, `API_KEY` boşsa ve `MATRIX_MODE` beklenen iki değerden biri değilse hata verip `sys.exit(1)` çağırır. `security_check()` ayrıca `.env` dosyasının var olup olmadığını kontrol eder.

> ⚠️ `.env` dosyası asla Git'e eklenmemelidir (`ex2/.gitignore` bunu zaten hariç tutar); şablonu `.env.example` olarak paylaşılır.

---

## 📁 Dosya Yapısı

```
python08/
├── ex0/
│   └── construct.py        ← Sanal ortam kontrol scripti
│
├── ex1/
│   ├── loading.py           ← Bağımlılık kontrolü + analiz
│   ├── pyproject.toml       ← Proje & bağımlılık tanımları (Poetry)
│   └── requirements.txt     ← pip için bağımlılık listesi
│
└── ex2/
    ├── oracle.py             ← Environment variable okuma & doğrulama
    ├── .env.example          ← Değişken şablonu (versiyon kontrolüne girer)
    ├── .gitignore             ← .env dosyasını gizler
    └── requirements.txt       ← python-dotenv bağımlılığı
```

---

## 💻 Kullanım

```bash
# ex0 — Sanal ortam kontrolü
python3 ex0/construct.py

# ex1 — Bağımlılık kontrolü & analiz
pip install -r ex1/requirements.txt   # veya: cd ex1 && poetry install
python3 ex1/loading.py

# ex2 — Environment variables
cp ex2/.env.example ex2/.env          # .env dosyasını oluştur ve doldur
pip install -r ex2/requirements.txt
python3 ex2/oracle.py
```

---

## 📚 Notlar

- `os.environ.get(key)`: ortam değişkenini okur; bulunamazsa `None` döner.
- `importlib.util.find_spec(pkg)`: bir paketin yüklü olup olmadığını, onu import etmeden kontrol eder.
- `load_dotenv()`: `.env` dosyasındaki değişkenleri `os.environ`'a yükler; `.env` dosyası bulunamazsa sessizce hiçbir şey yapmaz (bu yüzden `security_check()` ayrıca dosyanın varlığını kontrol eder).
- `getattr(mod, "__version__", "unknown")`: bir modülün versiyon bilgisini, `__version__` özniteliği yoksa hata vermeden okur.

---

<div align="center">
    
### 👩‍💻 Created by Sude Naz Karayıldırım

[![42 Profile](https://img.shields.io/badge/42%20Profile-skarayil-black?style=flat-square&logo=42&logoColor=white)](https://profile.intra.42.fr/users/skarayil)
[![GitHub](https://img.shields.io/badge/GitHub-skarayil-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/skarayil)

**⭐ Eğer bu proje işinize yaradıysa, repo'ya star vermeyi unutmayın!**

</div>
