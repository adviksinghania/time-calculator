def add_time(start, duration, day=None):
    # days in a week
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

    # initial time and the duration to be added in hours and minutes
    init_time = list(map(int, start[:-3].split(':')))
    duration = list(map(int, duration.split(':')))

    # adding the minutes to the initial time
    init_time[1] += duration[1]
    count = 0  # to store the extra number of hours (60 minutes)
    while init_time[1] > 60:
        count += 1
        init_time[1] -= 60
    
    # adding the hours to the initial time
    init_time[0] += count + duration[0]
    count = 0  # to store the number of days
    while init_time[0] >= 12:
        init_time[0] -= 12
        if 'PM' in start:
            # increment the count for days if time crosses the PM mark
            count += 1
            # and replace PM with AM
            start = start.replace('PM', 'AM')
        elif 'AM' in start:
            # else replace AM with PM
            start = start.replace('AM', 'PM')

    init_time[0] = '12' if init_time[0] == 0 else str(init_time[0])
    init_time[1] = str(init_time[1]).rjust(2, '0')
    new_time = ':'.join(init_time) + start[-3:]

    if day is not None:
        day = day.lower().capitalize()
        days = days[days.index(day):] + days[:days.index(day)]
        n = count
        while n > 7:
            n -= 7
        new_time += ', ' + days[n]
    
    if count == 1:
        new_time += ' (next day)'
    elif count > 1:
        new_time += ' (' + str(count) + ' days later)'

    return new_time
