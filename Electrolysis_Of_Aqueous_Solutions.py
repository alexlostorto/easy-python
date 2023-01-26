REACTIVITY_SERIES = {
    'Potassium': 24,
    'Sodium': 23,
    'Lithium': 22,
    'Barium': 21,
    'Strontium': 20,
    'Calcium': 19,
    'Magnesium': 18,
    'Aluminium': 17,
    'Manganese': 16,
    'Zinc': 15,
    'Chromium': 14,
    'Iron': 13,
    'Cadmium': 12,
    'Cobalt': 11,
    'Nickel': 10,
    'Tin': 9,
    'Lead': 8,
    'Hydrogen': 7,
    'Antimony': 6,
    'Bismuth': 5,
    'Copper': 4,
    'Mercury': 3,
    'Silver': 2,
    'Gold': 1,
    'Platinum': 0,
}


def formatString(string):
    # Capitalises the first letter of the string
    return string.lower().capitalize()


def main():
    while True:
        # Asks the user for the element
        element = formatString(input("Element: "))
        if element in REACTIVITY_SERIES:
            # If the element is in the reactivity series, stop the loop
            break

    if REACTIVITY_SERIES[element] > 7:
        print(f"Hydrogen will be produced in an aqueous solution.")
    else:
        print(f"{element} will be produced in an aqueous solution.")


if __name__ == '__main__':
    main()
