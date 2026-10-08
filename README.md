# IBM Applied Data Science Capstone: SpaceX Falcon 9 Landing Prediction

**Author:** Dhruv Khokhriya  
**Specialization:** IBM Data Science Professional Certificate  
**Repository:** [https://github.com/khokhriya/IBM-Applied-Data-Science-Capstone](https://github.com/khokhriya/IBM-Applied-Data-Science-Capstone)  
**Deliverable PDF Report:** [`Data Science Capstone Project Report.pdf`](Data%20Science%20Capstone%20Project%20Report.pdf)  

---

## 🚀 Project Overview

Commercial aerospace has undergone a paradigm shift driven by SpaceX's ability to reuse orbital-class rocket boosters. While conventional expendable launches cost upwards of **~$165 million**, SpaceX advertises Falcon 9 launches at approximately **~$62 million**, primarily due to the recovery and reuse of the first-stage booster.

The primary objective of this capstone is to **predict whether the Falcon 9 first stage will land successfully**, utilizing public launch records, geospatial features, orbital inclinations, and machine learning models. Accurately predicting booster recovery enables commercial launch clients and competitors to estimate launch costs, price competitive bids, and forecast mission risk.

---

## 📁 Repository Deliverables Inventory

| Deliverable | File Name | Description | Direct Link |
| :--- | :--- | :--- | :--- |
| **SpaceX API Ingestion** | `jupyter-labs-eda-datacollection-spacex-api.ipynb` | Extracts launch logs via SpaceX REST API v4, hydrating rocket and payload entities | [Open Notebook](jupyter-labs-eda-datacollection-spacex-api.ipynb) |
| **Web Scraping** | `jupyter-labs-webscraping.ipynb` | Scrapes Falcon 9 launch logs from Wikipedia using BeautifulSoup4 | [Open Notebook](jupyter-labs-webscraping.ipynb) |
| **Data Wrangling** | `labs-jupyter-spacex-Data-wrangling.ipynb` | Median imputation, target binary encoding, and 83 one-hot features | [Open Notebook](labs-jupyter-spacex-Data-wrangling.ipynb) |
| **EDA Visualizations** | `jupyter-labs-eda-dataviz.ipynb` | 6 Matplotlib/Seaborn charts analyzing flight number, payload mass, and orbits | [Open Notebook](jupyter-labs-eda-dataviz.ipynb) |
| **EDA with SQL** | `jupyter-labs-eda-sql-coursera_sqllite.ipynb` | 10 SQLite queries executed on SPACEXTBL database | [Open Notebook](jupyter-labs-eda-sql-coursera_sqllite.ipynb) |
| **Folium Map** | `lab_jupyter_launch_site_location.ipynb` | Geospatial maps with MarkerClusters and proximity distance measurements | [Open Notebook](lab_jupyter_launch_site_location.ipynb) |
| **Plotly Dash App** | `spacex_dash_app.py` | Interactive dashboard web application with dropdowns & payload range slider | [Open Script](spacex_dash_app.py) |
| **Machine Learning** | `SpaceX_Machine_Learning_Prediction_Part_5.ipynb` | Benchmarking 4 classifiers (SVM, Decision Tree, Logistic Regression, KNN) | [Open Notebook](SpaceX_Machine_Learning_Prediction_Part_5.ipynb) |
| **Presentation Report (PDF)** | `Data Science Capstone Project Report.pdf` | Final 47-slide executive PDF presentation | [Open PDF](Data%20Science%20Capstone%20Project%20Report.pdf) |
| **Presentation Slides (PPTX)**| `Data_Science_Capstone_Project_Report.pptx` | Editable PowerPoint deck | [Open PPTX](Data_Science_Capstone_Project_Report.pptx) |
| **Master Dataset** | `spacex_data.csv` | 90 Falcon 9 missions with 83 engineered attributes | [Open CSV](spacex_data.csv) |

---

## 📊 Key Findings & Results

1. **Overall Recovery Success Rate:** **77.8%** across 90 historical Falcon 9 missions, showing a steep learning curve from 0% (2010–2012) to >90% (2018–2020).
2. **Top Launch Complex:** **KSC LC-39A** achieved the highest landing success ratio (**88.0%**), benefiting from optimized infrastructure and eastward orbital trajectories.
3. **Payload Mass Envelope:** Payloads in the **2,000 kg – 6,000 kg** range demonstrate peak landing recovery odds. Very heavy payloads (>8,000 kg) reduce propellant margins.
4. **Champion Predictive Model:** **Support Vector Machine (SVM)** achieved **94.4% test accuracy** (with **100% recall** and **93.3% precision**).
5. **Business Recommendation:** The SVM classifier provides a data-driven framework for commercial launch pricing, allowing commercial clients to bid competitively on reusable flight opportunities.

---

## 🛠️ Tech Stack & Requirements

- **Python:** 3.11+
- **Data Manipulation:** `pandas`, `numpy`
- **Visualization:** `matplotlib`, `seaborn`, `folium`, `plotly`, `dash`
- **Machine Learning:** `scikit-learn`
- **Database:** `sqlite3`
- **Web Extraction:** `requests`, `beautifulsoup4`

To install dependencies:
```bash
pip install pandas numpy matplotlib seaborn folium plotly dash scikit-learn requests beautifulsoup4
```

---

## 👤 Author
**Dhruv Khokhriya**  
IBM Applied Data Science Capstone  
