README.md


# 🐶 Dogecoin Fiyat Tahmini (Regression Model)

Bu proje, geçmiş fiyat verilerine göre **Dogecoin'in bir sonraki günkü kapanış fiyatını** tahmin eden bir makine öğrenimi modeli içerir.

---

## 📁 Proje Dosyaları

- `dogecoin_historical.csv` → Ham veri seti
- `train_dogecoin_model.py` → Model eğitim kodları
- `dogecoin_price_model.pkl` → Eğitilmiş model
- `app.py` → Streamlit kullanıcı arayüzü
- `requirements.txt` → Gerekli Python paketleri

---

## 🚀 Kullanım

### 1. Ortamı Kur

```bash
pip install -r requirements.txt

Modeli Eğit
python train_dogecoin_model.py

Uygulamayı Başlat
streamlit run app.py


💡 Kullanıcı Arayüzü
Kullanıcı, açılış fiyatı, en yüksek/düşük değerler, hacim ve piyasa değerini girer. Model bu değerlere göre bir sonraki günün kapanış fiyatını tahmin eder.



📦 Model
Model: RandomForestRegressor

Skor: R² ≈ 0.984, RMSE ≈ 0.0021


🧪 Eğitim Amaçlıdır
Bu proje yalnızca eğitim ve demo amaçlıdır. Gerçek yatırım kararlarında kullanılmamalıdır.


🪪 Lisans
MIT License