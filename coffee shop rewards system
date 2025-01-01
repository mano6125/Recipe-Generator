# Function to calculate free drinks
def calculate_free_drinks(rewards_record, drinks_purchased):
    total_drinks = rewards_record + drinks_purchased
    free_drinks = total_drinks // 6
    return free_drinks

# Function to update rewards record
def update_rewards(rewards_record, drinks_purchased):
    total_drinks = rewards_record + drinks_purchased
    free_drinks = total_drinks // 6
    updated_rewards = total_drinks % 6
    return updated_rewards, free_drinks

# Function to process an order
def process_order(customers, customer_code, drinks_purchased):
    if customer_code not in customers:
        print(f"Customer {customer_code} not found. Adding to system with 0 rewards.")
        customers[customer_code] = 0  # Add new customer with 0 rewards

    current_rewards = customers[customer_code]
    updated_rewards, free_drinks = update_rewards(current_rewards, drinks_purchased)
    customers[customer_code] = updated_rewards  # Update the dictionary
    return updated_rewards, free_drinks

# Function to display customer data
def display_customer_data(customers):
    print("\nCustomer Rewards Records:")
    for customer_code, rewards_record in customers.items():
        print(f"Customer {customer_code}: {rewards_record} drinks towards next reward.")

# Main program
def main():
    # Dictionary to store customer data
    customers = {
        "C123": 5,  # Customer C123 has 5 drinks towards their next reward
        "A456": 2,  # Customer A456 has 2 drinks towards their next reward
    }

    while True:
        print("\nCoffee Shop Rewards System")
        print("1. Add or process an order")
        print("2. Display customer data")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            customer_code = input("Enter customer code: ")
            drinks_purchased = int(input("Enter number of drinks purchased: "))
            updated_rewards, free_drinks = process_order(customers, customer_code, drinks_purchased)
            print(f"Customer {customer_code}: {free_drinks} free drinks awarded.")
            print(f"Updated rewards record: {updated_rewards}")

        elif choice == "2":
            display_customer_data(customers)

        elif choice == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
