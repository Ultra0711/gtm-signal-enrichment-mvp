# GTM Signal Enrichment MVP 🚀

A lightweight, automated Go-To-Market (GTM) engineering script designed to replace manual outbound prospecting. This tool simulates tracking high-intent hiring signals from startup directories, programmatically enriches target accounts using the Apollo.io API, and outputs structured, high-value leads for sales teams.

Built as a practical case study to demonstrate modern, low-overhead outbound infrastructure automation for fast-scaling B2B startups.

## ✨ Key Features
- **Intent-Driven Discovery:** Identifies accounts displaying clear growth indicators (e.g., active hiring signals for GTM/Sales positions).
- **Targeted Persona Matching:** Programmatically isolates key decision-makers (CROs, VPs of Sales, Heads of Growth) rather than pulling generic company contacts.
- **Data Pipeline Hygiene:** Normalizes raw web/API data and maps it into a clean, spreadsheet-ready schema (`Company Name`, `Domain`, `Observed Signal`, `Contact Name`, `Title`, `Email`, `LinkedIn`).

## 🛠️ Tech Stack & Tools
- **Language:** Python 3
- **Data Manipulation:** Pandas
- **APIs & Networking:** Requests (Integrating Apollo.io REST API)
- **Output Data Format:** CSV / Google Sheets

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python installed, then install the required dependencies:
```bash
pip install requests pandas
```

### 2. API Setup
1. Sign up for a free developer account at [Apollo.io](https://apollo.io).
2. Generate your API key from the developer settings.
3. Open `gtm_lead_gen.py` and replace `YOUR_FREE_APOLLO_API_KEY` with your actual key.

### 3. Run the Script
Execute the script via your terminal:
```bash
python gtm_lead_gen.py
```
Upon successful execution, the script will output a `yc_gtm_leads.csv` file in your root directory, ready to be dropped straight into HubSpot, Salesforce, or Google Sheets.

## 📊 Business Impact
Manual list building wastes hours of a Sales Development Representative's (SDR) day. By automating the data retrieval and enrichment layers:
1. **Time-to-Outbound decreases** from hours to seconds.
2. **Data accuracy improves** by mapping titles explicitly via API logic.
3. **Conversion rates increase** by focusing exclusively on accounts with an active, verified buying signal.
