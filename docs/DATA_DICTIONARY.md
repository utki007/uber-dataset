# Uber Dataset - Data Dictionary

This document describes all datasets included in this repository and their fields.

## Dataset Files

### 1. uber_rides.csv
Main dataset containing individual ride/trip information.

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| ride_id | String | Unique identifier for each ride |
| date | Date (YYYY-MM-DD) | Date when the ride occurred |
| time | Time (HH:MM:SS) | Time when the ride started |
| pickup_latitude | Float | Latitude coordinate of pickup location |
| pickup_longitude | Float | Longitude coordinate of pickup location |
| dropoff_latitude | Float | Latitude coordinate of dropoff location |
| dropoff_longitude | Float | Longitude coordinate of dropoff location |
| passenger_count | Integer | Number of passengers in the ride |
| trip_duration_minutes | Integer | Duration of the trip in minutes |
| fare_amount | Float | Total fare charged for the ride (in USD) |
| payment_type | String | Payment method (credit_card, cash, etc.) |
| driver_id | String | Unique identifier for the driver |

**Sample Use Cases:**
- Analyzing ride patterns by time and location
- Calculating average trip duration and fare
- Identifying peak hours and popular routes

---

### 2. drivers.csv
Information about Uber drivers.

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| driver_id | String | Unique identifier for each driver |
| name | String | Driver's full name |
| phone | String | Contact phone number |
| email | String | Email address |
| registration_date | Date | Date when driver registered |
| rating | Float | Average driver rating (1-5 scale) |
| total_rides | Integer | Total number of completed rides |
| years_experience | Integer | Years of driving experience |
| vehicle_type | String | Type of vehicle (sedan, suv, etc.) |
| license_number | String | Driver's license number |

**Sample Use Cases:**
- Analyzing driver performance metrics
- Correlating driver rating with ride patterns
- Driver retention analysis

---

### 3. locations.csv
Geographic location information for popular pickup and dropoff points.

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| location_id | String | Unique identifier for the location |
| location_name | String | Name of the location/landmark |
| borough | String | NYC borough (Manhattan, Brooklyn, Queens, Bronx, Staten Island) |
| zone | String | Specific zone or neighborhood |
| latitude | Float | Latitude coordinate |
| longitude | Float | Longitude coordinate |
| popular_pickup | Boolean | Whether this is a popular pickup location |
| popular_dropoff | Boolean | Whether this is a popular dropoff location |

**Sample Use Cases:**
- Geographic analysis of ride distribution
- Identifying hotspots for pickups and dropoffs
- Route optimization

---

### 4. hourly_stats.csv
Aggregated statistics by hour and day.

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| date | Date | Date of the statistics |
| hour | Integer | Hour of the day (0-23) |
| day_of_week | String | Day name (Monday, Tuesday, etc.) |
| total_rides | Integer | Total number of rides in that hour |
| avg_fare | Float | Average fare amount for that hour |
| peak_hour | Boolean | Whether this is a peak traffic hour |
| weather_condition | String | Weather condition (clear, cloudy, rain, etc.) |

**Sample Use Cases:**
- Time series analysis
- Peak hour identification
- Weather impact analysis on ride demand
- Demand forecasting

---

### 5. fare_details.csv
Detailed breakdown of fare components for each ride.

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| ride_id | String | Unique identifier matching uber_rides.csv |
| base_fare | Float | Base fare charge (USD) |
| distance_fare | Float | Fare based on distance traveled (USD) |
| time_fare | Float | Fare based on time duration (USD) |
| surge_multiplier | Float | Surge pricing multiplier (1.0 = no surge) |
| tip_amount | Float | Tip given by passenger (USD) |
| taxes_fees | Float | Total taxes and fees (USD) |
| total_fare | Float | Final total fare (USD) |
| discount_applied | Boolean | Whether any discount was applied |

**Sample Use Cases:**
- Fare structure analysis
- Surge pricing patterns
- Revenue optimization
- Tipping behavior analysis

---

## Data Relationships

```
uber_rides.csv
├── ride_id → fare_details.csv (ride_id)
├── driver_id → drivers.csv (driver_id)
├── pickup/dropoff coordinates → locations.csv (latitude/longitude)
└── date/time → hourly_stats.csv (date/hour)
```

## Data Quality Notes

- All datasets contain sample data for demonstration and analysis purposes
- Coordinates are based on New York City locations
- Date range: January 2024
- All monetary values are in USD
- Missing values: None in the provided sample data

## Recommended Analysis Tasks

1. **Temporal Analysis**: Analyze ride patterns across different times and days
2. **Geographic Analysis**: Map popular routes and locations
3. **Revenue Analysis**: Calculate total revenue, average fares, and surge impact
4. **Driver Performance**: Evaluate driver ratings and productivity
5. **Demand Forecasting**: Predict future ride demand based on historical patterns
6. **Weather Impact**: Correlate weather conditions with ride volumes and fares

## Getting Started

To begin analyzing these datasets:

```python
import pandas as pd

# Load datasets
rides = pd.read_csv('data/raw/uber_rides.csv')
drivers = pd.read_csv('data/raw/drivers.csv')
locations = pd.read_csv('data/raw/locations.csv')
hourly_stats = pd.read_csv('data/raw/hourly_stats.csv')
fare_details = pd.read_csv('data/raw/fare_details.csv')

# Example: Merge rides with driver information
rides_with_drivers = rides.merge(drivers, on='driver_id')
```

## License and Usage

This dataset is provided for educational and analysis purposes. Please ensure compliance with data privacy regulations when using similar real-world data.
