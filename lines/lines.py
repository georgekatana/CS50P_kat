import sys
import os
def main ():
     if len(sys.argv)==1:
          sys.exit("Too few command line arguments")
     elif len(sys.argv)>2:
          sys.exit("Too many Command line arguments")
     elif not sys.argv[1].endswith(".py"):
          sys.exit("Not a Python file")
     else:
          file_name=sys.argv[1]
          try:
               with open(file_name,"r") as file_name:
                    content=file_name.readlines()
                    new_lines=0
                    for line in content:
                         if not line.lstrip().startswith("#") and line.lstrip() !='':
                              new_lines+=1
               print(new_lines,end='')
          except FileNotFoundError:
               sys.exit("file does not exist")

if __name__ == "__main__":
    main()