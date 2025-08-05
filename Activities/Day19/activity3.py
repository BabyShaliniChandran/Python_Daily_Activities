from datetime import datetime

date_input = input("Enter your date of joining (YYYY-MM-DD): ")

try:
    year, month, day = map(int, date_input.split("-"))
    joining_date = datetime(year, month, day).date()
    today = datetime.today().date()

    days_completed = (today - joining_date).days
    years = days_completed // 365
    months = (days_completed % 365) // 30

    print(f"Days completed: {days_completed}")
    print(f"Approximate duration: {years} years and {months} months")

except ValueError:
    print("Invalid date format. Please enter the date as YYYY-MM-DD.")
