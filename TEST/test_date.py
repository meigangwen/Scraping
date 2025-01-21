import datetime

if __name__ == '__main__':
    # specify the API URL without the offset
    now = datetime.datetime.now()
    print("Current date and time:", now)

    today = datetime.date.today()
    print(today)

    last_10_days = []

    for i in range(1, 11):  # Start from 1 because we are counting from today backwards
        day = today - datetime.timedelta(days=i)
        last_10_days.append(day)

    # Print the dates
    for date in last_10_days:
        print(date)

    date_string = today.strftime("%Y.%m.%d")
    print(date_string)

    test_string = "2023.01.21"
    date_object = datetime.datetime.strptime(test_string, "%Y.%m.%d").date()
    print(date_object)


