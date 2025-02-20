from utils import add, multiply, sqrt

def main():
    print("You are on master branch")
    result = multiply(80.5, 33)
    print(f"The result of multiplication is {result}")

    n = 144
    result = sqrt(144)
    print(f"The square root of {n} = {result}")

main()