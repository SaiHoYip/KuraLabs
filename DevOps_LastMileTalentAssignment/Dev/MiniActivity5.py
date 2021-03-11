housePrice = 1000000
buyerCreditGood = True
if buyerCreditGood:
    downPayment = 0.1 * housePrice
else:
    downPayment = 0.2 * housePrice

print("Down Payment: " + str(downPayment))