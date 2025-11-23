# 3D Pursuit Simulation  
Bu proje, 3D uzayda hareket eden bir **enemy (düşman)** küresi ile onu takip etmeye çalışan bir **soldier (asker)** küresinin fizik tabanlı hareket simülasyonudur.  
Simülasyon SciPy’nin **solve_ivp** ODE çözücüsü ile asker hareketini hesaplar ve matplotlib 3D animasyon ile gösterir.

---

## 🚀 Özellikler
- 3D uzayda gerçek zamanlı takip animasyonu
- Enemy nesnesi sinüsoidal bir 3D yol izler
- Soldier, enemy pozisyonuna kilitlenir ve ona doğru hızla ilerler
- Her iki nesne de arkalarında **iz (trail)** bırakır
- Asker ve enemy için **ayrı hız** tanımlanabilir
- Tamamen Python ve scientific stack ile yazılmıştır

---

## 📦 Gereksinimler
Aşağıdaki kütüphaneler gereklidir:
numpy
scipy
matplotlib


Kurmak için:

```bash
pip install -r requirements.txt

▶️ Çalıştırma

Aşağıdaki Python komut dosyasını çalıştırın:
python main.py

📁 Proje Yapısı Önerisi
3d_pursuit/
│── main.py
│── requirements.txt
└── README.md

🔧 Parametreler
Main dosyada kolayca değiştirilebilir:
soldier_speed = 1.5  # askerin hızı
enemy_speed   = 1.0  # düşmanın hızı

🎥 Animasyon İçeriği
Kırmızı küre: Enemy
Mavi küre: Soldier
Her iki küre arkasında bir iz (trail) bırakır
Soldier, enemy'nin anlık pozisyonunu takip eder


