# Uber Dataset Repository

A comprehensive collection of datasets for analyzing Uber ride-sharing data. This repository contains sample datasets that simulate real-world Uber operations, perfect for data analysis, machine learning, and visualization projects.

## 📊 Datasets Included

This repository contains the following datasets:

1. **uber_rides.csv** - Individual ride/trip records with pickup/dropoff locations, timing, and basic fare information
2. **drivers.csv** - Driver information including ratings, experience, and contact details
3. **locations.csv** - Geographic data for popular NYC locations and zones
4. **hourly_stats.csv** - Aggregated statistics by hour including weather conditions
5. **fare_details.csv** - Detailed fare breakdowns with surge pricing and tips

## 📁 Repository Structure

```
uber-dataset/
├── data/
│   ├── raw/              # Raw dataset files
│   │   ├── uber_rides.csv
│   │   ├── drivers.csv
│   │   ├── locations.csv
│   │   ├── hourly_stats.csv
│   │   └── fare_details.csv
│   └── processed/        # Processed/cleaned datasets (add your own)
├── docs/
│   └── DATA_DICTIONARY.md  # Comprehensive data documentation
├── notebooks/            # Jupyter notebooks for analysis (add your own)
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pandas
- numpy
- matplotlib/seaborn (for visualization)

### Quick Start

```python
import pandas as pd

# Load the main rides dataset
rides = pd.read_csv('data/raw/uber_rides.csv')

# Basic exploration
print(rides.head())
print(rides.describe())

# Load other datasets as needed
drivers = pd.read_csv('data/raw/drivers.csv')
locations = pd.read_csv('data/raw/locations.csv')
hourly_stats = pd.read_csv('data/raw/hourly_stats.csv')
fare_details = pd.read_csv('data/raw/fare_details.csv')
```

## 📖 Documentation

For detailed information about each dataset, field descriptions, data types, and relationships, see the [Data Dictionary](docs/DATA_DICTIONARY.md).

## 🔍 Sample Analysis Ideas

- **Temporal Analysis**: Identify peak hours, daily patterns, and seasonal trends
- **Geographic Analysis**: Map popular routes and high-demand areas
- **Revenue Analytics**: Analyze fare structures, surge pricing impact, and tipping patterns
- **Driver Performance**: Evaluate driver ratings, productivity, and retention
- **Predictive Modeling**: Forecast demand, predict fares, or estimate trip duration
- **Weather Impact**: Correlate weather conditions with ride volumes and pricing

## 📊 Key Statistics (Sample Data)

- **Total Rides**: 25 sample records
- **Date Range**: January 15-17, 2024
- **Location**: New York City (Manhattan, Brooklyn, Queens, Bronx, Staten Island)
- **Drivers**: 10 sample driver profiles
- **Time Coverage**: Hourly statistics for 48 hours

## 🛠️ Data Analysis Tools

Recommended tools for working with this dataset:

- **Python**: pandas, numpy, scikit-learn
- **Visualization**: matplotlib, seaborn, plotly
- **Geospatial**: folium, geopandas
- **Statistics**: scipy, statsmodels
- **Machine Learning**: scikit-learn, tensorflow, pytorch

## 📝 Example Use Cases

### 1. Calculate Average Fare by Hour
```python
import pandas as pd

rides = pd.read_csv('data/raw/uber_rides.csv')
rides['hour'] = pd.to_datetime(rides['time']).dt.hour
avg_fare_by_hour = rides.groupby('hour')['fare_amount'].mean()
print(avg_fare_by_hour)
```

### 2. Analyze Driver Performance
```python
drivers = pd.read_csv('data/raw/drivers.csv')
top_drivers = drivers.nlargest(5, 'rating')
print(top_drivers[['name', 'rating', 'total_rides']])
```

### 3. Merge Datasets for Comprehensive Analysis
```python
# Combine rides with fare details and driver info
rides = pd.read_csv('data/raw/uber_rides.csv')
fares = pd.read_csv('data/raw/fare_details.csv')
drivers = pd.read_csv('data/raw/drivers.csv')

complete_data = rides.merge(fares, on='ride_id').merge(drivers, on='driver_id')
```

## 🤝 Contributing

Feel free to contribute by:
- Adding more sample data
- Creating analysis notebooks
- Improving documentation
- Suggesting new features or datasets

## ⚠️ Important Notes

- This is **sample data** for educational and demonstration purposes
- Real Uber data contains personally identifiable information (PII) and should be handled according to privacy regulations
- Always follow data privacy laws (GDPR, CCPA, etc.) when working with real ride-sharing data
- This dataset simulates New York City operations but can be adapted for other cities

## 📄 License

This dataset is provided for educational and analysis purposes. Please ensure compliance with data privacy regulations when using similar real-world data.

## 📧 Contact

For questions or suggestions, please open an issue in this repository.

## 🎯 Future Enhancements

- [ ] Add more diverse sample data (different cities, seasons)
- [ ] Include cancellation and refund data
- [ ] Add customer demographic information (anonymized)
- [ ] Include vehicle maintenance records
- [ ] Add traffic and route optimization data
- [ ] Include customer ratings and feedback

---

**Happy Analyzing! 🚗📈**
