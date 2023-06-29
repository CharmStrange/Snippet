import statistics
import random
from sklearn.linear_model import LinearRegression

# Function to get user input as a list of integers
def get_user_input(prompt):
    values = input(prompt).split()
    return [int(value) for value in values]

# Function to generate random data
def generate_random_data(min_val, max_val, num_samples):
    return [random.randint(min_val, max_val) for _ in range(num_samples)]

# Get user input for the data : This is vector!
# daily_restock = get_user_input("Enter daily restock values (separated by spaces): ")
# daily_visitors = get_user_input("Enter daily visitors values (separated by spaces): ")
# soldout_seeds = get_user_input("Enter soldout seeds values (separated by spaces): ")
# daily_my_ads = get_user_input("Enter daily My ADS values (separated by spaces): ")

# Generate random data
daily_restock = generate_random_data(0, 5000, 50)
daily_visitors = generate_random_data(0, 15, 50)
soldout_seeds = generate_random_data(0, 5000, 50)
daily_my_ads = generate_random_data(0, 15, 50)

# Calculate statistics
restock_mean = statistics.mean(daily_restock)
restock_var = statistics.variance(daily_restock)
restock_sd = statistics.stdev(daily_restock)

visitors_mean = statistics.mean(daily_visitors)
visitors_var = statistics.variance(daily_visitors)
visitors_sd = statistics.stdev(daily_visitors)

seeds_mean = statistics.mean(soldout_seeds)
seeds_var = statistics.variance(soldout_seeds)
seeds_sd = statistics.stdev(soldout_seeds)

ads_mean = statistics.mean(daily_my_ads)
ads_var = statistics.variance(daily_my_ads)
ads_sd = statistics.stdev(daily_my_ads)

print("Daily Restock - Mean:", restock_mean, "Variance:", restock_var, "Standard Deviation:", restock_sd)
print("Daily Visitors - Mean:", visitors_mean, "Variance:", visitors_var, "Standard Deviation:", visitors_sd)
print("Soldout Seeds - Mean:", seeds_mean, "Variance:", seeds_var, "Standard Deviation:", seeds_sd)
print("Daily My ADS - Mean:", ads_mean, "Variance:", ads_var, "Standard Deviation:", ads_sd)

# Regression model: daily visitors as a function of daily My ADS
regression_model_visitors = LinearRegression()
regression_model_visitors.fit([[ads] for ads in daily_my_ads], daily_visitors)

# Regression model: soldout seeds as a function of daily restock
regression_model_seeds = LinearRegression()
regression_model_seeds.fit([[restock] for restock in daily_restock], soldout_seeds)

# Predict new values
new_ads = get_user_input("Enter new values of daily My ADS (separated by spaces): ")
new_restock = get_user_input("Enter new values of daily restock (separated by spaces): ")

predicted_visitors = regression_model_visitors.predict([[ads] for ads in new_ads])
predicted_seeds = regression_model_seeds.predict([[restock] for restock in new_restock])

print("Predicted Visitors:", predicted_visitors)
print("Predicted Seeds:", predicted_seeds)
