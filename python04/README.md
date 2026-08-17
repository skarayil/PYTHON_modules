# 📜 Python Module 04 - Kadim Parşömenler (Dosya İşlemleri)

<div align="center">

![42 School](https://img.shields.io/badge/School-42-black?style=for-the-badge&logo=42)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Module](https://img.shields.io/badge/Module-python04-blue?style=for-the-badge)

**"Kadim Parşömenler" temasıyla dosya okuma, yazma ve güvenli dosya erişimi (File I/O)**

</div>

---

## 🎯 Modülün Amacı

Programlar çalıştığı sürece verileri RAM'de tutar; program kapandığında bu veri kaybolur. Bu modül, verinin diske kalıcı olarak nasıl yazılıp okunacağını (File I/O) ve bu işlemler sırasında oluşabilecek hataların (dosya bulunamadı, izin yok...) nasıl güvenle yönetileceğini öğretir.

### 🎓 Ana Öğrenme Hedefleri

#### 📖 Dosya Okuma
- `open(filename, "r")` ile bir dosyayı okuma modunda açmak
- `.read()` ile dosyanın tüm içeriğini tek seferde almak

#### ✍️ Dosya Yazma
- `open(filename, "w")` ile yeni bir dosya oluşturmak/üzerine yazmak
- `.write()` ile veriyi diske kaydetmek

#### 🔄 Veri Dönüştürme
- Okunan veriyi satır satır işleyip (`.splitlines()`) her satıra ek bir işaret (`#`) ekleyerek yeniden birleştirmek (`.join()`)

#### 🛡️ Hata Yönetimi ve Güvenli Erişim
- Dosya işlemlerini `try/except` ile sarmalayıp `FileNotFoundError`, `PermissionError` gibi durumlarda programın çökmesini engellemek
- Hataları `sys.stderr`'a yazarak normal çıktıdan (`stdout`) ayırmak
- Bir işlemin başarılı olup olmadığını `(bool, mesaj)` şeklinde bir `tuple` olarak döndürüp çağıran tarafın karar vermesini sağlamak

---

## ✨ Egzersiz Detayları

### 📋 Egzersiz Tablosu

| Egzersiz | Dosya | Konu | Temel Kavram |
|----------|-------|------|---------------|
| **ex0** | `ft_ancient_text.py` | Dosya okuma | `open(..., "r")`, `.read()` |
| **ex1** | `ft_archive_creation.py` | Okuma + dönüştürme + yazma | `.splitlines()`, `.join()`, `open(..., "w")` |
| **ex2** | `ft_stream_management.py` | Standart akışlar | `sys.stderr`, `sys.stdin.readline()` |
| **ex3** | `ft_vault_security.py` | Güvenli erişim | `try/except` içinde `(bool, str)` dönüşü |

---

### **ex0 — Dosya Okuma (`ft_ancient_text.py`)**

```python
f = open(filename, "r")
data: str = f.read()
print(data, end="")
f.close()
```

Komut satırından verilen dosya adı açılır, içeriği okunup ekrana basılır. Dosya bulunamazsa veya açılamazsa hata `try/except` ile yakalanıp ekrana basılır; program çökmez.

---

### **ex1 — Okuma + Dönüştürme + Yazma (`ft_archive_creation.py`)**

Okunan içerik satır satır ayrılır, her satırın sonuna `#` eklenir ve tekrar tek bir metne birleştirilir:

```python
def transform(data: str) -> str:
    lines: list[str] = data.splitlines()
    transformed: list[str] = [line + "#" for line in lines]
    return "\n".join(transformed) + "\n"
```

Kullanıcıdan yeni bir dosya adı istenir (`input()`); boş bırakılırsa kaydetme işlemi atlanır, aksi halde dönüştürülmüş veri `"w"` modunda yeni dosyaya yazılır.

---

### **ex2 — Standart Akışlar (`ft_stream_management.py`)**

Bir önceki egzersizin aynısını yapar, ancak iki önemli farkla:

```python
print(f"[STDERR] Error opening file '{filename}': {e}", file=sys.stderr)
...
new_filename: str = sys.stdin.readline().rstrip("\n")
```

Hatalar `stdout` yerine `sys.stderr`'a yönlendirilir (böylece normal çıktıdan ayrıştırılabilir), ve kullanıcı girdisi `input()` yerine doğrudan `sys.stdin.readline()` ile okunur.

---

### **ex3 — Güvenli Erişim (`ft_vault_security.py`)**

```python
def secure_archive(filename, action="read", content="") -> tuple[bool, str]:
    try:
        with open(filename, "r") as f:
            data = f.read()
        return (True, data)
    except Exception as e:
        return (False, str(e))
```

Artık hata mesajı doğrudan ekrana basılmaz; fonksiyon `(başarılı mı, sonuç/hata mesajı)` şeklinde bir `tuple` döndürür ve **`with` bloğu** kullanılarak dosyanın işlem bitince otomatik kapanması garanti edilir. Çağıran taraf bu tuple'a bakarak nasıl davranacağına kendisi karar verir. Var olmayan bir dosyaya (`/not/existing/file`) ve izinsiz bir dosyaya (`/etc/master.passwd`) erişim denemeleri, fonksiyonun hem `FileNotFoundError` hem `PermissionError` durumlarını `Exception` üzerinden yakaladığını gösterir.

---

## 📁 Dosya Yapısı

```
python04/
├── ex0/
│   └── ft_ancient_text.py        # Temel dosya okuma
├── ex1/
│   └── ft_archive_creation.py    # Okuma + dönüştürme + yazma
├── ex2/
│   └── ft_stream_management.py   # stderr ve stdin.readline
└── ex3/
    └── ft_vault_security.py      # with + (bool, str) dönüşü
```

---

## 💻 Kullanım

```bash
python3 ex0/ft_ancient_text.py <dosya>
python3 ex1/ft_archive_creation.py <dosya>
python3 ex2/ft_stream_management.py <dosya>
python3 ex3/ft_vault_security.py
```

`ex0`, `ex1` ve `ex2` bir dosya yolu argümanı bekler (`Usage: ... <file>` mesajıyla uyarır); `ex3` kendi test dosya adlarını (`ancient_fragment.txt`, `vault_copy.txt`) kod içinde kullanır.

---

## 📚 Notlar

- `open()` ile açılan bir dosya mutlaka `close()` edilmeli veya `with open(...) as f:` bloğu kullanılmalıdır; aksi halde dosya "meşgul" kalabilir.
- `except Exception as e:` genel bir yakalamadır; `ex3`'te olduğu gibi hem `FileNotFoundError` hem `PermissionError` gibi farklı hataları tek seferde kapsar.
- `ex2`'deki `sys.stderr` kullanımı, hata çıktısını normal programın çıktısından (`stdout`) ayırmak isteyen komut satırı araçlarında yaygın bir pratiktir.

---

### 👩‍💻 Created by Sude Naz Karayıldırım
