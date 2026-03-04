# Statistical Analysis Plan

## Data Description
- **Population:** All advertising campaigns in Notion database
- **Sample:** Campaigns with StartDate = 2020-01-14
- **Variable of Interest:** SpentAmount (continuous numerical variable)
- **Sample Size:** To be determined after data retrieval

## Descriptive Statistics
For the SpentAmount variable, we will calculate:
- Mean (average)
- Median
- Mode
- Standard deviation
- Variance
- Minimum
- Maximum
- Range
- Quartiles (Q1, Q2, Q3)
- Interquartile range (IQR)

## Formulas
- **Mean:** μ = (Σ xᵢ) / n
- **Standard Deviation:** σ = √[Σ (xᵢ - μ)² / (n - 1)]
- **Median:** Middle value when data is sorted
- **Mode:** Most frequently occurring value

## Data Visualization
Planned visualizations:
1. Histogram of SpentAmount distribution
2. Box plot to identify outliers
3. Time series (if multiple dates are analyzed)

## Hypotheses
- H₀: Average SpentAmount = $0 (null hypothesis)
- H₁: Average SpentAmount > $0 (alternative hypothesis)

## Confidence Intervals
- 95% confidence interval for the mean
- Calculation: Mean ± t_(α/2, n-1) × (s/√n)

## Assumptions
1. Data is approximately normally distributed (or n > 30 for CLT)
2. Observations are independent
3. Measurement scale is at least interval

## Limitations
- Single day snapshot (2020-01-14)
- Potential for missing data
- External factors not controlled for
- Notion API rate limiting
