def main():
    global camel_case
    camel_case=input("Camel Case: ")
    #run convert function on camel case
    convert_to_snake_case(camel_case)
    #print back converted case
    #camel case function definitions
def convert_to_snake_case(snake_case):
    for letter in camel_case:
        if letter.isupper():
            print("_"+letter.lower(),end="")
        else:
            print(letter,end="")
    return snake_case

#run main
main()