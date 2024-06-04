def display_welcome_message():
    print("Welcome to the booking system")

def get_destination():
    while True:
        destination = input("Please select a destination (Spain, UK, France): ").strip().capitalize()
        if destination in ["Spain", "Uk", "France"]:
            return destination
        else:
            print("Invalid option, please try again.")

def get_destination_price(destination):
    prices = {"France": 120, "Uk": 0, "Spain": 200}
    return prices[destination]

def get_hotel():
    while True:
        hotel = input("Please select a hotel (1, 2, 3): ").strip()
        if hotel in ["1", "2", "3"]:
            return int(hotel)
        else:
            print("Invalid option, please try again.")

def get_hotel_price(hotel):
    prices = {1: 300, 2: 700, 3: 200}
    return prices[hotel]

def get_weeks():
    while True:
        try:
            weeks = int(input("How many weeks will you be staying (1, 2, or 3)? ").strip())
            if weeks in [1, 2, 3]:
                return weeks
            else:
                print("Invalid option, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")

def get_number_of_people():
    while True:
        try:
            adults = int(input("How many adults will be travelling? ").strip())
            children = int(input("How many children will be travelling? ").strip())
            return adults, children
        except ValueError:
            print("Invalid input, please enter a number.")

def calculate_total_price(dest_price, hotel_price, weeks, adults, children):
    adults_total = (dest_price + hotel_price * weeks) * adults
    children_total = ((dest_price + hotel_price * weeks) * children) / 2
    return adults_total + children_total

def get_rating():
    while True:
        rating = input("Please rate your experience with this booking system (5 stars, 4 stars, 3 stars, 2 stars, 1 star): ").strip()
        if rating in ["5 stars", "4 stars", "3 stars", "2 stars", "1 star"]:
            return rating
        else:
            print("Invalid option, please try again.")

def main():
    display_welcome_message()
    while True:
        destination = get_destination()
        dest_price = get_destination_price(destination)
        hotel = get_hotel()
        hotel_price = get_hotel_price(hotel)
        weeks = get_weeks()
        adults, children = get_number_of_people()
        total_price = calculate_total_price(dest_price, hotel_price, weeks, adults, children)
        print(f"The total price for your trip is: {total_price:.2f}")
        
        rating = get_rating()
        print(f"Thank you for rating us: {rating}")

        another_price = input("Would you like to calculate another price (yes/no)? ").strip().lower()
        if another_price != "yes":
            print("Thank you for using the booking system. Have a great trip!")
            break

if __name__ == "__main__":
    main()
