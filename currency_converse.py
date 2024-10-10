def currency_conversion():
    #Country and the exchange rate.
    country1 = input("Enter the name of country1: ")
    country1_currency = input("Enter the currency initials for country1: ")
    country2 = input("Enter the name of country2: ")
    country2_currency = input("Enter the currency initials for country2: ")

    # Ask the user to choose 1 or 2
    choice = input(f"Enter '1' to convert from {country1} to {country2}, or '2' to convert from {country2} to {country1}: ")

    # Get the exchange rate
    exchange_rate = float(input(f"Enter the exchange rate from {country1_currency} to {country2_currency}: "))

    if choice == "1":
        # Convert from country1 to country2
        amount_country1 = float(input(f"Enter the amount in {country1_currency}: "))
        amount_country2 = amount_country1 * exchange_rate
        print(f"{amount_country1:.2f} {country1_currency} is equal to {amount_country2:.2f} {country2_currency}")

    elif choice == "2":
        # Convert from country2 to country1
        amount_country2 = float(input(f"Enter the amount in {country2_currency}: "))
        amount_country1 = amount_country2 / exchange_rate
        print(f"{amount_country2:.2f} {country2_currency} is equal to {amount_country1:.2f} {country1_currency}")
    
    else:
        print("Invalid choice. Please enter '1' or '2'.")

# Call the function to perform the conversion
currency_conversion()