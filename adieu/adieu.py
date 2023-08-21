def main ():
    import inflect
    p=inflect.engine()
    list_names=[]
    while True:
        try:
            name=input("Name: ")
            list_names.append(name)
        except EOFError:
            print()
            break
        except ValueError:
            pass

    print(f"Adieu, adieu, to {p.join(list_names)}")
if __name__=="__main__":
    main()