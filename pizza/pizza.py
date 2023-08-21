import tabulate
import csv
import sys
def main ():
     if len(sys.argv)==1:
          sys.exit("Too few command line arguments")
     elif len(sys.argv)>2:
          sys.exit("Too many Command line arguments")
     elif not sys.argv[1].endswith(".csv"):
          sys.exit("Not a Python file")
     else:
          csv_name=sys.argv[1]
          try:
               with open(csv_name,"r") as csv_name:
                    csv_reader = csv.DictReader(csv_name)
                    mylist=list(csv_reader)
                    print(tabulate.tabulate(mylist,headers="keys",tablefmt="grid"))

          except FileNotFoundError:
               sys.exit("file does not exist")

if __name__ == "__main__":
    main()