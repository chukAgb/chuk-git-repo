def collect_rainfall_data(num_years, rainfall_data):
    # Initialize variables to store total rainfall and number of months
    total_rainfall = 0
    total_months = num_years * 12

    # Outer loop to iterate over each year
    for year in range(1, num_years + 1):
        print(f"Year {year}:")

        # Inner loop to iterate over each month
        for month in range(1, 13):
            rainfall = rainfall_data[year-1][month-1]
            total_rainfall += rainfall

    # Calculate average rainfall per month
    average_rainfall = total_rainfall / total_months

    # Display the results
    print(f"\nNumber of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall}")
    print(f"Average rainfall per month: {average_rainfall:.2f}")

# number of years:
num_years = 2
rainfall_data = [
    [3.4, 4.5, 2.3, 5.6, 3.2, 4.1, 3.9, 4.0, 3.7, 4.2, 3.8, 4.1],  # Year 1
    [3.5, 4.6, 2.4, 5.7, 3.3, 4.2, 4.0, 4.1, 3.8, 4.3, 3.9, 4.2]   # Year 2
]

collect_rainfall_data(num_years, rainfall_data)
