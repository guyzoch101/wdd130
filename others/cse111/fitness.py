# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input('Please enter your gender: (M / F) ').upper()
    birthdate_str = input('Please enter your birthdate in YYYY-MM-DD: ')
    height_inch = float(input('Please enter your height in U.S. inch: '))
    weight_lb = float(input('Please enter your weight in U.S. pounds: '))
    
    # Call the compute_age, lb_to_kg, in_to_kg,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    age = compute_age(birthdate_str)
    weight_kg = lb_to_kg(weight_lb)
    height_cm = in_to_kg(height_inch)
    bmi = body_mass_index(weight_kg, height_cm)
    bmr = basal_metabolic_rate(gender, weight_kg, height_cm, age)
    # Print the results for the user to see.
    
    print(f'Age (years): {age}')
    print(f'Weight (kg): {weight_kg:.2f}')
    print(f'height (cm): {height_cm:.1f}')
    print(f'Body mass index: {bmi:.1f}')
    print(f'Basal metabolic rate: {bmr:.0f}')
    pass


def compute_age(birthdate_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or (birthdate.month == today.month and birthdate.day > today.day):
        years -= 1
    
    return years


def lb_to_kg(weight_lb):
    # returned values are only local variables valid in the corresponding function
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    # 1 lb = 0.45359237 kg
    weight_kg = weight_lb * 0.45359237
    
    return weight_kg


def in_to_kg(height_inch):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    # 1 in = 2.54 cm
    height_cm = height_inch * 2.54
    
    return height_cm


def body_mass_index(weight_kg, height_cm):
    """Compute and return a person's body mass index.
    Parameters
        weight_kg: a person's weight in kilograms.
        height_cm: a person's height in centimeters.
    Return: a person's body mass index.
    """
    # bmi = 10,000 * weight / height^2
    bmi = 10000 * weight_kg / (height_cm ** 2)
    
    return bmi


def basal_metabolic_rate(gender, weight_kg, height_cm, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    # (women)  bmr = 447.593 + 9.247 weight + 3.098 height − 4.330 age
    # (men)  bmr = 88.362 + 13.397 weight + 4.799 height − 5.677 age
    
    if gender == 'M':
        bmr = 88.362 + 13.397 * weight_kg + 4.799 * height_cm - 5.677 * age
    elif gender == 'F':
        bmr = 447.593 + 9.247 * weight_kg + 3.098 * height_cm - 4.330 * age
        
    return bmr


# Call the main function so that
# this program will start executing.
main()
