# 📊 CORD-19 Data Explorer (Sample Project)

This project is a simplified analysis of the **CORD-19 research dataset** using Python and Streamlit.  
It demonstrates the basic **data science workflow**: loading data, cleaning, analyzing, visualizing, and presenting results in an interactive web application.

---

## 🚀 Project Structure
- `metadata.csv` → Sample dataset (COVID-19 research papers metadata)
- `app.py` → Streamlit application
- `analysis.py` (optional) → Script/Jupyter notebook for exploratory analysis

---

## 🛠 Tools Used
- **Python 3.7+**
- [pandas](https://pandas.pydata.org/) → data loading & manipulation  
- [matplotlib](https://matplotlib.org/) & [seaborn](https://seaborn.pydata.org/) → visualizations  
- [streamlit](https://streamlit.io/) → interactive web app  

---

## 📂 Workflow
1. **Data Loading**
   - Load `metadata.csv` into a Pandas DataFrame
   - Convert `publish_time` into datetime
   - Extract publication year

2. **Data Cleaning**
   - Handle missing values
   - Create derived columns like `year`

3. **Data Analysis**
   - Count papers per year
   - Identify top publishing journals
   - Show publications by source
   - Preview a sample of the data

4. **Visualization**
   - Publications over time (bar chart)
   - Top journals (horizontal bar chart)
   - Publications by source (pie chart)

5. **Streamlit App**
   - Sidebar filters for year and journal
   - Interactive visualizations
   - Data preview

---

## ▶️ How to Run the Project

### 1. Clone the repo and navigate into it:
```bash
https://github.com/Nice254-art/python_week8_assignment/edit/main
cd Frameworks_Assignment
