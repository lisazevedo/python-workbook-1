import string

def isInteger(string): return False if len(''.join(c for c in string.strip() if not c.isdigit())) > 1 and ''.join(c for c in string.strip() if not c.isdigit()) != '-' and ''.join(c for c in string.strip() if not c.isdigit()) != '+' else True

def main(): print("Is a integer") if isInteger(input("Enter your string: ")) else print("Isnt a integer")

if __name__ == "__main__": main()
