# Program to calculate the total amount of a meal purchased at a restaurant.
#def calculate_meal_cost(food_charge):
    # Calculate tip (18% of food charge)
    #tip = food_charge * 0.18

    # Calculate sales tax (7% of food charge)
   # sales_tax = food_charge * 0.07

    # Calculate total price
  #  total_price = food_charge + tip + sales_tax

 #   return tip, sales_tax, total_price

# Ask the user to enter the charge for the food
#food_charge = float(input("Enter the charge for the food: "))

# Calculate the amounts
#tip, sales_tax, total_price = calculate_meal_cost(food_charge)

# Display the amounts
#print(f"Food Charge: ${food_charge:.2f}")
#print(f"Tip (18%): ${tip:.2f}")
#print(f"Sales Tax (7%): ${sales_tax:.2f}")
#print(f"Total Price: ${total_price:.2f}")



# Program to calculate the total amount of a meal purchased at a restaurant, including tip and sales tax

# Ast the user to enter the charge for the food
food_charge = float(input("Please Enter the charge for the food here: $"))

# Calculate tip and sales tax
# 18% tip
tip = food_charge * 0.18

# 7% sales tax
sales_tax = food_charge * 0.07

# Calculate the total amount
total_amount = food_charge + tip + sales_tax

# Display the breakdown and the total amount
print("\n--- Receipt ---")
print(f"Food Charge: ${food_charge:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Sales Tax (7%): ${sales_tax:.2f}")
print(f"Total Amount: ${total_amount:.2f}")
