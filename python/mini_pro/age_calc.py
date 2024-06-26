import datetime

while True:
    birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")
    
    try:
        birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format")
        continue
    
    current_date = datetime.datetime.now()
    age = current_date - birth_date
    age_years = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
    age_days = age.days
    age_months = int(age_days / 30.4) 
    age_hours = age.days * 24 + age.seconds // 3600
    age_minutes = age_hours * 60 + (age.seconds // 60) % 60
    age_seconds = age_days * 24 * 3600 + age.seconds

    print(f"{age_years} years")
    print(f"{age_months} months")
    print(f"{age_days} days")
    print(f"{age_hours} hours")
    print(f"{age_minutes} minutes")
    print(f"{age_seconds} seconds")
    
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == "n":
        break