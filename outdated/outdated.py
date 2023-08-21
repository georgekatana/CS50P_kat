def main ():
    months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    numbers=[1,2,3,4,5,6,7,8,9,10,11,12]

    while True:
        try:
            user_date=input("Date: ")
            date=user_date.replace("/"," ")
            date1=date.replace(","," ")
            month, date2, year=date1.split(" ")
            if int(date2)>0 and int(date2)<31:
                if month in months and "," in user_date:
                    month=months.index(month)+1
                    print(f"{int(year):02}"+'-'+f"{int(month):02}"+'-'f"{int(date2):02}")
                    break
                elif int(month) in numbers and "/" in user_date:
                    print(f"{int(year):02}"+'-'+f"{int(month):02}"+'-'+f"{int(date2):02}")
                    break
        except NameError:
            pass
        except ValueError:
            pass

if __name__=="__main__":
    main()