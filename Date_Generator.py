DAYS = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']
TIMES = ['AM', 'PM']
WEEK_START = 5  # What date is Monday
MONTH = 'June'
YEAR = '2023'
TIME = True  # Print AM and PM after each date


def main():
    for day in range(WEEK_START, 32):
        if not TIME:
            print(f"{DAYS[(day % 7) - (WEEK_START % 7)]} {day} {MONTH} {YEAR}")
            continue
        for time in range(2):
            print(
                f"{DAYS[(day % 7) - (WEEK_START % 7)]} {day} {MONTH} {YEAR} {TIMES[time]}")


if __name__ == '__main__':
    main()
