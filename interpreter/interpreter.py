def main():
    expression=input("Enter your math Expression  ? ")
    x,y,z=expression.split(" ")
    answer=evaluate(x,y,z)
    print(" {0:.1f}".format(answer))
def evaluate(x,y,z):
    y=str(y)
    x=int(x)
    z=int(z)
    if y=="+":
        answer1=(x+z)
    elif y=="-":
        answer1=(x-z)
    elif y=="*":
        answer1=(x*z)
    elif y=="/":
        answer1=(x/z)
    return answer1


main()