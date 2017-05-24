def times(time): # => [est, pst]
    time_arr = []
    est = 6
    pst = 9

    hour = int(time[0:2])
    est_hour = hour - est
    pst_hour = hour - pst

    if est_hour < 0:
        est_hour += 24
    if pst_hour < 0:
        pst_hour += 24

    time_arr.append("EST: " + str(est_hour) + ":" + time[3:5])
    time_arr.append("PST: " + str(pst_hour) + ":" + time[3:5])

    return time_arr

def timezones():
    time = raw_input("enter time (eg: 3:00, 14:00): ")

    if len(time) < 5:
        time = "0" + time

    time = times(time)

    for t in time:
        print t

def main():
    timezones()

main()
