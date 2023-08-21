def main():
    fileName=input("Enter file name ? ")
    answer1=fileName.casefold().replace("-"," ").replace(" ","")
    print(evaluate(answer1))


def evaluate(answer1):
        if answer1.endswith(".gif"):
            answer1=("image/gif")
        elif answer1.endswith(".jpeg"):
            answer1=("image/jpeg")
        elif answer1.endswith(".jpg"):
            answer1=("image/jpeg")
        elif answer1.endswith(".png"):
            answer1=("image/png")
        elif answer1.endswith(".pdf"):
            answer1=("application/pdf")
        elif answer1.endswith(".txt"):
            answer1=("text/plain")
        elif answer1.endswith(".zip"):
            answer1=("application/zip")
        else:
            answer1=("application/octet-stream")
        return answer1


main()