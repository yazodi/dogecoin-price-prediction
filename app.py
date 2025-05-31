import streamlit as st
import joblib
import numpy as np

# Modeli yükle
model = joblib.load("dogecoin_price_model.pkl")

st.title("🐶 Dogecoin Fiyat Tahmini")
st.markdown("Geçmiş gün fiyatlarına göre bir sonraki kapanış fiyatını tahmin eder.")

# Kullanıcı girişi
open_price = st.number_input("Açılış Fiyatı (open)", value=0.22)
high_price = st.number_input("En Yüksek Fiyat (high)", value=0.23)
low_price = st.number_input("En Düşük Fiyat (low)", value=0.21)
volume = st.number_input("Hacim (volume)", value=1.2e9, format="%.2e")
market_cap = st.number_input("Piyasa Değeri (marketCap)", value=3.3e10, format="%.2e")

# Tahmin
if st.button("Tahmin Et"):
    features = np.array([[open_price, high_price, low_price, volume, market_cap]])
    prediction = model.predict(features)[0]
    st.success(f"📈 Tahmin Edilen Kapanış Fiyatı: {prediction:.4f} $")
