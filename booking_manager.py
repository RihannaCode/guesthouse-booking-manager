import json


# Load previous bookings from the JSON file
def load_bookings():
    try:
        with open("bookings.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# Save bookings to the JSON file
def save_bookings(bookings):
    with open("bookings.json", "w") as file:
        json.dump(bookings, file, indent=4)


# Add a new booking
def add_booking(bookings):
    name = input("Enter the guest name: ")

    while True:
        try:
            nights = int(
                input("Enter the number of nights: ")
            )

            if nights > 0:
                break
            else:
                print("The number of nights must be greater than zero.")

        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            price_per_night = int(
                input("Enter the price per night: ")
            )

            if price_per_night > 0:
                break
            else:
                print("Price per night must be greater than zero.")

        except ValueError:
            print("Please enter a valid number.")

    booking = {
        "guest_name": name,
        "nights": nights,
        "price_per_night": price_per_night,
        "status": "active"
    }

    bookings.append(booking)
    save_bookings(bookings)

    print("Booking added successfully!")


# Show all bookings
def show_bookings(bookings):
    if not bookings:
        print("No bookings found.")
        return

    for booking in bookings:
        total_price = (
            booking["nights"] * booking["price_per_night"]
        )

        print("--------------------")
        print(f"Guest: {booking['guest_name']}")
        print(f"Nights: {booking['nights']}")
        print(f"Price per night: {booking['price_per_night']}")
        print(f"Total price: {total_price}")
        print(f"Status: {booking['status']}")

    print("--------------------")


# Search for a booking
def search_booking(bookings):
    name = input("Enter the guest name to search: ").lower()
    found = False

    for booking in bookings:
        if booking["guest_name"].lower() == name:
            total_price = (
                booking["nights"] * booking["price_per_night"]
            )

            print("--------------------")
            print(f"Guest: {booking['guest_name']}")
            print(f"Nights: {booking['nights']}")
            print(f"Price per night: {booking['price_per_night']}")
            print(f"Total price: {total_price}")
            print(f"Status: {booking['status']}")
            print("--------------------")

            found = True

    if not found:
        print("Booking not found.")


# Cancel an active booking
def cancel_booking(bookings):
    name = input("Enter the guest name to cancel: ").lower()

    for booking in bookings:
        if (
            booking["guest_name"].lower() == name
            and booking["status"] == "active"
        ):
            booking["status"] = "cancelled"
            save_bookings(bookings)

            print("Booking cancelled successfully!")
            return

    print("Active booking not found.")


# Calculate the total income from active bookings
def show_total_income(bookings):
    total_income = 0

    for booking in bookings:
        if booking["status"] == "active":
            booking_income = (
                booking["nights"] * booking["price_per_night"]
            )

            total_income += booking_income

    print(f"Total income: {total_income}")


# Load saved bookings when the program starts
bookings = load_bookings()


# Main menu
while True:
    print("\n===== Guesthouse Booking Manager =====")
    print("1. Add Booking")
    print("2. Show Bookings")
    print("3. Search Booking")
    print("4. Cancel Booking")
    print("5. Show Total Income")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_booking(bookings)

    elif choice == "2":
        show_bookings(bookings)

    elif choice == "3":
        search_booking(bookings)

    elif choice == "4":
        cancel_booking(bookings)

    elif choice == "5":
        show_total_income(bookings)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Please choose a number from 1 to 6.")
