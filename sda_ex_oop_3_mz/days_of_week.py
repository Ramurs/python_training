def day_of_week(value:int)->str:
    days= {
    1: "Poniedziałek",
    2: "Wtorek",
    3: "Środa",
    4: "Czwartek",
    5: "Piątek",
    6: "Sobota",
    7: "Niedziela"
    }
    return (days[value])

def main():
    value=int(input("Podaj nr dnia tygodnia "))
    print(day_of_week(value))

if __name__ == "__main__":
    main()