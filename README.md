# Guesthouse Booking Manager

This is a simple Python project I built to practice what I have learned so far and use different Python concepts in one program.

The program can be used to add and manage guesthouse bookings. It saves the information in a JSON file, so the bookings are not lost when the program is closed.

## Features

- Add a new booking
- Show all bookings
- Search for a booking by guest name
- Cancel an active booking
- Calculate the total price of each booking
- Show the total income from active bookings
- Save and load bookings using a JSON file
- Handle invalid inputs

## What I Practiced

While building this project, I practiced:

- Python functions
- Lists and dictionaries
- Loops and conditions
- Getting input from the user
- Error handling with `try` and `except`
- Reading and writing JSON files
- Searching and changing information inside a list
- Organizing a program with a menu

## How It Works

When the program starts, it loads previous bookings from `bookings.json`.

The user can choose from the menu:

1. Add Booking
2. Show Bookings
3. Search Booking
4. Cancel Booking
5. Show Total Income
6. Exit

New bookings are saved automatically. When a booking is cancelled, its status changes from `active` to `cancelled`.

Cancelled bookings are not included in the total income.

## Run the Project

Make sure Python is installed, then run:

```bash
python booking_manager.py
```

No external libraries are required.

## Why I Built This

I built this project as the next step in my Python learning journey. It helped me practice working with saved data and building a program with several connected features.
