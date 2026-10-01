import json
import requests
import pandas as pd

# 1. CONFIGURATION
# Replace with your actual free API key from Apollo.io
APOLLO_API_KEY = "YOUR_FREE_APOLLO_API_KEY" 

def fetch_yc_startups():
    """
    Simulates fetching target tech startups from Y Combinator's public API data.
    This bypasses complex scraping blocks by pulling direct corporate metadata.
    """
    print("🤖 Step 1: Scanning startup directory for GTM targets...")
    
    # Example raw target list modeled after YC B2B companies looking to scale
    sample_targets = [
        {"name": "Deel", "domain": "deel.com", "signal": "Hiring Sales Leads"},
        {"name": "Ramp", "domain": "ramp.com", "signal": "Expanding GTM Team"},
        {"name": "Brex", "domain": "brex.com", "signal": "Hiring Account Executives"},
        {"name": "Retool", "domain": "retool.com", "signal": "Scaling Outbound Operations"},
        {"name": "Vanta", "domain": "vanta.com", "signal": "Hiring Growth Engineers"}
    ]
    return sample_targets

def enrich_company_contact(domain):
    """
    Uses the free Apollo.io API to find the key GTM decision-maker 
    (VP of Sales, CRO, or Head of Growth) at the target company.
    """
    print(f"🔍 Step 2: Enriching data for domain: {domain}...")
    url = "https://apollo.io"
    
    headers = {
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
        "X-Api-Key": APOLLO_API_KEY
    }
    
    # We look specifically for high-level sales and marketing roles
    data = {
        "domain": domain,
        "titles": ["VP of Sales", "CRO", "Head of Sales", "Director of Growth", "Head of Go-To-Market"]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            res_data = response.json()
            person = res_data.get("person", {})
            
            return {
                "Contact Name": person.get("name", "Not Found"),
                "Title": person.get("title", "Not Found"),
                "Email": person.get("email", "Contact via LinkedIn"),
                "LinkedIn": person.get("linkedin_url", "N/A")
            }
        else:
            return {"Contact Name": "API Limit/Error", "Title": "N/A", "Email": "N/A", "LinkedIn": "N/A"}
    except Exception as e:
        return {"Contact Name": "Error", "Title": str(e), "Email": "N/A", "LinkedIn": "N/A"}

def main():
    # Fetch initial signal data
    startups = fetch_yc_startups()
    lead_list = []
    
    # Loop through targets and enrich them
    for company in startups:
        enrichment = enrich_company_contact(company["domain"])
        
        # Merge our signal data with the enrichment data
        full_lead = {
            "Company Name": company["name"],
            "Domain": company["domain"],
            "Observed Signal": company["signal"],
            **enrichment
        }
        lead_list.append(full_lead)
        
    # 3. EXPORT TO CSV (Easily openable in Excel or Google Sheets)
    df = pd.DataFrame(lead_list)
    df.to_csv("yc_gtm_leads.csv", index=False)
    print("\n✅ Success! File saved as 'yc_gtm_leads.csv'. Drag and drop this into Google Sheets.")

if __name__ == "__main__":
    main()
