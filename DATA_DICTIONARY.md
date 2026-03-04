# Data Dictionary - Advertising Database

## Database Information
- **Name:** Advertising
- **ID:** 21b97551-844e-8068-b387-fe7a56b04348
- **Platform:** Notion
- **Record Type:** Advertising Campaigns

## Field Definitions

### CampaignID
- **Type:** Title
- **Description:** Unique identifier for each advertising campaign
- **Format:** Text string
- **Example:** "CAM-2020-001"
- **Required:** Yes

### StartDate
- **Type:** Date
- **Description:** The date when the advertising campaign began
- **Format:** ISO 8601 date (YYYY-MM-DD)
- **Example:** "2020-01-14"
- **Required:** Yes
- **Analysis Note:** Primary filter field for this study

### EndDate
- **Type:** Date
- **Description:** The date when the advertising campaign ended
- **Format:** ISO 8601 date (YYYY-MM-DD)
- **Example:** "2020-02-14"
- **Required:** Yes

### SpentAmount
- **Type:** Number
- **Description:** Total monetary amount spent on the campaign
- **Format:** Decimal number (currency)
- **Example:** 2500.00
- **Required:** Yes
- **Analysis Note:** Primary analysis variable
- **Unit:** USD (assumed)

### AdType
- **Type:** Select
- **Description:** Category of advertising medium
- **Options:**
  - Video (color: pink)
  - Search Engine (color: pink)
  - Social Media (color: purple)
  - Banner (color: orange)
- **Required:** No

### AdPlacement
- **Type:** Select
- **Description:** Location where ad was displayed
- **Options:**
  - Footer (color: gray)
  - Homepage (color: yellow)
  - News Section (color: red)
  - Sidebar (color: gray)
- **Required:** No

### Impressions
- **Type:** Number
- **Description:** Number of times the ad was displayed
- **Format:** Integer
- **Example:** 50000
- **Required:** No

### Conversions
- **Type:** Number
- **Description:** Number of desired actions taken (clicks, purchases, etc.)
- **Format:** Integer
- **Example:** 125
- **Required:** No

### ROI
- **Type:** Number
- **Description:** Return on investment as a percentage
- **Format:** Decimal number
- **Example:** 15.5 (representing 15.5%)
- **Required:** No

### CostPerClick
- **Type:** Number
- **Description:** Average cost per click
- **Format:** Decimal number (currency)
- **Example:** 2.50
- **Required:** No

### CostPerConversion
- **Type:** Number
- **Description:** Average cost per conversion
- **Format:** Decimal number (currency)
- **Example:** 45.00
- **Required:** No

### ConversionRate
- **Type:** Number
- **Description:** Percentage of impressions that resulted in conversions
- **Format:** Decimal number (percentage)
- **Example:** 0.25 (representing 0.25%)
- **Required:** No

### EngagementRate
- **Type:** Number
- **Description:** Percentage of audience that engaged with the ad
- **Format:** Decimal number (percentage)
- **Example:** 3.5 (representing 3.5%)
- **Required:** No

### AudienceReach
- **Type:** Number
- **Description:** Total number of unique individuals exposed to the ad
- **Format:** Integer
- **Example:** 45000
- **Required:** No

### TargetLocation
- **Type:** Select
- **Description:** Geographic targeting of the campaign
- **Options:**
  - International (color: green)
  - Local (color: gray)
  - National (color: purple)
  - Regional (color: orange)
- **Required:** No

### DeviceTargeting
- **Type:** Select
- **Description:** Device type targeting
- **Options:**
  - Desktop (color: gray)
  - All Devices (color: brown)
  - Mobile (color: pink)
  - Tablet (color: red)
- **Required:** No

### FrequencyCap
- **Type:** Number
- **Description:** Maximum number of times an individual will see the ad
- **Format:** Integer
- **Example:** 3
- **Required:** No

### KeywordFocus
- **Type:** Rich Text
- **Description:** Keywords or topics targeted by the campaign
- **Format:** Text
- **Example:** "Dorohedoro, anime, manga, dark fantasy"
- **Required:** No

### AudienceDemographics
- **Type:** Rich Text
- **Description:** Description of target audience demographics
- **Format:** Text
- **Example:** "Males 18-34 interested in anime and gaming"
- **Required:** No

## Data Quality Considerations
- **Missing Values:** Some optional fields may be empty
- **Data Validation:** Dates should be valid ISO 8601 format
- **Currency:** Assumed to be USD, but not explicitly specified
- **Duplicates:** CampaignID should be unique

## Analysis Notes
- Primary analysis will focus on `StartDate` and `SpentAmount` fields
- Secondary analysis may explore relationships between `SpentAmount` and performance metrics
- Date range for study: Single day (2020-01-14)