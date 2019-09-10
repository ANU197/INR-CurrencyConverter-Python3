with open("/home/apdebian/Desktop/python3/exchangeprice.txt") as f:
    fl = []
    fl = f.readlines()
    currencyDict = {}
    for line in fl:
        parsed = line.split("\t")
        currencyDict[parsed[0]] = float(parsed[1])


INR = float(input("Enter Amount:"))
print('\n')
print('Enter the name of the currency you want to convert amount to? Available options:\n')
for item in currencyDict.keys():
    print(item)

print('\n')
currency = input('Please enter one of them: ')
print(f"{INR} INR is equal to {INR*currencyDict[currency]} {currency}")
