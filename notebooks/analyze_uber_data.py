#!/usr/bin/env python3
"""
Uber Dataset Analysis - Example Script

This script demonstrates basic analysis using the Uber datasets.
"""

import pandas as pd
import numpy as np

def load_datasets():
    """Load all Uber datasets."""
    print("Loading datasets...")
    rides = pd.read_csv('data/raw/uber_rides.csv')
    drivers = pd.read_csv('data/raw/drivers.csv')
    locations = pd.read_csv('data/raw/locations.csv')
    hourly_stats = pd.read_csv('data/raw/hourly_stats.csv')
    fare_details = pd.read_csv('data/raw/fare_details.csv')
    
    print(f"✓ Loaded {len(rides)} rides")
    print(f"✓ Loaded {len(drivers)} drivers")
    print(f"✓ Loaded {len(locations)} locations")
    print(f"✓ Loaded {len(hourly_stats)} hourly statistics")
    print(f"✓ Loaded {len(fare_details)} fare details")
    
    return rides, drivers, locations, hourly_stats, fare_details

def basic_statistics(rides, drivers):
    """Calculate and display basic statistics."""
    print("\n" + "="*60)
    print("BASIC STATISTICS")
    print("="*60)
    
    print(f"\nRides Overview:")
    print(f"  Total rides: {len(rides)}")
    print(f"  Average fare: ${rides['fare_amount'].mean():.2f}")
    print(f"  Average trip duration: {rides['trip_duration_minutes'].mean():.2f} minutes")
    print(f"  Average passengers per ride: {rides['passenger_count'].mean():.2f}")
    
    print(f"\nDriver Overview:")
    print(f"  Total drivers: {len(drivers)}")
    print(f"  Average driver rating: {drivers['rating'].mean():.2f}")
    print(f"  Average driver experience: {drivers['years_experience'].mean():.2f} years")
    
    print(f"\nPayment Distribution:")
    payment_dist = rides['payment_type'].value_counts()
    for payment_type, count in payment_dist.items():
        percentage = (count / len(rides)) * 100
        print(f"  {payment_type}: {count} ({percentage:.1f}%)")

def analyze_peak_hours(hourly_stats):
    """Analyze peak hours from hourly statistics."""
    print("\n" + "="*60)
    print("PEAK HOURS ANALYSIS")
    print("="*60)
    
    peak_hours = hourly_stats[hourly_stats['peak_hour'] == True]
    print(f"\nTotal peak hours recorded: {len(peak_hours)}")
    print(f"Average rides during peak hours: {peak_hours['total_rides'].mean():.0f}")
    print(f"Average fare during peak hours: ${peak_hours['avg_fare'].mean():.2f}")
    
    print("\nPeak hours by day:")
    for _, row in peak_hours.iterrows():
        print(f"  {row['day_of_week']} at {row['hour']:02d}:00 - {row['total_rides']} rides")

def analyze_top_drivers(rides, drivers):
    """Analyze top-performing drivers."""
    print("\n" + "="*60)
    print("TOP DRIVERS ANALYSIS")
    print("="*60)
    
    # Merge rides with drivers
    rides_with_drivers = rides.merge(drivers, on='driver_id')
    
    # Calculate rides per driver
    rides_per_driver = rides.groupby('driver_id').size()
    
    # Get top 5 drivers by rating
    top_drivers = drivers.nlargest(5, 'rating')
    
    print("\nTop 5 Drivers by Rating:")
    for idx, driver in top_drivers.iterrows():
        driver_rides = rides_per_driver.get(driver['driver_id'], 0)
        print(f"  {driver['name']}: {driver['rating']:.1f} stars, "
              f"{driver['total_rides']} total rides, "
              f"{driver_rides} rides in dataset")

def analyze_fare_breakdown(fare_details):
    """Analyze fare components."""
    print("\n" + "="*60)
    print("FARE BREAKDOWN ANALYSIS")
    print("="*60)
    
    print("\nAverage Fare Components:")
    print(f"  Base fare: ${fare_details['base_fare'].mean():.2f}")
    print(f"  Distance fare: ${fare_details['distance_fare'].mean():.2f}")
    print(f"  Time fare: ${fare_details['time_fare'].mean():.2f}")
    print(f"  Tips: ${fare_details['tip_amount'].mean():.2f}")
    print(f"  Taxes & fees: ${fare_details['taxes_fees'].mean():.2f}")
    print(f"  Total average: ${fare_details['total_fare'].mean():.2f}")
    
    # Surge pricing analysis
    surge_rides = fare_details[fare_details['surge_multiplier'] > 1.0]
    print(f"\nSurge Pricing:")
    print(f"  Rides with surge: {len(surge_rides)} ({len(surge_rides)/len(fare_details)*100:.1f}%)")
    print(f"  Average surge multiplier: {surge_rides['surge_multiplier'].mean():.2f}x")
    print(f"  Average fare with surge: ${surge_rides['total_fare'].mean():.2f}")

def main():
    """Main execution function."""
    print("\n" + "="*60)
    print("UBER DATASET ANALYSIS")
    print("="*60)
    
    # Load datasets
    rides, drivers, locations, hourly_stats, fare_details = load_datasets()
    
    # Run analyses
    basic_statistics(rides, drivers)
    analyze_peak_hours(hourly_stats)
    analyze_top_drivers(rides, drivers)
    analyze_fare_breakdown(fare_details)
    
    print("\n" + "="*60)
    print("ANALYSIS COMPLETE")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
