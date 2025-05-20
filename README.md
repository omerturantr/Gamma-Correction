# 🎛️ Gamma Correction

Bu proje, bir görüntü üzerinde farklı gamma düzeltme (gamma correction) seviyelerini uygulayarak görsel sonuçlarını gösteren basit bir Python uygulamasıdır. Gamma düzeltmesi, görüntülerin parlaklık algısını değiştirmek için kullanılan önemli bir görüntü işleme tekniğidir.

## 🖼️ Örnek Sonuç

Aşağıda, farklı gamma değerleriyle işlenmiş bir meyve görseli yer almakta:

![Gamma Correction Output](Screenshot%202025-05-20%20195156.png)

> Görselde sırasıyla: Orijinal, Gamma 0.3 (karartma), Gamma 1 (değişiklik yok), Gamma 3 (aydınlatma) uygulanmıştır.

---

## 🔧 Kurulum ve Kullanım

### 1. Depoyu Klonlayın

```bash
git clone https://github.com/omerturantr/gamma-correction.git
cd gamma-correction
```

### 2. Gereksinimleri Yükleyin

```bash
pip install opencv-python matplotlib numpy
```

### 3. Uygulamayı Başlatın

```bash
python main.py
```

---

## 🧠 Kodun Açıklaması

`apply_gamma_correction()` fonksiyonu, verilen gamma değerine göre LUT (Look-Up Table) oluşturarak görüntüye gamma düzeltmesi uygular:

```python
def apply_gamma_correction(image, gamma):
    invGamma = 1.0 / gamma
    table = np.array([(i / 255.0) ** invGamma * 255 for i in np.arange(256)]).astype("uint8")
    return cv2.LUT(image, table)
```

- **Gamma < 1**: Görüntüyü karartır.  
- **Gamma = 1**: Görüntü değişmez.  
- **Gamma > 1**: Görüntüyü aydınlatır.

---

## 📁 Dosya Yapısı

```
gamma-correction/
├── fruits.jpg                        # Giriş görüntüsü
├── Screenshot 2025-05-20 195156.png # Çıktı ekran görüntüsü
├── main.py                          # Ana Python betiği
└── README.md
```

---

## 📄 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.

---

## 👤 Geliştirici

**Ömer Turan**  
📧 [omerturantr@gmail.com](mailto:omerturantr@gmail.com)  
🔗 [GitHub Profilim](https://github.com/omerturantr)
