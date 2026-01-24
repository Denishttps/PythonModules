def ft_count_harvest_recursive():
    def count_days(until_day: int, day: int = 1):
        if day > until_day:
            print("Harvest time!")
            return
        print(f"Day {day}")
        count_days(until_day, day + 1)

    until_day = int(input("Days until harvest: "))
    count_days(until_day)