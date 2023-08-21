def main ():
    generate_integer(get_level)
    import random
    import sys
def get_level():
    while True:
        level=int(input("level: "))
        if level not in [1,2,3]:
            continue
        return level
def generate_integer(level):
    score=0
    for i in in range(10):
        trials=0
        if level==1:
            num1=random.randint(0,9)
            num2=random.randint(0,9)
        elif level==2:
            num1=random.randint(10,99)
            num2=random.randint(10,99)
        else:
            num1=random.randint(100,999)
            num2=random.randint(100,999)
        while True:
            print(f"{num1} + {num2} = " end="")
            answer=int(input())
            if answer==num1+num2:
                score+=1
                break
            elif answer!=num1+num2 and trials<3:
                print(f"EEEE")
            continue
            else:
                print(f"{num1} + {num2} ={num1+num2}")
            break

if __name__=="__main__":
    main()