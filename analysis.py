#!/usr/bin/env python3
"""
Dorohedoro Advertising Study Analysis Script
Analyzes campaigns launched on 2020-01-14 (day after Dorohedoro premiere)
"""

import json
from datetime import datetime
from statistics import mean

# Study parameters
DOROHEDORO_PREMIERE = datetime(2020, 1, 13)
TARGET_DATE = datetime(2020, 1, 14)
DATABASE_ID = "21b97551-844e-8068-b387-fe7a56b04348"

def analyze_campaigns(campaigns_data):
    """
    Analyze advertising campaigns and calculate average spend
    
    Args:
        campaigns_data: List of campaign dictionaries with SpentAmount field
    
    Returns:
        dict: Analysis results with total, count, and average
    """
    spent_amounts = [c['SpentAmount'] for c in campaigns_data if 'SpentAmount' in c]
    
    if not spent_amounts:
        return {"error": "No SpentAmount data found"}
    
    return {
        "total_campaigns": len(spent_amounts),
        "total_spent": sum(spent_amounts),
        "average_spent": mean(spent_amounts),
        "min_spent": min(spent_amounts),
        "max_spent": max(spent_amounts)
    }

def main():
    print("=" * 80)
    print("DOROHEDORO ADVERTISING STUDY")
    print("=" * 80)
    print()
    
    print(f"Anime: Dorohedoro")
    print(f"Premiere Date: {DOROHEDORO_PREMIERE.strftime('%Y-%m-%d')}")
    print(f"Analysis Date: {TARGET_DATE.strftime('%Y-%m-%d')} (day after premiere)")
    print()
    
    print("Database Query Specification:")
    query = {
        "database_id": DATABASE_ID,
        "filter": {
            "property": "StartDate",
            "date": {"equals": TARGET_DATE.strftime('%Y-%m-%d')}
        },
        "page_size": 100
    }
    print(json.dumps(query, indent=2))
    print()
    
    print("Status: Rate limited by Notion API")
    print("Unable to retrieve actual data at this time.")
    print()
    
    # Sample data structure for when data is retrieved
    sample_campaigns = [
        {"CampaignID": "CAMP-001", "SpentAmount": 2500.00},
        {"CampaignID": "CAMP-002", "SpentAmount": 1800.50},
        {"CampaignID": "CAMP-003", "SpentAmount": 3200.75}
    ]
    
    print("Sample Analysis (using mock data):")
    results = analyze_campaigns(sample_campaigns)
    for key, value in results.items():
        if isinstance(value, float):
            print(f"  {key}: ${value:,.2f}")
        else:
            print(f"  {key}: {value}")

if __name__ == "__main__":
    main()
