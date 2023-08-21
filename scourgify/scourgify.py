import tabulate
import csv
import sys
def main ():
     if len(sys.argv)==2:
          sys.exit("Too few command line arguments")
     elif len(sys.argv)>3:
          sys.exit("Too many Command line arguments")
     elif not sys.argv[1].endswith(".csv") and not sys.argv[2].endswith(".csv"):
          sys.exit(f'{sys.argv[1]} is not a Valid CSV file')
     else:
          csv_name=sys.argv[1]
          new_csv_name=sys.argv[2]
          try:
               with open(csv_name) as csv_name:
                    csv_reader = csv.DictReader(csv_name)
                    with open(sys.argv[2], 'w') as new_csv_name:
                         fieldnames = ['first_name', 'last_name','house']
                         writer = csv.DictWriter(new_csv_name,fieldnames=fieldnames)
                         writer.writeheader()
                         for row in csv_reader:
                              row['name']=row['name'].replace(" ","")
                              row['first_name']=row.pop("name")
                              first_name,last_name=row['first_name'].split(",")
                              row['first_name']=last_name
                              row['last_name']=first_name
                              row['last_name'].strip()
                              row['first_name'].strip()
                              writer.writerow(row)

          except FileNotFoundError:
               sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()