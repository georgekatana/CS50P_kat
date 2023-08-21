def main():
    #get input for mass in kilograms
    m=int(input("type mass in kilograms: "))
    result=convert_to_energy(m)
    print("M: ",result)
def convert_to_energy(m):
     c=300000000
     energy=m*(c*c)
     return energy

main()