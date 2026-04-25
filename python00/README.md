# Python_Module_00 

## ⚙️ Python Nasıl Çalışır?
Python kodu yazıldığından itibaren makinenin anlayacağı hale gelene kadar şu aşamalardan geçer:

* **Python dosyası (.py):** Bizim yazdığımız ham kod.
* **Bytecode (.pyc):** Kodun çevrildiği ara format.
* **Python Virtual Machine (PVM):** Kodun okunduğu ve anlaşıldığı yer.
* **Bilgisayar:** İşlemi çalıştırır.

---

## 📂 Egzersiz Detayları

### **ex0 / Fonksiyon Tanımlama**
* **`def`**: Fonksiyonu oluşturmamızı sağlar.
* **`:` (İki Nokta)**: Fonksiyonun içine yazılacakları dahil eder. Python'da süslü parantez `{}` yerine tüm kodlar bu yapının altına, yani fonksiyonun "scope"u içine yazılır.

---

### **ex1 / Terminal İşlemleri**
* **`input`**: Terminal üzerinden kullanıcıdan bir değer almak için kullanılır.
* **`print`**: Klasik yazdırma komutudur. Örneğin; terminalden gelen `garden name` bilgisini ekrana yazdırmak için kullanılır.

---

### **ex2 / Veri Türü Belirleme ve Alan Hesabı**
* **`int`**: `input` ile gelen veriler varsayılan olarak metindir. Önüne `int` yazarak bu değerin sayısal bir değer olduğunu belirtiriz.
* **İşlem**: Bu egzersizde alınan en ve boy değerleri çarpılarak alan hesaplaması yapılır.

---

### **ex3 / Toplama İşlemi**
* `ex2` ile benzer mantıktadır. Tek fark, çarpma yerine toplam gün sayısını bulmak için toplama işlemi yapılmasıdır.

---

### **ex4 & ex5 / Koşul Yapıları (If-Else)**
* Burada `if` ve `else` yapıları öğrenilir. Terminalden gönderilen sayının hangi koşula (şarta) uyacağına karar verilir ve uygun çıktı `print` ile yazdırılır.

---

### **ex6 / Döngüler (Iterative & Recursive)**

Bu bölümde bir işlemi birden çok kez yaptırmanın iki farklı yolunu öğreniyoruz:

**1. Iterative (Döngüsel) Yöntem:**
* **`range`**: Sayı aralığı oluşturur. `(1, 10)` dersen 1 ile 10 arasını alır. Eğer `(1, 10, 2)` dersen, sondaki 3. sayı artış miktarıdır; yani 1, 3, 5... şeklinde 2'şer atlayarak gider.
* **`for i in range(1, days + 1)`**: `range` içindeki sayılar üzerinde sırayla dolaşmamızı sağlar. `i` değişkeni her dönüşte sırayla 1, 2, 3... değerlerini alır.
* **`f-string` (f"")**: `print(f"Day {i}")` satırında olduğu gibi, metnin içine değişkeni direkt yerleştirmemizi sağlar. `{i}` içindeki değer neyse ekrana o yazılır.

**2. Recursive (Özyinelemeli) Yöntem:**
* **`ft_count_harvest_recursive`**: Burada fonksiyon kendi kendini tekrar çağırır. 
* **Durdurma Koşulu**: `if day > days` olduğunda işlem biter ve "Harvest time!" yazdırılır. Bu çok önemlidir, yoksa fonksiyon sonsuza kadar çalışır.
* **Mantık**: Eğer gün dolmadıysa gün adını yazdırır ve `helper(day + 1)` diyerek bir sonraki gün için kendisini tekrar çalıştırır.

---

### **ex7 / Tip Belirtme ve Formatlama**

Bu bölümde kodun daha profesyonel ve hatasız yazılmasını sağlayan kuralları öğreniyoruz:

* **Type Hint (Tip Belirtme)**: `seed_type: str`, `quantity: int` gibi ifadelerle hangi değişkenin ne tür veri (metin mi, sayı mı) alacağını baştan söyleriz. Bu, hataları önceden yakalamayı sağlar.
* **`-> None`**: Bu fonksiyonun dışarıya bir sonuç (değer) döndürmeyeceğini, sadece içindeki işi yapacağını belirtir.
* **`.capitalize()`**: Kullanıcı ne yazarsa yazsın (örn: "tomato"), ilk harfi büyütüp ("Tomato") veriyi standart hale getirir.
* **Koşul Kontrolü**: `if unit == "packets":` satırı ile sadece birim "packets" ise işlem yapılmasını sağlar