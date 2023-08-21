def main():
    greeting=input("How were you greeted  ")
    greeting1=greeting.casefold().replace(" ","")
    print (f"pay ${(evaluate(greeting1))}")

def evaluate(greeting1):
        if greeting1.startswith("hello"):
                return 0
        elif greeting1.startswith("h") and not greeting1.startswith("hello") :
                return 20
        else:
                return 100

if __name__ == "__main__":
    main()