def main():
    Plate = input("Plate: ")
    if is_valid(Plate)== True:
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 6>=len(s)>=2 and s[0:2].isalpha() and s.isalnum():
        return True
    else:
        return False
    i=1
    while i<len(s):
        if s[i].isalpha()==True:
            if not s[i]==0:
                return True
        else:
            break
        i+=1

main()