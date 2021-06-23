def imperial_bmi_formula(weight, height):
    return (weight/(height**2))*703


def metric_bmi_formula(weight, height):
    return weight/(height**2)


def calculate_bmi_category(bmi):
    if bmi < 18.5:
        print("That classifies you as being underweight.")
    elif bmi >= 18.5 and bmi < 24.9:
        print("That classifies you as being within a normal weight range.")
    elif bmi >= 25 and bmi < 29.9:
        print("That classifies you as being overweight.")
    elif bmi > 30:
        print("That classifies you as being obese.")
    else:
        print("Something went wrong.")


measurementSelection = input("Do you use the imperial or metric system? ")

if measurementSelection == "1" or measurementSelection == "imperial":
    userWeight = float(input("What is your weight in pounds (lb)? "))
    userHeight = float(input("What is your height in inches (in)? "))
    userBMI = imperial_bmi_formula(userWeight, userHeight)
    print("Your BMI is: ", round(userBMI, 2))
    calculate_bmi_category(userBMI)

if measurementSelection == "2" or measurementSelection == "metric":
    userWeight = float(input("What is your weight in kilograms (kg)? "))
    userHeight = float(input("What is your height in meters (m)? "))
    userBMI = metric_bmi_formula(userWeight, userHeight)
    print("Your BMI is: ", round(userBMI, 2))
    calculate_bmi_category(userBMI)
