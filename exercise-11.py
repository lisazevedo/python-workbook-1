def imperial_volume(units, measure): 
    if "cup" in measure: print("{} cup(s), {} tablespoon(s), {} teaspoon(s)".format(str(units), "0", "0"))
    elif "tablespoon" in measure: print("{} cup(s), {} tablespoon(s), {} teaspoon(s)".format(str(int(int(units) / 16)), str(int(int(units) % 16)), "0"))
    elif "teaspoon"in measure: print("{} cup(s), {} tablespoon(s), {} teaspoon(s)".format(str(int(int(int(int(units) / 3)) / 16)), str(int(int(int(int(units) / 3)) % 16)), str(int(int(units) % 3))))

def main(): imperial_volume(input("Enter unit: "), input("Enter measure: "))

if __name__ == "__main__": main()
