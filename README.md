Trader Behavior Analysis Based on Market Sentiment

Project Overview

This project analyzes the relationship between Bitcoin market sentiment and trader performance. The analysis combines historical trading data with the Fear & Greed Index to understand how different market sentiments influence trading outcomes.

The objective is to identify patterns in trader profitability, trading activity, and overall performance during different sentiment conditions such as Fear, Greed, Extreme Fear, and Extreme Greed.

---

Datasets Used

1. Historical Trader Data

Contains detailed trading records including:

- Trade timestamps
- Trade side
- Quantity
- Price
- Closed PnL
- Trading activity information

2. Fear & Greed Index Data

Contains market sentiment information including:

- Timestamp
- Sentiment classification
- Fear & Greed values

---

Methodology

Data Loading

Both datasets were imported using Pandas and inspected for data quality issues.

Data Cleaning

- Missing values were checked and handled.
- Timestamp formats were standardized.
- Unnecessary columns were removed where required.

Data Merging

The datasets were merged using timestamp-based matching to associate each trade with the corresponding market sentiment.

Exploratory Data Analysis (EDA)

Several analyses were performed to understand trader behavior under different sentiment conditions:

- Trade count by sentiment
- Average Closed PnL by sentiment
- Total Closed PnL by sentiment
- Win rate by sentiment
- Trade activity comparison
- Profitability comparison

Visualization

Multiple visualizations were created using Matplotlib and Seaborn to identify patterns and support findings.

---

Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- VS Code

---

Key Analysis Performed

1. Trade Count by Sentiment
2. Average Profit/Loss by Sentiment
3. Total Profit/Loss by Sentiment
4. Win Rate Comparison
5. Trading Activity Analysis
6. PnL Distribution Analysis
7. Market Sentiment Impact Assessment

---

Key Findings

- Market sentiment has a measurable impact on trader behavior.
- Trading activity varies across different sentiment conditions.
- Profitability differs during Fear and Greed periods.
- Certain sentiment categories show stronger trading performance than others.
- Sentiment-based analysis can provide valuable insights into trader decision-making patterns.

---

Conclusion

This project demonstrates how market sentiment can influence trading behavior and profitability. By combining trading records with sentiment indicators, meaningful patterns can be identified that help explain trader performance under varying market conditions.

The analysis highlights the importance of incorporating sentiment indicators into trading and market evaluation frameworks.

---

Repository Structure

Trader-Sentiment-Analysis/
│
├── analysis.ipynb
├── README.md
├── requirements.txt
├── data/
└── images/
