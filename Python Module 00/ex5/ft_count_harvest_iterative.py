def ft_count_harvest_iterative():
    until_day = int(input("Days until harvest: "))
    for day in range(1, until_day + 1):
        print(f"Day {day}")
    print("Harvest time!")
