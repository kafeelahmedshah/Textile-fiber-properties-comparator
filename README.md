# Textile Fiber Properties Comparator

**Roll No:** 25TE009  
**Department:** Textile Engineering  
**Framework:** Python + Streamlit

## Project overview

A Streamlit application that helps textile students compare cotton, polyester, wool, silk, and nylon. It displays moisture regain, approximate tenacity ranges, and a qualitative breathability guide score through comparison tables and interactive charts.

## Features

- Select two or more fibers for comparison
- Side-by-side property comparison table
- Moisture regain chart
- Approximate tenacity / strength range chart
- Qualitative breathability guide chart
- Quick comparison insights
- Individual fiber detail page
- Fiber origin, absorbency, heat behavior, advantages, limitations, and common uses
- Download comparison data as CSV
- Data limitations and responsible-use note

## Fibers included

1. Cotton
2. Polyester
3. Wool
4. Silk
5. Nylon

## Project files

- `app.py` — Main Streamlit application
- `requirements.txt` — Required Python packages
- `README.md` — Project documentation

## Run locally

1. Install Python 3.9 or newer.
2. Open a terminal in this project folder.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
streamlit run app.py
```

The app will open in your browser. The local address is usually `http://localhost:8501`.

## Deploy on Streamlit Community Cloud

1. Create a GitHub repository.
2. Upload `app.py`, `requirements.txt`, and `README.md`.
3. Sign in to Streamlit Community Cloud with GitHub.
4. Create a new app and select the repository and `app.py`.
5. Deploy.

## Data and limitations

The property values are approximate educational references. Actual moisture regain and tenacity depend on fiber grade, conditioning, processing, and test method. Breathability is a qualitative 1–5 teaching score, not a standardized laboratory measurement. Fabric construction and finishing also affect comfort and breathability. Consult recognized textile references or laboratory test reports for exact specifications.
