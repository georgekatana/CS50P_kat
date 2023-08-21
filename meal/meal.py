def main():
    time=input("What time is it? ")
    mealtime=convert(time)
    time.casefold()
    if 8.0>=mealtime>=7.0:
        print("breakfast time")
    elif 13.0>=mealtime>=12.0:
        print("lunch time")
    elif 19.0>=mealtime>=18.0:
        print("dinner time")
def convert(time):
    hours,minutes=time.split(":")
    minutes=minutes.replace("pm","").replace("am","")
    hours=(float(hours)+(float(minutes)/60))
    return hours

if __name__ == "__main__":
    main()