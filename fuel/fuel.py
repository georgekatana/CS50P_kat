def main ():
    percentage_fuel=get_fraction()*100
    percentage_fuel=round(percentage_fuel)
    if  percentage_fuel>=99:
        print("F")
    elif percentage_fuel<=1:
        print("E")
    else:
        print(f"{percentage_fuel}%")

def get_fraction():
    while True:
        try:
            x, y = map(int, input("Fraction:").split("/"))
            #print("X: ",x,"\nY: ",y)
            fraction=x/y
            if fraction>1:
                raise ValueError
            return fraction
        except ZeroDivisionError:
            pass
        except ValueError:
           pass
        except NameError:
           pass

if __name__ == "__main__":
    main()