import re
import sys
def main():
    print(f'{validate(input("IPv4 Adress:"))}')
def validate(ip):
    valid_ip=re.search(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:\.|$)){4}$",ip)
    if valid_ip :
        return True
    else:
        return False

if __name__=="__main__":
    main()