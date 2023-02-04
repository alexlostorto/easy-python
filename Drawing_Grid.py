# Import pandas package
import pandas as pd


def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def getInput(prompt):
    userInput = input(prompt)
    if isFloat(userInput):
        return userInput
    else:
        getInput(prompt)


def main():
    rows = int(getInput("Number of rows: "))
    columns = int(getInput("Number of columns: "))
    height = float(getInput("Grid height: "))
    width = float(getInput("Grid width: "))

    cellHeight = height/rows
    cellWidth = width/columns

    print("\n\n-----GRID DIMENSIONS-----")
    print(f"Cell Height: {round(cellHeight, 1)}")
    print(f"Cell Width: {round(cellWidth, 1)}\n\n")

    grid = []

    column = []
    for i in range(columns + 1):
        column.append(round(i * cellWidth, 1))
    grid.append(column)

    for i in range(rows):
        column = [round((i + 1) * cellHeight, 1)]
        for i in range(columns):
            column.append("_")
        grid.append(column)

    print("-----GRID-----")
    df = pd.DataFrame(grid)
    print(df.to_string(index=False, header=False))


if __name__ == '__main__':
    main()
