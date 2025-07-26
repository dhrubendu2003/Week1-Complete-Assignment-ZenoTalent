from datetime import datetime

def get_birth_date():
    while True:
        try:
            birth_date_str = input("Enter your birth date (mm/dd/yyyy): ")
            birth_date = datetime.strptime(birth_date_str, '%m/%d/%Y')
            return birth_date
        except ValueError:
            print("Invalid date format. Please enter mm/dd/yyyy.")

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def convert_to_european_format(birth_date):
    return birth_date.strftime('%d/%m/%Y')

def main():
    birth_date = get_birth_date()
    age = calculate_age(birth_date)
    european_format = convert_to_european_format(birth_date)

    print(f"Your current age is: {age} years")
    print(f"Your birthdate in European format is: {european_format}")

if __name__ == "__main__":
    main()
