from validator_collection import checkers

def main():
    print(validate_email(input("Whats your Email Adress?: ")))

def validate_email(s):
    match = checkers.is_email(s)
    if match:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
