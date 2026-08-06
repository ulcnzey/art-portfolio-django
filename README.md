# 🎨 StajWeb — Sanat & Portfolyo Platformu

> Sanatçıların işlerini sergilemesi için tasarlanmış, içerik yönetimi
> tamamen panel üzerinden yapılabilen dinamik bir portfolyo web sitesi.

Statik HTML sayfalarla uğraşmadan; yeni bir eser, galeri görseli veya
hizmet eklemek için tek yapılması gereken yönetim panelinden formu
doldurmak. Site kendini günceller.

---

## ✨ Neler Yapabiliyor

| Modül | Açıklama |
|---|---|
| **Portfolio** | Kategorili eser koleksiyonu, görsel yükleme, tarih bazlı sıralama |
| **Extra Gallery** | Ana portfolyo dışındaki çalışmalar için ayrı galeri alanı |
| **Services** | Sunulan hizmetler — özelleştirilebilir ikon desteğiyle |
| **Admin Panel** | Arama, filtreleme ve kategori bazlı yönetim |

Tüm içerikler veritabanından geliyor; kod dosyalarına dokunmadan
yönetilebiliyor.

---

## 🛠 Teknoloji Seçimleri

**Python 3.x · Django 5.2 · SQLite · Bootstrap 5 · Bootstrap Icons**

Neden Django? İçerik yönetimi ihtiyacı olan bir projede Django Admin,
sıfırdan CRUD arayüzü yazma maliyetini ortadan kaldırıyor. Model
tanımını yaptığın anda çalışan bir yönetim paneline sahip oluyorsun.

Neden SQLite? Tek yazarlı, düşük eşzamanlılıklı bir portfolyo sitesi
için yeterli. Yük arttığında `DATABASES` ayarını değiştirmek dışında
kod değişikliği gerektirmeden PostgreSQL'e geçilebilecek şekilde
kurgulandı.

---

## 📐 Mimari

```
stajweb/
├── stajweb/          # Proje konfigürasyonu (settings, root urls, wsgi)
├── blog/
│   ├── models.py     # Portfolio, ExtraGallery, Service
│   ├── views.py      # Ana sayfa view'ı
│   ├── admin.py      # Admin panel özelleştirmeleri
│   ├── templates/    # Blade değil — Django Template Language
│   └── static/       # CSS, JS, sabit görseller
└── media/            # Kullanıcı tarafından yüklenen görseller
```

**Django MVT deseni:** Model veriyi, View iş mantığını, Template sunumu
üstlenir. Bu ayrım sayesinde tasarımı değiştirmek için Python koduna,
veri yapısını değiştirmek için HTML'e dokunmak gerekmiyor.

**Static vs Media ayrımı:** `static/` geliştiricinin yazdığı sabit
dosyalar (CSS, JS), `media/` kullanıcının yüklediği dinamik dosyalar
(eser görselleri). Farklı yaşam döngüleri olduğu için farklı servis
stratejileri gerektirirler.

---

## 🔐 Konfigürasyon Yönetimi

Hassas değerler (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`) koddan
ayrılarak ortam değişkenlerine taşındı. Depoda yalnızca
`.env.example` şablonu bulunur; gerçek değerler versiyon kontrolüne
girmez.

Bu, **12-Factor App** metodolojisinin *Config* prensibi: aynı kod
tabanı, ortama göre değişen konfigürasyonla farklı ortamlarda
çalışabilir.

---

## 🚀 Kurulum

```bash
git clone https://github.com/KULLANICI_ADIN/stajweb.git
cd stajweb

python -m venv venv
venv\Scripts\activate          # macOS/Linux: source venv/bin/activate

pip install -r requirements.txt

cp .env.example .env           # SECRET_KEY değerini doldurun

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Site: `http://127.0.0.1:8000/` · Panel: `http://127.0.0.1:8000/admin/`

**Yeni SECRET_KEY üretmek için:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 📸 Ekran Görüntüleri

| Ana Sayfa | Yönetim Paneli |
|---|---|
| ![Ana Sayfa](docs/screenshots/home.png) | ![Panel](docs/screenshots/admin.png) |

---

## 🧠 Geliştirme Sürecinde Öğrendiklerim

- **ImageField ve media yönetimi:** Yüklenen dosyaların nerede
  saklandığı, `MEDIA_ROOT` / `MEDIA_URL` ayrımı ve geliştirme
  ortamında servis edilmesi.
- **URL yapılandırma hiyerarşisi:** Media route'unun app değil proje
  seviyesinde ve yalnızca `DEBUG` modunda tanımlanması gerektiği —
  production'da bu işi web sunucusu üstlenir.
- **Admin özelleştirme:** `list_display`, `list_filter` ve
  `search_fields` ile yönetim panelini gerçekten kullanılabilir hale
  getirmek.
- **Secret yönetimi:** Credential'ların koda gömülmesinin neden bir
  güvenlik açığı olduğu ve ortam değişkeni yaklaşımının nasıl
  çözdüğü.

---

## 🗺 Yol Haritası

- [ ] Eser detay sayfası (`/portfolio/<slug>/`)
- [ ] Kategori bazlı filtreleme
- [ ] Görsel optimizasyonu (thumbnail üretimi)
- [ ] PostgreSQL'e geçiş ve production deploy

---

## 📄 Lisans

MIT