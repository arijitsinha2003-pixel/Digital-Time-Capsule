
import json
import os
from datetime import date, datetime

FILE_NAME = "capsules.json"


def load_capsules():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read saved capsules.")
        return []


def save_capsules(capsules):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(capsules, file, indent=4)


def create_capsule(capsules):
    message = input("\nWrite a message to your future self: ").strip()

    if not message:
        print("Your message cannot be empty!")
        return

    unlock_date = input("Unlock date (YYYY-MM-DD): ").strip()

    try:
        parsed_date = datetime.strptime(
            unlock_date, "%Y-%m-%d"
        ).date()

        if parsed_date < date.today():
            print("Please choose today or a future date.")
            return

    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.")
        return

    capsule = {
        "message": message,
        "created": date.today().isoformat(),
        "unlock_date": parsed_date.isoformat()
    }

    capsules.append(capsule)
    save_capsules(capsules)

    print("\nYour time capsule has been saved! 📦")


def view_capsules(capsules):
    if not capsules:
        print("\nNo time capsules yet.")
        return

    today = date.today()

    for number, capsule in enumerate(capsules, start=1):
        unlock_date = date.fromisoformat(capsule["unlock_date"])

        print(f"\n--- Capsule {number} ---")
        print(f"Created: {capsule['created']}")
        print(f"Unlock date: {capsule['unlock_date']}")

        if today >= unlock_date:
            print(f"Message: {capsule['message']}")
        else:
            print("🔒 This message is still locked!")
            print(f"Come back on {unlock_date}.")


def main():
    capsules = load_capsules()

    while True:
        print("\n==============================")
        print("     DIGITAL TIME CAPSULE")
        print("==============================")
        print("1. Create a capsule")
        print("2. View my capsules")
        print("3. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            create_capsule(capsules)

        elif choice == "2":
            view_capsules(capsules)

        elif choice == "3":
            print("Keep making memories. Goodbye! 👋")
            break

        else:
            print("Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
