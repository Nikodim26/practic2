from datetime import datetime, timedelta


def fgfdgfdg(times):
    new_time = []
    for time in times:
        date_obj = datetime.strptime(time, "%Y.%m.%d")  #
        new_date_obj = datetime.strftime(date_obj + timedelta(days=7), "%B %#d, %Y")

        new_time.append(f'{new_date_obj}')

    return new_time


if __name__ == '__main__':
    t1 = ["2022.12.31", "2023.1.7", "2023.1.14"]
    print(fgfdgfdg(t1))
