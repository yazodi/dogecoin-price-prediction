
# 🐶 Dogecoin Price Prediction using Python

This project focuses on analyzing historical Dogecoin (DOGE) price data and applying machine learning regression techniques to forecast future prices.

## 📁 Contents

- Dataset: `dogecoin_historical.csv`
- Tools: Python, Jupyter Notebook
- Libraries: `pandas`, `matplotlib`, `seaborn`, `AutoTS`

## ⚙️ Technologies Used

- Python 3.x
- Jupyter Notebook
- AutoTS (Automated Time Series Forecasting)

## 📊 Workflow

1. **Data Loading**
   - DOGE price data is loaded from a `.csv` file using `pandas`.

2. **Data Cleaning**
   - Missing values are handled.
   - Column names are stripped of any extra spaces.

3. **Visualization**
   - Dogecoin close prices are visualized using `matplotlib` and `seaborn`.

4. **Model Training**
   - `AutoTS` is used for automatic time series regression modeling.
   - The model selects the best algorithm to predict future DOGE prices.

## 🧠 Algorithms Used

AutoTS automatically evaluates multiple models such as:
- Linear Regression
- Decision Tree Regression
- ARIMA
- Prophet
- Other time series models

## 📦 Requirements

```bash
pip install pandas matplotlib seaborn autots
```

## 📈 Sample Visualization

```python
plt.plot(data["close"])
plt.title("DOGE/USD Daily Close Price")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
```

## 📌 Notes

- CSV file uses semicolon (;) as a separator.
- Column names were cleaned with `.str.strip()` to avoid `KeyError`.

## ✍️ Contribution

Feel free to fork the project, suggest improvements, or add new features like LSTM or technical indicators.

## 📜 License

MIT License

