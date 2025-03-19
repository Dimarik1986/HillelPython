
total_seconds = [0, 224930, 466289, 950400, 1209600, 1900800, 8639999, 22493, 7948799]

for total_second in total_seconds:
    x = 60 * 60 * 24
    y = 60 * 60

    days = total_second // x

    hours = total_second % x//y

    minutes = (total_second % y) // 60
    seconds = total_second % 60

    print(f"{total_second}, -> ,{days} days, {hours}:{minutes}:{seconds}")