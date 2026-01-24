def ft_plant_age():
    age_in_days = input("Enter plant age in days: ")
    if int(age_in_days) > 60:
        print("The plant is ready to harvest.")
    else:
        print("The plant is not ready to harvest.")