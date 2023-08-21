import requests
import urllib.request
import json
import sys
def main():
    if float(sys.argv[1]):
        try:
            n=float(sys.argv[1])
            r=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            bitcoin_dict=r.json()
            rate=float(bitcoin_dict["bpi"]["USD"]["rate_float"])
            bitcoin_value=rate*n
            print(f"${bitcoin_value:,.4f}")
        except requests.RequestException:
            print("Could not open url")
        except ValueError:
            sys.exit("Command-line argument is not a Number")

if __name__=="__main__":
    main()