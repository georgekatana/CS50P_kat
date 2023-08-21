def main():
    phrase=input("Hello: ")
    result=convert(phrase)
    print(result)

def convert(phrase):
     phrase=phrase.replace(":)","🙂")
     phrase1=phrase.replace(":(","🙁")
     return phrase1

main()

