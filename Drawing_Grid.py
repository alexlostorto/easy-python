# Import pandas package
import pandas as pd


def getInput(prompt):
    userInput = input(prompt)
    if userInput.isnumeric():
        return int(userInput)
    else:
        getInput(prompt)


def main():
    rows = getInput("Number of rows: ")
    columns = getInput("Number of columns: ")
    height = getInput("Grid height: ")
    width = getInput("Grid width: ")

    cellHeight = height/rows
    cellWidth = width/columns

    print("\n\n-----GRID DIMENSIONS-----")
    print(f"Cell Height: {cellHeight}")
    print(f"Cell Width: {cellWidth}\n\n")

    grid = []

    column = []
    for i in range(rows + 1):
        column.append(i * cellHeight)
    grid.append(column)

    for i in range(columns + 1):
        column = [i * cellWidth]
        for i in range(rows):
            column.append("_")
        grid.append(column)

    print("-----GRID-----")
    df = pd.DataFrame(grid)
    print(df.to_string(index=False, header=False))


if __name__ == '__main__':
    main()
