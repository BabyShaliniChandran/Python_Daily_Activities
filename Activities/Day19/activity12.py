try:
    with open("guests.txt", "r") as file:
        guests = file.readlines()
        print("Current guests:")
        for guest in guests:
            print(guest.strip())
except FileNotFoundError:
    print("Guest list is empty.")

new_guest = input("Enter the name of the new guest: ")

with open("guests.txt", "a") as file:
    file.write(new_guest + "\n")

print(open("guests.txt").read())
