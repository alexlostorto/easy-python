from turtle import *


def main():
    # Ask user the number of sides
    n = input("Number of sides: ")

    # Convert input to int if input is a number
    if n.isnumeric():
        n = int(n)

    exteriorAngle = 360 / n
    print(f"Exterior angle: {exteriorAngle}")
    for i in range(n):
        forward(100)
        right(exteriorAngle)

    # So the program doesn't instantly close
    Screen().exitonclick()


if __name__ == '__main__':
    main()
