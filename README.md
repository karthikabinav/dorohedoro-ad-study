# Dorohedoro Premiere Advertising Study

## Overview
This study analyzes advertising campaigns that launched the day after the Dorohedoro anime premiered.

## Study Parameters
- **Anime:** Dorohedoro
- **Premiere Date:** January 13, 2020
- **Target Analysis Date:** January 14, 2020 (day after premiere)
- **Data Source:** Notion Advertising Database
- **Database ID:** `21b97551-844e-8068-b387-fe7a56b04348`

## Objective
Calculate the average amount spent on advertisements that started on 2020-01-14.

## Methodology
1. Query Notion Advertising database
2. Filter by `StartDate = '2020-01-14'`
3. Extract all `SpentAmount` values
4. Calculate arithmetic mean: Sum(SpentAmount) / Count

## Current Status
⚠️ **Rate Limited** - Notion API is currently rate limiting requests

## Files
- `analysis.py` - Python script for data analysis
- `methodology.md` - Detailed methodology documentation
- `results.json` - Placeholder for results data

## Next Steps
1. Wait for Notion API rate limit reset
2. Execute database query
3. Process results and calculate average
4. Update this repository with findings
