weight = int(input("Enter your weight: "))
LbKg = input("L(lb) or K(kg)")
if LbKg.upper() == "L":
    ConvertedWeight = weight * 0.45
    print(str(ConvertedWeight) + " kilos")
else:
    ConvertedWeight = weight / 0.45
    print(str(ConvertedWeight) + " pounds")