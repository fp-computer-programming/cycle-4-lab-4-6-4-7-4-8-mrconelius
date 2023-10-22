beast = input("bear")
dish = input("fish")
beast = beast.strip(" -")
dish = dish.strip(" -")
if beast[0] == dish[0] and beast[0] == dish[-1]:
    print("True")
else:
    print("false")