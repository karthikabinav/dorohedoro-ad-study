# Methodology: Dorohedoro Advertising Study

## Data Source
- **Platform:** Notion
- **Database:** Advertising
- **Database ID:** `21b97551-844e-8068-b387-fe7a56b04348`

## Database Schema
The Advertising database contains the following relevant fields:
- **CampaignID** (title): Unique identifier for each campaign
- **StartDate** (date): Campaign start date
- **EndDate** (date): Campaign end date
- **SpentAmount** (number): Total amount spent on the campaign
- **AdType** (select): Type of advertisement (Video, Social Media, Banner, Search Engine)
- **Impressions** (number): Number of impressions delivered
- **Conversions** (number): Number of conversions
- **ROI** (number): Return on investment

## Query Process

### Step 1: Identify Target Date
- **Dorohedoro Premiere:** January 13, 2020
- **Analysis Date:** January 14, 2020 (day after premiere)

### Step 2: Filter Database
```json
{
  "database_id": "21b97551-844e-8068-b387-fe7a56b04348",
  "filter": {
    "property": "StartDate",
    "date": {"equals": "2020-01-14"}
  },
  "page_size": 100
}
```

### Step 3: Extract Data
For each matching record, extract the `SpentAmount` field value.

### Step 4: Calculate Average
```python
average = sum(SpentAmount) / count(SpentAmount)
```

## Expected Output
- Total number of campaigns started on 2020-01-14
- Total amount spent across all campaigns
- Average amount spent per campaign
- Statistical summary (min, max, median, standard deviation)

## Validation
- Verify date format compliance with Notion API
- Confirm SpentAmount field is populated for all records
- Check for outliers or data anomalies

## Limitations
- Rate limiting by Notion API may require multiple attempts
- Data accuracy depends on proper campaign logging
- External factors affecting ad spend not captured
