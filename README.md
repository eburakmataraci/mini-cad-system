# Mini CAD System

Python ve Tkinter ile geliştirilmiş, 2D çizim ve 3D render yeteneklerine sahip hafif bir masaüstü CAD uygulaması.

---

## Özellikler

### 2D Çizim Araçları
- **Çizgi** — serbest doğru çizimi
- **Dikdörtgen** — köşeden köşeye çizim
- **Üçgen** — üçgen çokgen oluşturma
- **Daire** — elips / daire çizimi (36 noktalı çokgen yaklaşımı)

### 3D Nesneler
- **Küp** — 6 yüzlü, ışıklandırmalı küp
- **Piramit** — 5 yüzlü piramit
- Nesneler başlangıçta izometrik açıda yerleştirilir; fare sürüklemesiyle boyut ayarlanır
- Tüm 3D yüzler **Painter's Algorithm** ile Z sırasına göre çizilir
- Sağ fare tuşu + sürükle → **küresel 3D kamera rotasyonu**

### Seçim ve Düzenleme
- Nesneleri seçip tutuşlarla **yeniden boyutlandırma** (köşe handles)
- Seçili nesneyi **sürükleyerek taşıma**
- **Z ekseni rotasyonu** (2D ve 3D): ±15° adımlarla
- **3D nesne rotasyonu**: X ve Y eksenleri ayrı ayrı
- **Ölçek**: %20 büyütme / %20 küçültme
- **Katman yönetimi**: Öne getir / Arkaya gönder
- **Kopyala** — seçili nesneyi ofsetli konumda çoğaltır
- **Sil** — seçili nesneyi kaldırır

### Görünüm ve Stil
- Renk seçici (Tkinter `colorchooser`)
- Kenarlık kalınlığı (1 / 2 / 3 / 5 / 8 / 10 px)
- **Dolu / Kenarlık** stili arasında geçiş
- Özelleştirilebilir ızgara (görünür / gizli)
- **Izgaraya yapış (snap)** modu

### Geçmiş ve Dosya
- **Geri Al / İleri Al** — 30 adıma kadar geçmiş
- **Kaydet / Yükle** — tüm çizim `.json` formatında saklanır

---

## Dosya Yapısı

```
.
├── main.py        # Ana uygulama — MiniCADApp sınıfı, UI kurulumu, tüm olay yönetimi
├── config.py      # Renk paleti (COLORS) ve font tanımlamaları (FONTS)
├── math_3d.py     # 3D matematik yardımcıları: normalize, cross/dot product, shade_color
└── ui_utils.py    # Tkinter widget yardımcıları: make_btn, add_hover, sep
```

### Modül Sorumlulukları

| Dosya | Sorumluluk |
|---|---|
| `main.py` | Uygulama durumu, olay döngüsü, çizim ve render mantığı |
| `config.py` | Merkezi renk ve font sabitleri |
| `math_3d.py` | Vektör işlemleri ve yüzey gölgelendirme hesaplamaları |
| `ui_utils.py` | Tekrar kullanılabilir buton / ayırıcı oluşturma fonksiyonları |

---

## Gereksinimler

- Python 3.8+
- Tkinter (Python'un standart kütüphanesiyle gelir; ayrıca kurulum gerekmez)

> **Not:** Bazı Linux dağıtımlarında Tkinter ayrıca kurulabilir:
> ```bash
> sudo apt install python3-tk
> ```

---

## Çalıştırma

```bash
python main.py
```

Uygulama 1450×880 piksel boyutunda açılır.

---

## Klavye Kısayolları

| Kısayol | İşlev |
|---|---|
| `Ctrl+C` | Seçili nesneyi kopyala |
| `Ctrl+Z` | Geri al |
| `Ctrl+Y` | İleri al |
| `Delete` | Seçili nesneyi sil |

---

## Kayıt Formatı

Çizimler JSON olarak kaydedilir. Format:

```json
{
  "2d": [
    {
      "type": "polygon",
      "coords": [100, 100, 200, 100, 200, 200, 100, 200],
      "fill": "#3b82f6",
      "outline": "#3b82f6",
      "width": "2"
    }
  ],
  "3d": [
    {
      "id": "3d_0_1",
      "type": "cube",
      "cx": 400, "cy": 300, "size": 60,
      "rot_x": -0.6155, "rot_y": 0.7854, "rot_z": 0.0,
      "color": "#f97316",
      "style": "fill",
      "width": 2,
      "vertices": [...],
      "faces": [...]
    }
  ]
}
```

---

## Mimari Notlar

- **3D Render:** Her frame'de tüm 3D nesneler sıfırdan yeniden çizilir. Nesne rotasyonu + global kamera rotasyonu zincir matris dönüşümleri ile uygulanır. Yüzey görünürlüğü backface culling (normal Z > 0) ile belirlenir; gölgelendirme diffuse ışık hesabına dayanır.
- **Geçmiş Yönetimi:** Her değiştirici işlemden önce `save_state()` çağrılarak o anki 2D canvas durumu ve 3D nesne listesi `history` yığınına eklenir. Maksimum 30 adım saklanır.
- **Izgara Yapışması:** `get_snapped_coord()` tüm fare koordinatlarını `grid_size` katına yuvarlar.
