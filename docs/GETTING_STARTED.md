# Getting Started with Uber Dataset Analysis

This guide will help you quickly get started with analyzing the Uber datasets in this repository.

## Quick Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- pandas (data manipulation)
- numpy (numerical operations)
- matplotlib (plotting)
- seaborn (statistical visualizations)
- jupyter (notebook environment)

### 2. Verify Installation

Run the sample analysis script:

```bash
python notebooks/analyze_uber_data.py
```

You should see detailed statistics and analysis output.

### 3. Explore with Jupyter

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Then open `notebooks/uber_analysis_quickstart.ipynb` for an interactive analysis experience.

## Dataset Overview

The repository contains 5 interconnected datasets:

| Dataset | Records | Description |
|---------|---------|-------------|
| uber_rides.csv | 25 | Individual ride records with pickup/dropoff details |
| drivers.csv | 10 | Driver profiles with ratings and experience |
| locations.csv | 10 | NYC location data with coordinates |
| hourly_stats.csv | 48 | Hourly aggregated statistics (2 days) |
| fare_details.csv | 25 | Detailed fare breakdowns with surge pricing |

## Common Analysis Patterns

### Loading Data

```python
import pandas as pd

rides = pd.read_csv('data/raw/uber_rides.csv')
drivers = pd.read_csv('data/raw/drivers.csv')
```

### Basic Statistics

```python
# Average fare
print(f"Average fare: ${rides['fare_amount'].mean():.2f}")

# Rides by payment type
print(rides['payment_type'].value_counts())

# Top drivers by rating
top_drivers = drivers.nlargest(5, 'rating')
print(top_drivers[['name', 'rating', 'total_rides']])
```

### Merging Datasets

```python
# Combine rides with driver information
rides_with_drivers = rides.merge(drivers, on='driver_id')

# Combine rides with fare details
complete_data = rides.merge(fare_details, on='ride_id')
```

### Time Series Analysis

```python
rides['datetime'] = pd.to_datetime(rides['date'] + ' ' + rides['time'])
rides['hour'] = rides['datetime'].dt.hour

# Rides by hour
hourly_distribution = rides.groupby('hour').size()
```

### Visualization

```python
import matplotlib.pyplot as plt

# Fare distribution
rides['fare_amount'].hist(bins=20)
plt.xlabel('Fare Amount ($)')
plt.ylabel('Frequency')
plt.title('Fare Distribution')
plt.show()
```

## Analysis Ideas

### Beginner Level
1. Calculate average fare by payment type
2. Find the busiest hours of the day
3. Identify the most active drivers
4. Compare trip durations across different times

### Intermediate Level
1. Analyze surge pricing patterns
2. Map geographic distribution of pickups/dropoffs
3. Predict trip duration based on distance
4. Calculate driver efficiency metrics

### Advanced Level
1. Build a fare prediction model
2. Optimize driver allocation based on demand
3. Identify profitable routes and times
4. Analyze weather impact on ride patterns

## Tips for Analysis

1. **Always check for missing values**: `df.isnull().sum()`
2. **Understand data types**: `df.dtypes`
3. **Get summary statistics**: `df.describe()`
4. **Visualize before analyzing**: Create plots to understand distributions
5. **Document your findings**: Use markdown cells in Jupyter notebooks

## Next Steps

1. Read the [Data Dictionary](DATA_DICTIONARY.md) for detailed field descriptions
2. Explore the sample Jupyter notebook
3. Try modifying the analysis script
4. Create your own analyses based on the patterns above

## Need Help?

- Check the Data Dictionary for field descriptions
- Review the sample notebook for examples
- Examine the analysis script for code patterns
- Open an issue if you find any problems

## Contributing

Found ways to improve the datasets or analysis? Contributions welcome!

1. Add more sample data
2. Create new analysis notebooks
3. Improve documentation
4. Add visualization examples

---

Happy analyzing! 🚗📊
