from utils import add
# the above also executes the code of that module, that's why the print function of that script ran
# so, don't put code in the script you're importing

def main():
    print("You are on feature a branch")
    a = 10
    b = 50
    result = add(a,b)
    print(f"The result of the addition is {result}")

main()