# Author: GitHub Copilot
# Booking App - Command-line application for managing appointments

import json
import os
from datetime import datetime, timedelta

# Path to the bookings data file
DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "bookings.json")

# Available services and their durations (in minutes)
SERVICES = {
    "1": {"name": "Haircut", "duration": 30, "price": 25.00},
    "2": {"name": "Hair Coloring", "duration": 90, "price": 80.00},
    "3": {"name": "Massage (30 min)", "duration": 30, "price": 45.00},
    "4": {"name": "Massage (60 min)", "duration": 60, "price": 80.00},
    "5": {"name": "Facial", "duration": 60, "price": 60.00},
    "6": {"name": "Manicure", "duration": 45, "price": 35.00},
}

# Available time slots (hour, minute)
TIME_SLOTS = [
    "09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
    "12:00", "12:30", "13:00", "13:30", "14:00", "14:30",
    "15:00", "15:30", "16:00", "16:30", "17:00",
]


def load_bookings():
    """Load bookings from the JSON data file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_bookings(bookings):
    """Save bookings to the JSON data file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(bookings, f, indent=2)


def _next_booking_id(bookings):
    """Return the next unique booking ID, independent of list length."""
    if not bookings:
        return "BK0001"
    max_num = 0
    for b in bookings:
        try:
            num = int(b["id"][2:])
            if num > max_num:
                max_num = num
        except (ValueError, IndexError):
            pass
    return f"BK{max_num + 1:04d}"


def _slot_to_minutes(slot):
    """Convert 'HH:MM' string to total minutes since midnight."""
    h, m = slot.split(":")
    return int(h) * 60 + int(m)


def get_available_slots(date_str, bookings):
    """Return time slots not yet booked (respecting service durations) for the given date."""
    occupied_ranges = []
    for b in bookings:
        if b["date"] == date_str:
            start = _slot_to_minutes(b["time"])
            end = start + b.get("duration", 30)
            occupied_ranges.append((start, end))

    available = []
    for slot in TIME_SLOTS:
        slot_start = _slot_to_minutes(slot)
        if not any(start <= slot_start < end for start, end in occupied_ranges):
            available.append(slot)
    return available


def print_separator():
    print("-" * 50)


def print_header(title):
    print_separator()
    print(f"  {title}")
    print_separator()


def view_available_slots(bookings):
    """Display available time slots for a chosen date."""
    print_header("View Available Slots")
    date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date_str:
        date_str = datetime.today().strftime("%Y-%m-%d")
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    available = get_available_slots(date_str, bookings)
    print(f"\nAvailable slots on {date_str}:")
    if not available:
        print("  No slots available for this date.")
    else:
        for slot in available:
            print(f"  {slot}")


def book_appointment(bookings):
    """Book a new appointment."""
    print_header("Book an Appointment")

    # Choose date
    date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date_str:
        date_str = datetime.today().strftime("%Y-%m-%d")
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    # Show available slots
    available = get_available_slots(date_str, bookings)
    if not available:
        print(f"No available slots on {date_str}.")
        return
    print(f"\nAvailable slots on {date_str}:")
    for i, slot in enumerate(available, 1):
        print(f"  {i}. {slot}")

    # Choose time slot
    slot_choice = input("\nSelect slot number: ").strip()
    if not slot_choice.isdigit() or not (1 <= int(slot_choice) <= len(available)):
        print("Invalid slot selection.")
        return
    chosen_time = available[int(slot_choice) - 1]

    # Choose service
    print("\nAvailable services:")
    for key, svc in SERVICES.items():
        print(f"  {key}. {svc['name']} ({svc['duration']} min) - ${svc['price']:.2f}")

    service_choice = input("\nSelect service number: ").strip()
    if service_choice not in SERVICES:
        print("Invalid service selection.")
        return
    chosen_service = SERVICES[service_choice]

    # Enter name
    name = input("\nEnter your name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    # Enter phone (optional)
    phone = input("Enter your phone number (optional): ").strip()

    # Create booking
    booking_id = _next_booking_id(bookings)
    booking = {
        "id": booking_id,
        "name": name,
        "phone": phone,
        "date": date_str,
        "time": chosen_time,
        "service": chosen_service["name"],
        "duration": chosen_service["duration"],
        "price": chosen_service["price"],
        "booked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    bookings.append(booking)
    save_bookings(bookings)

    print(f"\n✓ Booking confirmed!")
    print(f"  Booking ID : {booking_id}")
    print(f"  Name       : {name}")
    print(f"  Date       : {date_str} at {chosen_time}")
    print(f"  Service    : {chosen_service['name']}")
    print(f"  Price      : ${chosen_service['price']:.2f}")


def view_bookings(bookings):
    """Display all current bookings."""
    print_header("All Bookings")
    if not bookings:
        print("  No bookings found.")
        return
    for b in sorted(bookings, key=lambda x: (x["date"], x["time"])):
        print(f"  [{b['id']}] {b['date']} {b['time']} | {b['name']} | {b['service']} | ${b['price']:.2f}")


def cancel_booking(bookings):
    """Cancel an existing booking by ID."""
    print_header("Cancel a Booking")
    if not bookings:
        print("  No bookings to cancel.")
        return

    view_bookings(bookings)
    booking_id = input("\nEnter booking ID to cancel (e.g. BK0001): ").strip().upper()

    for i, b in enumerate(bookings):
        if b["id"] == booking_id:
            confirm = input(
                f"Cancel booking for {b['name']} on {b['date']} at {b['time']}? (y/n): "
            ).strip().lower()
            if confirm == "y":
                bookings.pop(i)
                save_bookings(bookings)
                print(f"✓ Booking {booking_id} has been cancelled.")
            else:
                print("Cancellation aborted.")
            return

    print(f"Booking ID '{booking_id}' not found.")


def main():
    bookings = load_bookings()

    while True:
        print_header("Welcome to the Booking App")
        print("  1. View available slots")
        print("  2. Book an appointment")
        print("  3. View all bookings")
        print("  4. Cancel a booking")
        print("  5. Exit")
        print_separator()

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            view_available_slots(bookings)
        elif choice == "2":
            book_appointment(bookings)
        elif choice == "3":
            view_bookings(bookings)
        elif choice == "4":
            cancel_booking(bookings)
        elif choice == "5":
            print("\nGoodbye! See you soon.")
            break
        else:
            print("Invalid option. Please choose 1-5.")

        print()


if __name__ == "__main__":
    main()
