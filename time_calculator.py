def fold_hours(hours):
    days = hours // 24
    hours = hours % 24
    return [days, hours]


def fold_minutes(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    return [hours, minutes]


def add_time(start, duration, *args):
    days_of_week = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]

    # Split hours and minutes.
    [th, tmp] = start.split(":")
    [dh, dm] = duration.split(":")

    # Split AM/PM from minutes.
    [tm, mid] = tmp.split(" ")

    # Convert to int.
    th = int(th)
    tm = int(tm)
    dh = int(dh)
    dm = int(dm)

    # Adjust to 24 hour time.
    if mid.lower() == "pm":
        th = th + 12

    hours = th + dh
    minutes = tm + dm
    [h, minutes] = fold_minutes(minutes)
    hours += h
    [days, hours] = fold_hours(hours)

    if hours == 0:
        new_time = "12:{:0>2d} AM".format(minutes)
    elif hours < 12:
        new_time = "{:d}:{:0>2d} AM".format(hours, minutes)
    elif hours == 12:
        new_time = "{:d}:{:0>2d} PM".format(hours, minutes)
    else:
        new_time = "{:d}:{:0>2d} PM".format(hours - 12, minutes)

    # Handle the optional start day.
    if len(args) == 1:
        day = args[0]
        dow = days_of_week.index(day.lower().capitalize())
        day = days_of_week[(dow + (days % 7)) % 7]
        new_time += ", {}".format(day)

    if days > 0:
        if days == 1:
            new_time += " (next day)"
        else:
            new_time += " ({:d} days later)".format(days)

    return new_time
