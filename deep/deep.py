def main():
    answer=input("what is the Answer to the Great Question ? ")
    answer1=answer.casefold().replace("-"," ").replace(" ","")
    print(evaluate(answer1))

def evaluate(answer1):
        if answer1=="42":
                answer1=("Yes")
        elif answer1=="fortytwo":
                answer1=("Yes")
        else:
                answer1=("NO")
        return answer1

main()