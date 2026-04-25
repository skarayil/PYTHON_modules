def  ft_water_reminder():
    water_reminder = int(input("Days since last watering: "))
    if  water_reminder <= 2:
        print("Plants are fine")
    else:
        print("Water the plants!")