def main():
    print("Amount due: 50")
    amount_due=50
    total_coins=0
    while True:
        inserted_coin=int(input("Insert Coin: "))
        if inserted_coin==25 or inserted_coin==10 or inserted_coin==5:
            amount_due-=inserted_coin
            total_coins+=inserted_coin
        else:
            print(f"Amount Due: {amount_due}")
        if total_coins >=50:
            change_owed=total_coins-50
            print(f"change owed: {change_owed}")
            break
        else:
            print(f"Amount Due: {amount_due}")



#run main
main()