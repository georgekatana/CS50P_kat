def main ():
    grocery_dict={}
    while True:
        try:
            item=input().upper()
            if item in grocery_dict:
                grocery_dict[item]+=1
            else:
                grocery_dict[item]=1
        except NameError:
            pass
        except ValueError:
            pass
        except EOFError:
            #sorted(grocery_dict.items)
            for item in sorted(grocery_dict.keys()):
                print(grocery_dict[item], item)
            break
        #except Exception as e:
        #    print("Your Errors: {e}")


if __name__=="__main__":
    main()